#!/usr/bin/python
# -*- coding:UTF-8 -*-
import socket
import time
IP = 'localhost'
PORT = 3336

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP,PORT))
s.listen(1)
conn,addr = s.accept()
print 'Connected By ',addr
while 1:
    # data=conn.recv(1024)
    while 1:
        time.sleep(1)
        conn.sendall('123456!')
        print 'send 123456'
