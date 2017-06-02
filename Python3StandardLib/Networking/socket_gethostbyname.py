import socket

HOSTS = ['google','rush','www.python.org']

for host in HOSTS:
    print(host)
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print(' Hostname:', name)
        print('Aliases:', aliases)
        print('Addresses:', addresses)
    except socket.error as msg:
        print('ERROR:', msg)
    print()


