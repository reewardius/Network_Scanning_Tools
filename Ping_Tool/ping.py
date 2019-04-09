# Ping Tool in Python3
# devloped by @Sri_Programmer
# python v3.7.2

# library imports

import subprocess
import platform

domain_name = input('Enter your domain name or IP Addresss: ')
system_OS = None
packets_number = input('Enter number of packets do you want to transmit: ')

if platform.system().lower() == 'windows':
    system_OS = '-n'
else:
    system_OS = '-c'

try: # To over any exceptions

    subprocess.call(['ping', system_OS, packets_number, domain_name])

except KeyboardInterrupt:
    quit()

except Exception as e:
    print(e)

