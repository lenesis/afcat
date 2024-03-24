from modules import getparse
import requests
from colorama import Fore
from os import system as terminator
def scan():
    try:
        __reqhead = requests.get(getparse.get()).headers
        for key in __reqhead:
            print (f'{Fore.BLUE} [ {key} ]-----> {Fore.GREEN}{__reqhead[key]}{Fore.RESET}')
    except KeyboardInterrupt:
        print ('Leaving...')
    except ConnectionError:
        print ("Could not connect:(\ncheck your internet connection.")
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
        
    

