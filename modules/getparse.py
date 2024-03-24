from colorama import Fore
import validators


def get() -> str:

    url = input(Fore.YELLOW + '\n----ENTER-URL---► ' + Fore.BLUE)
    print(Fore.YELLOW, 'Processing...\n')
    prc = True
    if url[-1] != '/':
        url = url + '/'

    if validators.url(url) != True:
        url = 'https://' + url
    return url
