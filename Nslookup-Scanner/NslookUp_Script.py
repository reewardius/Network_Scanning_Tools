# Nslookup Script in Python.
# Date 24/01/2019. 
# Done by Sri ManikantaPalakollu.
# Python v3.6.7

import socket

# Banner function is used to create the banner on the terminal.
def banner():
    print('''
                                           
   (_) _       (_)                (_)                                         (_)                                        
   (_)(_)_     (_)   _  _  _  _   (_)               _  _  _        _  _  _    (_)     _  _         _    _  _  _  _       
   (_)  (_)_   (_) _(_)(_)(_)(_)  (_)            _ (_)(_)(_) _  _ (_)(_)(_) _ (_)   _(_)(_)       (_)  (_)(_)(_)(_)_     
   (_)    (_)_ (_)(_)_  _  _  _   (_)           (_)         (_)(_)         (_)(_) _(_)  (_)       (_)  (_)        (_)    
   (_)      (_)(_)  (_)(_)(_)(_)_ (_)           (_)         (_)(_)         (_)(_)(_)_   (_)       (_)  (_)        (_)    
   (_)         (_)   _  _  _  _(_)(_) _  _  _  _(_) _  _  _ (_)(_) _  _  _ (_)(_)  (_)_ (_)_  _  _(_)_ (_) _  _  _(_)    
   (_)         (_)  (_)(_)(_)(_)  (_)(_)(_)(_)(_)  (_)(_)(_)      (_)(_)(_)   (_)    (_)  (_)(_)(_) (_)(_)(_)(_)(_)      
                                                                                                       (_)               
                                                                                                       (_)               
    
    ''')

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
                print('Non-authoritative answer:')
                print('Name : {}'.format(url))
                print('Address : {}'.format(socket.gethostbyname(url)))
                print('\n')
            elif int(choice) == 2:  # it returns the server name as the outpuit which is the reverse nslookup scan.
                url = input('Enter a Ip Address:')
                print('\n')
                print('Address : {}'.format(socket.gethostbyaddr(url)[0]))
                print('\n')
            elif int(choice) == 3:
                print('Thanks for Using it.')
                print('Script written by Sri Manikanta.')
                break
            else:
                print('Please Enter a valid URL')
        except socket.error:    # If any exception raised in try block it will produce the error message.
            print(socket.error)

# program start point.

if __name__  ==  '__main__':
    banner()
    scanner()
