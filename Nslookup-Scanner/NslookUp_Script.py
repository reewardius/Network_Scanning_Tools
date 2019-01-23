# Nslookup Script in Python.
# done by Sri ManikantaPalakollu.
# Python v3.6.7

import socket

while True:

    print('1. IP ADDRESS FINDER.')
    print('2. SERVER ADDRESS FINDER.')
    print('3. Exit')
    choice = input('Enter your Choice:')

    try:
        if int(choice) == 1:
            url = input('Enter a valid URL without HTTP/HTTPS:')
            print('Non-authoritative answer:')
            print('Name : {}'.format(url))
            print('Address : {}'.format(socket.gethostbyname(url)))
            print('\n')
        elif int(choice) == 2:
            url = input('Enter a Ip Address:')
            print('Address : {}'.format(socket.gethostbyaddr(url)[0]))
            print('\n')
        elif int(choice) == 3:
            print('Thanks for Using it.')
            print('Scripted by Sri Manikanta.')
            break
        else:
            print('Please Enter a valid URL')
    except socket.error:
        print(socket.error)


