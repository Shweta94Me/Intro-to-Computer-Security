import sys
from cryptography.fernet import Fernet
import os

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('Invalid input. Please enter python program_name.py')
        sys.exit()
    else:
        try:
            while(True):
                print('\nPlease enter User ID:\n')
                userID = (str(input())).strip()
                print('\nPlease enter Password:\n')
                password = (str(input())).strip()
                if os.path.isfile('password'):
                    mode = 'a+'
                else:
                    mode = 'w+'
                if os.path.isfile('key.key'):
                    with open('key.key', 'rb') as file:
                        key = file.read()
                        file.close()
                else:
                    key = Fernet.generate_key()
                    with open('key.key', 'wb') as file:
                        file.write(key)
                        file.close()
                cipher = Fernet(key)
                ep = cipher.encrypt(password.encode('utf-8')) #convert string to bytes type 
            
                with open('password', mode) as fp:
                    fp.write(userID + ' ' + ep.decode('utf-8') + '\n')
                    fp.close()
                print('\nPlease enter next entry.')
        except KeyboardInterrupt:
            print('Program existed successfully.')