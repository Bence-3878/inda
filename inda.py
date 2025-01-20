#!/usr/bin/python3
# verzió: beta 1.3
# Script neve: inda.py
# Copyright (C) 2025 [Saját Neved]
#
# Ez a program szabad szoftver: terjeszthető és/vagy módosítható a
# Free Software Foundation által közzétett GNU General Public License
# (GPL) 3-as verziója vagy (tetszés szerint) bármely későbbi verziója
# feltételei szerint.
#
# Ez a program remélhetőleg hasznos lesz, de minden GARANCIA NÉLKÜL,
# még az eladhatóságra vagy egy adott célra való alkalmasságra sem.
# Lásd a GNU General Public License-t további részletekért.
#
# A GNU General Public License másolatát meg kellett kapnod a programmal együtt.
# Ha nem, látogass el a <https://www.gnu.org/licenses/> oldalra.

import os
import sys
import platform
import requests
from bs4 import BeautifulSoup

def get_config_folder():
    system = platform.system()

    if system == "Windows":
        # Az AppData/Local könyvtárat használja Windows rendszeren
        return os.path.join(os.getenv('APPDATA'), "inda")
    elif system == "Darwin":  # macOS esetében
        # A felhasználói könyvtár alatti "Library/Application Support" használata
        return os.path.join(os.path.expanduser("~"), "Library", "Application Support", "inda")
    else:  # Linux (vagy egyéb Unix rendszerek)
        # A szabványos .config könyvtárat használja
        return os.path.join(os.path.expanduser("~"), ".config", "inda")



CONFIG_FOLDER = get_config_folder()

sess = requests.Session()

