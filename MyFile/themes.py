from colorama import Fore, Style, init

init(autoreset=True)

GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
CYAN = Fore.CYAN
WHITE = Fore.WHITE

RESET = Style.RESET_ALL
BRIGHT = Style.BRIGHT

BANNER = GREEN + BRIGHT + """
=========================================
        FILE BROWSER v1.0
=========================================
""" + RESET