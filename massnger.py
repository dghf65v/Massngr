#!/bin/python3
import os
from socket import socket , AF_INET , SOCK_STREAM
s = socket(AF_INET,SOCK_STREAM)
host = str(input("Host >> "))
s.bind((host,4000))
s.listen(1)
c,a = s.accept()
print ("connection from {0}".format(a[0]))
while True:
    print(c.recv(1024))
    sender = str(input("< mssnger > "))
    sender = sender.encode("utf-8")
    c.send(sender)
c.close()