def upload(files):
    os.makedirs(CONFIG_FOLDER, exist_ok=True)
    auth_path = os.path.join(CONFIG_FOLDER, "auth")
    username, password = None, None
    config_path = os.path.join(CONFIG_FOLDER, "config")
    if not os.path.isfile(config_path):
        config()
    try:
        with open(config_path, "rb") as f:
            tags, isPrivate, isUnlisted= f.read().decode().strip().split("\n")
    except Exception as e:
        print(f"Nem várt hiba történt: {e}")
        exit(11)
    if not os.path.isfile(auth_path):
        print("felhasználónév:")
        username = input()
        print("jelszó:")
        password = input()
        with open(auth_path, "wb") as f:
            f.write(f"{username}\n{password}".encode())
    try:
        with open(auth_path, "rb") as f:
            username, password = f.read().decode().strip().split("\n")
    except Exception as e:
        print(f"Nem várt hiba történt: {e}")
        exit(2)
    if not username or not password:
        print("Hiányzó hitelesítő adatok.")
        exit(3)


    try:
        response = sess.get("https://indavideo.hu/login")
        response = sess.post("https://daemon.indapass.hu/http/login",
                                 data={"username": username, "password": password
                                     ,"partner_id": "indavideo", "redirect_to": "//indavideo.hu/login"})
    except requests.exceptions.RequestException as e:
        print(f"HTTP kérés hiba: {e}")
        exit(4)
    if response.status_code != 200:
        print("Sikertelen bejelentkezés.")
        exit(5)
    soup = BeautifulSoup(response.text, "html.parser")
    error_element = soup.find("div", {"class": "error"})
    error = error_element.text if error_element else None
    if error:
        print(error)
        exit(6)


    url = "https://upload.indavideo.hu/"
    
    grouped_files = []
    current_file = []
    
    for file in files[2:]:
        if os.path.splitext(file)[1]:  # Check if there is a file extension
            if current_file:
                grouped_files.append(" ".join(current_file))
                current_file = []
            grouped_files.append(file)
        else:
            current_file.append(file)
    
    if current_file:
        grouped_files.append(" ".join(current_file))
    
    for file in grouped_files:
        title = os.path.basename(file)
        title = title[:title.rfind(".")]


        response = sess.get(url)
        if response.status_code != 200:
            print(f"Hiba történt az oldal lekérése közben: {response.status_code}")
            exit(7)
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            file_hash_input = soup.find("input", {"name": "upload_data[file_hash]"})
            file_hash = file_hash_input["value"] if file_hash_input and "value" in file_hash_input.attrs else None
            
            user_id_input = soup.find("input", {"name": "upload_data[user_id]"})
            user_id = user_id_input["value"] if user_id_input and "value" in user_id_input.attrs else None
        except AttributeError:
            print("Hiba az oldalelemek feldolgozásakor.")
            exit(8)
        if not file_hash or not user_id:
            print("A feltöltéshez szükséges adatok hiányoznak.")
            exit(9)
        url2 = f"https://upload.indavideo.hu/upload.php?FILE_HASH={file_hash}&UID={user_id}&isIframe=1"

        with open(file, "rb") as opened_file:
            file_ = {"file": opened_file}
            response = sess.post(url2, files={
                "FILE_HASH": (None, file_hash),
                "Filedata": (os.path.basename(file), opened_file, "video/mp4")
            })
            if response.status_code != 200:
                print("Nem sikerült a videót feltölteni.")
                exit(10)


        response = sess.post(url, data={
            "upload_data[file_hash]": file_hash,
            "upload_data[parent_id]": "0",
            "upload_data[user_id]": user_id,
            "id_preset": "",
            "upload_data[pushToFb]": "",
            "upload_data[title]": title,
            "upload_data[description]": "",
            "upload_data[tags]": tags,
            "upload_data[isPrivate]": isPrivate,
            "upload_data[isUnlisted]": isUnlisted,
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
        soup = BeautifulSoup(response.text, "html.parser")
        video_link_div = soup.find("div", {"class": "video_link"})
        if not video_link_div:
            print("Hiba: Nem található 'video_link' osztályú div az oldalon.")
            return

        video_link_input_elems = video_link_div.find("input", {"type": "text"})
        if not video_link_input_elems:
            print("Hiba: A 'video_link' div nem tartalmaz input mezőt.")
            return

        if "value" in video_link_input_elems.attrs:
            link = video_link_input_elems["value"]
            print(f"Videó Link: {link}")
        else:
            print("Hiba: Az input mezőben nincs 'value' attribútum.")
    return

def config():
    os.makedirs(CONFIG_FOLDER, exist_ok=True)
    config_path = os.path.join(CONFIG_FOLDER, "config")
    if os.path.isfile(config_path):
        n = None
        while n != "3":
            print("(1) list\n(2) edit\n(3) exit")
            n = input()
            if n == "1":
                with open(config_path, "rb") as f:
                    tags, isPrivate, isUnlisted= f.read().decode().strip().split("\n")
                print(f"Címkék: {tags}\n")
                if isPrivate == "1" and isUnlisted == "0":
                    print("Láthatoség: Privált")
                if isPrivate == "0" and isUnlisted == "1":
                    print("Láthatoség: Nem listázot")
                if isPrivate == "0" and isUnlisted == "0":
                    print("Láthatoség: Publikus")

            elif n == "2":
                with open(config_path, "rb") as f:
                    tags, isPrivate, isUnlisted= f.read().decode().strip().split("\n")
                print("Címkék: ")
                tags = input()
                print("Láthatoség: (1) Publikus\n"
                      "            (2) Nem listázot\n"
                      "            (3) Privált")
                l = input()
                if l == "1":
                    isPrivate  = "0"
                    isUnlisted = "0"
                elif l == "2":
                    isPrivate  = "0"
                    isUnlisted = "1"
                elif l == "3":
                    isPrivate  = "1"
                    isUnlisted = "0"
                with open(config_path, "wb") as f:
                    f.write(f"{tags}\n{isPrivate}\n{isUnlisted}".encode())
    else:
        with open(config_path, "wb") as f:
            print("Alapértemezet beállításokat kiván használni? [Y/n]")
            if input().lower() == "n":
                print("Címkék: ")
                tags = input()
                print("Láthatoség: (1) Publikus\n"
                      "            (2) Nem listázot\n"
                      "            (3) Privált")
                l = input()
                if l == "1":
                    isPrivate = "0"
                    isUnlisted = "0"
                elif l == "2":
                    isPrivate = "0"
                    isUnlisted = "1"
                elif l == "3":
                    isPrivate = "1"
                    isUnlisted = "0"
                with open(config_path, "wb") as f:
                    f.write(f"{tags}\n{isPrivate}\n{isUnlisted}".encode())
            else:
                f.write("Anime,\n0\n1".encode())



def main():
    if sys.argv[1] == "config":
        config()
        return 0
    if len(sys.argv) < 3 or sys.argv[1] != "upload":
        print("Használata: python inda.py upload [files]")
        return 1
    upload(sys.argv)
    return 0



if __name__ == '__main__':
    main()


