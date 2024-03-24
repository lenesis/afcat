import requests
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from colorama import Fore
from os import system as terminator
from modules import getparse

disable_warnings(InsecureRequestWarning)
user_agent = {'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'}


def __fetch(target_url):
    endpoints = [
        "/?rest_route=/wp/v2/users/",
        "/wp-json/wp/v2/users/",
    ]
    i = 0
    for ep in endpoints:
        url = f"{target_url}{ep}"
        response = requests.get(url, timeout=7, headers=user_agent, verify=False, allow_redirects=False)
        if response.status_code == 200:
            i += 1
            user_data = response.json()
            if user_data:
                for user in user_data:
                    print(f"\n{Fore.LIGHTCYAN_EX} ---[ {target_url} ]---> {Fore.GREEN} [ {user['slug']} ] {Fore.RESET}")
    else:
        if i == 0:
            print (Fore.RED + 'NO RESULTS FOUND:(' + Fore.RESET)
    return


def scan():
    try:
        prc = False
        url = getparse.get()
        
        __fetch(url)


    except KeyboardInterrupt:
        if prc:
            print(Fore.YELLOW, 'Stopped Processing.', Fore.RESET)

            
        else:
            print('\nExiting...')
    except ConnectionError:
        print ("Could not connect:(\ncheck your internet connection.")
        input ('Press Enter to Continue')
    except:
        print(Fore.RED, 'Invalid URL GIVEN:(', Fore.RESET)
        ask = input('\nTry Again? [y/n]: ').lower()
        if ask == 'y':
            terminator('clear')
            scan()
        elif ask == 'n':
            exit('\nGOODBYE DEAR!')
        else:
            exit('\nwrong choice again! I\'m leaving...')

