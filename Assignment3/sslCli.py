import socket
import sys
import ssl

class sslCli:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.s = None

    def bindSocket(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print('Socket successfully created')
        except socket.error as err:
            print('Socket creation failed with ' + str(err))
            sys.exit()
        self.makeRequest()
    
    def makeRequest(self):
        try:
            secure_soc = ssl.wrap_socket(self.s,
                                        server_side=False,
                                        ca_certs='smestry1.pem',
                                        cert_reqs=ssl.CERT_REQUIRED)
        except socket.error as err:
            print('SSL wrap failed ' + str(err))
            sys.exit()
        try:
            secure_soc.connect((self.host, self.port))
        except:
            print('No server found on ' + str(self.host) + ' at port ' + str(self.port))
            sys.exit()
        print('\nPlease enter User ID:\n')
        userID = (str(input())).strip()
        print('\nPlease enter Password:\n')
        password = (str(input())).strip()
        secure_soc.sendall(str.encode('\n'.join([userID,password])))
        reply = str(secure_soc.recv(1024).decode('utf-8'))
        print(reply.strip())
        self.s.close()
        secure_soc.close()
        print('Client closed')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Invalid input. Please enter python program_name.py domain_name')
        sys.exit()
    else:
        host = sys.argv[1]
        port = 3000
        cli = sslCli(host,port)
        cli.bindSocket()
