Shweta Sharad Mestry
smestry1@binghamton.edu
B00815342


***Programming language used***
Python (Code is written in Python 3.7.6 version)

***Code tested on***
remote.cs.binghamton.edu which having python version 2.7.16

***Execute program*** 
If python version is less than 3:
To run server :: python3 sslServ.py
To run client on remote.cs.binghamton.edu:: python3 sslCli.py remote.cs.binghamton.edu
Enter UserID and press enter.
Enter password and press enter.
If entered UserID and password match with userID and its corresponding password present in password file then program will print 'correct ID and password' otherwise 'incorrect ID and password'.

If python version is greater than 3:
To run server :: python sslServ.py
To run client :: python sslCli.py <host_name>

***Certificate creation using server's private key***
openssl req -new -x509 -days 365 -nodes -newkey rsa:4096 -out smestry1.pem -keyout privkey.pem
***Review generated certificate***
openssl x509 -text -noout -in smestry1.pem





