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
            return
        return
    return None








def main():
    if len(sys.argv) == 1:
        print("Használat: python main.py [login/upload]")
        return
    elif sys.argv[1] == "login":
        authentication()
        return
    elif sys.argv[1] == "upload":
        return



if __name__ == '__main__':
    main()


