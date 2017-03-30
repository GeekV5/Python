#!/usr/bin/python
# -*- coding:UTF-8 -*-

# Socket通讯 客户端
import socket

IP = 'localhost'
PORT = 3333
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
def run():
    while True:
        s.connect((IP,PORT))
        s.send("Hell,node,I am HFP!!")
        # s.wait()
        print 'Send Suc!!'

if __name__=='__main__':
    run()

# data=s.recv(1024)

# print 'Receive from Node:',repr(data)