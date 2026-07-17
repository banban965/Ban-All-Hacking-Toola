# ui.py

from pathlib import Path

from themes import *
from utils import clear, pause
from file_ops import create_file, create_folder
from search import search

CURRENT = Path.home()


def header():
    clear()
    print(BANNER)
    print(CYAN + "Current Path")
    print(WHITE + str(CURRENT))
    print("-" * 60)


def list_files():
    header()

    items = sorted(CURRENT.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))

    if not items:
        print(YELLOW + "Folder is empty.")
    else:
        for i, item in enumerate(items, 1):
            if item.is_dir():
                print(GREEN + f"{i:03} 📁 {item.name}")
            else:
                print(WHITE + f"{i:03} 📄 {item.name}")

    pause()


def change_directory():
    global CURRENT

    header()

    folder = input("Folder (.. = Back): ").strip()

    new = (CURRENT / folder).resolve()

    if new.exists() and new.is_dir():
        CURRENT = new
        print("\nDirectory changed.")
    else:
        print("\nFolder not found.")

    pause()


def create_new_folder():
    header()

    name = input("Folder Name: ").strip()

    ok, msg = create_folder(CURRENT, name)

    print("\n" + msg)

    pause()


def create_new_file():
    header()

    name = input("File Name: ").strip()

    ok, msg = create_file(CURRENT, name)

    print("\n" + msg)

    pause()


def search_menu():
    header()

    keyword = input("Search: ").strip()

    result = search(CURRENT, keyword)

    print()

    if not result:
        print("No results.")
    else:
        for item in result:
            print(f"{item['type']} : {item['path']}")

    pause()


def menu():

    while True:

        header()

        print("[1] Browse Files")
        print("[2] Change Folder")
        print("[3] Search")
        print("[4] New Folder")
        print("[5] New File")
        print("[0] Exit")

        cmd = input("\nSelect > ").strip()

        if cmd == "1":
            list_files()

        elif cmd == "2":
            change_directory()

        elif cmd == "3":
            search_menu()

        elif cmd == "4":
            create_new_folder()

        elif cmd == "5":
            create_new_file()

        elif cmd == "0":
            break

        else:
            print("\nInvalid option.")
            pause()