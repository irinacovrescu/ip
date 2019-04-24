#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import cIPDataBase

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   c.send('Thank you for connecting'.encode())
   print (c.recv(1024))

   mydb = cIPDataBase.myDataBase()
   print(mydb.askLogIn(c.recv(1024), "root"))
   print ("hei" + mydb.showInfo(c.recv(1024)))

   c.close()                # Close the connection