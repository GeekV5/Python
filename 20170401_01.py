#!/usr/bin/python
# -*- coding:UTF-8 -*-

# Socket通讯 客户端
import socket
import time
IP = 'localhost'
PORT = 3333

def run():
    while True:
        # time.sleep(1)
        str=raw_input("请输入想要发送的消息：")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        s.connect((IP,PORT))
        s.send(str)
        # s.wait()
        print 'Send Suc!!时间：',time.time()
        s.close()

if __name__=='__main__':
    run()

# data=s.recv(1024)

# print 'Receive from Node:',repr(data)