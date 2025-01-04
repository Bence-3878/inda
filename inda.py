import os
import sys

import requests
from bs4 import BeautifulSoup

CONFIG_FOLDER = os.path.join(os.path.expanduser("~"), ".config", "inda")

sess = requests.Session()

def authentication():
    os.makedirs(CONFIG_FOLDER, exist_ok=True)
    if os.path.isfile(os.path.join(CONFIG_FOLDER, "auth")):
        print("Már bejelentkezet. Kiván másik felhasználóba átjelentkezni? [y/N]")
        if input().lower() == "y":
            os.remove(os.path.join(CONFIG_FOLDER, "auth"))
            print("felhasználónév:")
            username = input()
            print("jelszó:")
            password = input()
            auth_path = os.path.join(CONFIG_FOLDER, "auth")
            with open(auth_path, "wb") as f:
                f.write(f"{username}\n{password}".encode())
    return username, password




def upload(files):
    auth_path = os.path.join(CONFIG_FOLDER, "auth")
    if not os.path.isfile(auth_path):
        authentication()
    try:
        with open(auth_path, "rb") as f:
            username, password = f.read().decode().split("\n")
    except FileNotFoundError:
        username,password = authentication()
    except Exception as e:
        print(f"Nem várt hiba történt: {e}")
        exit(1)


    try:
        response = sess.get("https://indavideo.hu/login")
        response = sess.post("https://daemon.indapass.hu/http/login",
                                 data={"username": username, "password": password
                                     ,"partner_id": "indavideo", "redirect_to": "//indavideo.hu/login"})
    except requests.exceptions.RequestException as e:
        print(f"HTTP kérés hiba: {e}")
        exit(1)
    if response.status_code != 200:
        print("Sikertelen bejelentkezés.")
        exit(1)
    soup = BeautifulSoup(response.text, "html.parser")
    error_element = soup.find("div", {"class": "error"})
    error = error_element.text if error_element else None
    if error:
        print(error)
        exit(1)


    url = "https://upload.indavideo.hu/"
    for file in files[2:]:
        title = os.path.basename(file)
        title = title[:title.rfind(".")]
        file_ = {"file": open(file, "rb")}

        response = sess.get(url)
        if response.status_code != 200:
            print(f"Hiba történt az oldal lekérése közben: {response.status_code}")
            exit(1)
        soup = BeautifulSoup(response.text, "html.parser")
        file_hash_input = soup.find("input", {"name": "upload_data[file_hash]"})
        if file_hash_input and "value" in file_hash_input.attrs:
            file_hash = file_hash_input["value"]

        user_id_input = soup.find("input", {"name": "upload_data[user_id]"})
        if user_id_input and "value" in user_id_input.attrs:
            user_id = user_id_input["value"]

        response = sess.post(url, data={"FILE_HASH": file_hash}, files=file_)
        if response.status_code != 200:
            print("Nem sikerült a videót feltölteni.")
            exit(1)
        response = sess.post(url, data={
            "upload_data[file_hash]": file_hash,
            "upload_data[parent_id]": "0",
            "upload_data[user_id]": user_id,
            "id_preset": "",
            "upload_data[pushToFb]": "",
            "upload_data[title]": title,
            "upload_data[description]": "",
            "upload_data[tags]": "Anime,",
            "upload_data[isPrivate]": "0",
            "upload_data[isUnlisted]": "1",
            "upload_data[is_commentable]": "on",
            "upload_data[channels][37]": "37",
            "upload_data[preset_title]": "",
            "upload_data[thumb_fname]": "",
            "upload_data[password]": "",
            "upload_data[password2]": "",
            "upload_data[pub_now]": "on",
            "upload_data[additional][additional-new][source]": "",
            "upload_data[additional][additional-new][title]": "",
            "upload_data[additional][additional-new][url]": "",
            "upload_data[additional][additional-new][description]": "",
            "upload_data[has_noads]": "on",
            "adultStatement": "on",
            "copyrightStatement": "on"
        })
        if response.status_code != 200:
            print("Nem sikerült elküldeni az ürlapot.")
        response = sess.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        video_link_input = soup.find("div", {"class": "video_link"}).find("input",
                                                                          {"type": "text", "readonly": "readonly"})
        if video_link_input and "value" in video_link_input.attrs:
            link = video_link_input["value"]
            print(f"Videó URL: {link}")





def main():
    if len(sys.argv) == 1:
        print("Használat: python inda.py login"
              "           python inda.py upload [files]")
        return 1
    elif sys.argv[1] == "login":
        authentication()
        return 0
    elif sys.argv[1] == "upload":
        if len(sys.argv) == 2:
            print("Használata: python inda.py upload [files]")
            return 1
        upload(sys.argv)
        return 0



if __name__ == '__main__':
    main()


