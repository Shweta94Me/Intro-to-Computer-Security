import os
import sys
from cryptography.fernet import Fernet

def readPassFile():
    data = {}
    if os.path.isfile('password'):
        with open ('password', 'r') as fp:
            for line in fp:
                word = line.split()
                data[word[0]] = word[1]
            fp.close()
    else:
        print('password file does not exist')
        sys.exit()
    return data

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('Invalid input. Please enter python program_name.py')
        sys.exit()
    else:
        data = readPassFile()
        print('\nPlease enter User ID:\n')
        userID = (str(input())).strip()
        print('\nPlease enter Password:\n')
        password = (str(input())).strip()
        if userID in data:
            ep = data[userID]
            if os.path.isfile('key.key'):
                with open('key.key', 'rb') as fp:
                    key = fp.read()
                    fp.close()
            else:
                print('Key file does not exist')
                sys.exit()
            cipher = Fernet(key)
            dp = cipher.decrypt(ep.encode('utf-8'))
            if str(dp.decode('utf-8')) == str(password):
                print('The password is correct.')
                #decrypt ep and then compare with entered password
            else:
                print('The password is incorrect.')
        else:
            print('ID does not exist.')