import socket
import ssl
import sys
import os 

class sslServ:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.s = None

    def bindSocket(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            print('Socket successfully created')
        except socket.error as err:
            print('Socket creation failed with ' + str(err))
            sys.exit()
        try:   
            self.s.bind((self.host,self.port))
            print('Socket is binded to port '+ str(self.port))
        except socket.error as err:
            print('Socket binding failed with ' + str(err))
            sys.exit()
        try:
            self.s.listen(1)
            print('Socket is listing')
        except socket.error as err:
            print('Socket listening failed with ' + str(err))
            sys.exit()
        self.getRequest()
    
    def readPassFile(self):
        data = {}
        if os.path.isfile('password'):
            with open ('password', 'r') as fp:
                for line in fp:
                    word = line.split()
                    data[word[0]] = word[1]
                fp.close()
        return data

    def getRequest(self):
        client, addr = self.s.accept()
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
        userID, password = [str(i) for i in secure_soc.recv(1024).decode('utf-8').split('\n')]
        data = self.readPassFile()
        if userID in data:
            if data[userID] == password:
                result = 'correct ID and password'
            else:
                result = 'incorrect ID and password'
        else:
            result = 'incorrect ID and password'
        secure_soc.send(str.encode(result))
        self.s.close()
        secure_soc.close()
        print('Server closed')

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('Invalid input. Please enter python program_name.py')
        sys.exit()
    else:
        host = socket.gethostname()
        port = 3000
        serv = sslServ(host,port)
        serv.bindSocket()