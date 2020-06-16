import socket
import sys
import ssl

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Invalid input. Please enter python program_name.py domain_name')
        sys.exit()
    else:
        host = sys.argv[1]
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print('Socket successfully created')
        except socket.error as err:
            print('Socket creation failed with ' + str(err))
        try:
            secure_soc = ssl.wrap_socket(s,
                                        server_side=False,
                                        ca_certs='smestry1.pem',
                                        cert_reqs=ssl.CERT_REQUIRED)
        except socket.error as err:
            print('SSL wrap failed ' + str(err))
            sys.exit()
        port = 3000
        try:
            secure_soc.connect((host, port))
        except:
            print('No server found on ' + str(host) + ' at port ' + str(port))
            sys.exit()
        print('\nPlease enter User ID:\n')
        userID = (str(input())).strip()
        print('\nPlease enter Password:\n')
        password = (str(input())).strip()
        secure_soc.sendall(str.encode('\n'.join([userID,password])))
        reply = str(secure_soc.recv(4096).decode('utf-8'))
        print(reply.strip())
        s.close()
        secure_soc.close()
        print('Client closed')