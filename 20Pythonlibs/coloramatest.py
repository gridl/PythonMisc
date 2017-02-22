from colorama import init, Fore, Back, Style
init(autoreset=True)

messages = ['test test', (Fore.LIGHTYELLOW_EX + Style.BRIGHT + Back.MAGENTA + 'Alert!!!'), 'test test']

for m in messages:
    print(m)