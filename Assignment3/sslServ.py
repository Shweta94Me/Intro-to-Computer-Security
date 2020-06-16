import socket
import ssl
import sys
import os 

def readPassFile():
    data = {}
    if os.path.isfile('password'):
        with open ('password', 'r') as fp:
            for line in fp:
                word = line.split()
                data[word[0]] = word[1]
            fp.close()
    return data
    
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('Invalid input. Please enter python program_name.py')
        sys.exit()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print('Socket successfully created')
    except socket.error as err:
        print('Socket creation failed with ' + str(err))
    port = 3000
    s.bind(('127.0.0.1',port))
    print('Socket is binded to port '+ str(port))
    s.listen(1)
    print('Socket is listing')
    
    client, addr = s.accept()
    try:
        secure_soc = ssl.wrap_socket(client, 
                                     server_side=True, 
                                     certfile='smestry1.pem',
                                     keyfile='privkey.pem',
                                     ssl_version=ssl.PROTOCOL_TLSv1
                                     )
    except socket.error as err:
        print('SSL wrap failed ' + str(err))
        sys.exit()
    print('Got connection request from ' + str(addr))
    userID, password = [str(i) for i in secure_soc.recv(1024).decode('utf-8').split('\n')]
    print('UserID : ' + str(userID) + 'Password : ' + str(password))
    data = readPassFile()
    if userID in data:
        if data[userID] == password:
            result = 'correct ID and password'
        else:
            result = 'incorrect ID and password'
    else:
        result = 'incorrect ID and password'
    secure_soc.send(str.encode(result))
    s.close()
    secure_soc.close()
    print('Server closed')

    
        
    
