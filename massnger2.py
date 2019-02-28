#!/bin/python3
from socket import socket , AF_INET , SOCK_STREAM
s = socket(AF_INET,SOCK_STREAM)
host = str(input("Host >>"))
s.connect((host,4000))
while True:
    sender = str(input("< client >"))
    sender = sender.encode("utf-8")
    s.send(sender)
    print(s.recv(1000).decode("utf-8"))
#c.close()

