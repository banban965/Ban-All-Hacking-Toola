#!/usr/bin/env python3

from colorama import init
from themes import BANNER
from utils import clear
from ui import menu

init(autoreset=True)

def main():
    clear()
    print(BANNER)
    menu()

if __name__ == "__main__":
    main()