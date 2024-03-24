from os import system as terminator


def check_for_deps():
    print('Checking Dependencies, Please Wait.\n')

    terminator('pip list > .dep.afcat')
    f = open('.dep.afcat', 'r')
    installed = f.read()
    f.close()
    terminator('rm .dep.afcat')
    if 'requests' not in installed:
        terminator('pip install requests')
    if 'colorama' not in installed:
        terminator('pip install colorama')
    if 'validators' not in installed:
        terminator('pip install validators')
    terminator('clear')
