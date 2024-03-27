from modules import depcheck
from modules import adminf, bannerise
from modules import wpusr
from modules import headerscan
from colorama import init, Fore
from os import system as terminator
from modules import proxyguy
init()
depcheck.check_for_deps()
try:
    current_proxy = proxyguy.getcurrent(True)

except IndexError:
    current_proxy = None

def get_prompt():
    print(Fore.YELLOW, f'''   CHOOSE AN OPTION:
        1. General Headers Scan
        2. Admin and Other Common Pages Scan
        3. WordPress Users List Scan (CVE-2017-5487)
        99. Set Proxy (Corrent Proxy: {current_proxy['menu']})
        0. Exit
        ''')
    inp = input('-------► ')
    try:
        if int(inp) == 1:
            headerscan.scan()
            print('Press Enter To Continue.')
            input()
            terminator('clear')
            bannerise.banner()
            get_prompt()
        elif int(inp) == 2:
            adminf.find_admin()
            print('Press Enter To Continue.')
            input()
            terminator('clear')
            bannerise.banner()
            get_prompt()
        elif int(inp) == 3:
            wpusr.scan()
            print('Press Enter To Continue.')
            input()
            terminator('clear')
            bannerise.banner()
            get_prompt()
        elif int(inp) == 0:
            exit(Fore.GREEN + '\nGOODBYE MY FRIEND:)' + Fore.RESET)
        else:
            print(Fore.RED, 'Wrong Option Given!', Fore.RESET)
            ask = input('\nTry Again? [y/n]: ').lower()
            if ask == 'y':
                terminator('clear')
                bannerise.banner()
                get_prompt()
            elif ask == 'n':
                exit('\nGOODBYE DEAR!')
            else:
                exit('\nwrong choice again! I\'m leaving...')
    except ValueError:
        print('USE NUMBERS ONLY! Press Enter to try again.')
        input()
        terminator('clear')
        bannerise.banner()
        get_prompt()


try:
    bannerise.load()
    get_prompt()
except KeyboardInterrupt:
    exit('\nExiting...')
