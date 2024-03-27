from modules import getparse

def getproxy() -> str:
    with open('.proxy.afcat') as f:
        p = f.readlines()
    proxy = str(p[0])
    return proxy

def __setthis(proxy):
    with open('.proxy.afcat', 'w') as p:
        p.write(f'{proxy}')

def setproxy():
    proxy = getparse.get()
    __setthis(proxy)

def unsetproxy():
    __setthis('')