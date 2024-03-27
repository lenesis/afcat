

def getcurrent(menu=False) -> dict:
    with open('.proxy.afcat') as f:
        p = f.readlines()
    
    proxy = p[0].split('$')
    if menu==False:
        return {proxy[0] : proxy[1]}
    else:
        return {'menu' : proxy[1]}
