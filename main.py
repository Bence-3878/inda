import sys
import os
import requests
from httplib2.auth import authentication_info
CONFIG_FOLDER = os.path.join(os.path.expanduser("~"), ".config", "inda")


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
    return None

def login():
    auth_path = os.path.join(CONFIG_FOLDER, "auth")
    if not os.path.isfile(auth_path):
        authentication()
    with open(auth_path, "rb") as f:
        username, password = f.read().decode().split("\n")


    response = requests.post(
        "https://daemon.indapass.hu/http/login",
        data={"username": username, "password": password,
              "partner_id": "indavideo", "redirect_to": "//indavideo.hu/login",
              "autologin": "on"},
    )
    print(response.cookies)
    return None

def upload():
    login()
    return None




def main():
    if len(sys.argv) == 1:
        print("Használat: python main.py [login/upload]")
        return
    elif sys.argv[1] == "login":
        authentication()
        return
    elif sys.argv[1] == "upload":
        upload()
        return



if __name__ == '__main__':
    main()


