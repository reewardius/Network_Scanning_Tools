# Nslookup Script in Python.
# Date 24/01/2019. 
# Done by Sri ManikantaPalakollu.
# Python v3.7.2

import socket
from termcolor import colored,cprint

# Banner function is used to create the banner on the terminal.
def banner():
    logo = '''  _   _     _                _                
 | \ | |___| |    ___   ___ | | ___   _ _ __  
 |  \| / __| |   / _ \ / _ \| |/ / | | | '_ \ 
 | |\  \__ \ |__| (_) | (_) |   <| |_| | |_) |
 |_| \_|___/_____\___/ \___/|_|\_\\__,_| .__/ 
                                       |_|    
            '''
    cprint(logo,color='red',attrs=['bold'])

# Scanner() is used to perform the nslookup and reverse nslookup operation.

def scanner():
    while True:

        # Options for the user.
        print('1. IP ADDRESS FINDER.')
        print('2. SERVER ADDRESS FINDER.')
        print('3. Exit')
        choice = input('Enter your Choice:')

        try:
            if int(choice) == 1:    # it returns the ipaddress as the output wich is nslookup scan.
                url = input('Enter a valid URL without HTTP/HTTPS:')
                print('\n')
                cprint('Non-authoritative answer:',color='cyan',attrs=['bold'])
                cprint('Name : {}'.format(url),color='cyan',attrs=['bold'])
                cprint('Address : {}'.format(socket.gethostbyname(url)),color='cyan',attrs=['bold'])
                print('\n')
            elif int(choice) == 2:  # it returns the server name as the outpuit which is the reverse nslookup scan.
                url = input('Enter a Ip Address:')
                print('\n')
                cprint('Address : {}'.format(socket.gethostbyaddr(url)[0]),color='cyan',attrs=['bold'])
                print('\n')
            elif int(choice) == 3:
                cprint('Thanks for Using it.',color='white',attrs=['bold'])
                cprint('Script written by Sri Manikanta.',color='white',attrs=['bold'])
                break
            else:
                print('Please Enter a valid URL')
        except socket.error:    # If any exception raised in try block it will produce the error message.
            print(socket.error)

# program start point.

if __name__  ==  '__main__':
    banner()
    scanner()
