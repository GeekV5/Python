#!/usr/bin/python
# -*- coding:UTF-8 -*-

# Socket通讯 客户端
import socket
import time
IP = 'localhost'
PORT = 3333

def run():
    while True:

        time.sleep(6)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            s.connect((IP,PORT))
            s.send("Hell,node,I am HFP!!")
            # s.wait()
            print 'Send Suc!!'
        except socket.error, e:
            print "get connect error as", e
            continue
if __name__=='__main__':
    run()

# data=s.recv(1024)

# print 'Receive from Node:',repr(data)