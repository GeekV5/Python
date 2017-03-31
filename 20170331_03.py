#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 线程，套接字，哈希表，随机数
import socket
import struct
import hashlib
import base64
import threading
import random

# WebSocket聊天室
# 存放链接客户fd,元组
connectionlist = {}

# 发送指定的消息
def sendMessage(message):
    global connectionlist
    for connection in connectionlist.values():
        connection.send("\x00%s\xFF" %message)


def deleteconnection(item):
    global connectionlist
    del connectionlist['connection' + item]


class WebSocket(threading.Thread):
    def __init__(self, conn, index, name, remote, path="/"):
        threading.Thread.__init__(self)
        self.conn = conn
        self.index = index
        self.name = name
        self.remote = remote
        self.path = path
        self.buffer = ""

    def run(self):
        print 'Socket %s Start!' % self.index
        headers = {}
        self.handshaken = False

        while True:
            if self.handshaken == False:
                print 'Socket %s Start Handshaken with %s!' % (self.index, self.remote)
                self.buffer += self.conn.recv(1024)
                if self.buffer.find('\r\n\r\n') != -1:
                    header, data = self.buffer.split('\r\n\r\n', 1)
                    for line in header.split("\r\n")[1:]:
                        key, value = line.split(": ", 1)
                        headers[key] = value

                    headers["Location"] = "ws://%s%s" % (headers["Host"], self.path)
                    print "Location:",headers["Location"]
                    print "headers:",headers
                    #key1 = headers["Sec-WebSocket-Key1"]
                    #key2 = headers["Sec-WebSocket-Key2"]
                    if len(data) < 8:
                        data += self.conn.recv(8 - len(data))
                    #key3 = data[:8]
                    self.buffer = data[8:]
                    key = headers["Sec-WebSocket-Key"]
                    token = self.generate_token_2(self,key)
                    handshake = '\
HTTP/1.1 101 Web Socket Protocol Handshake\r\n \
Upgrade: WebSocket\r\n \
Connection: Upgrade\r\n \
Sec-WebSocket-Origin: %s\r\n \
Sec-WebSocket-Location: %s\r\n\r\n \
' % (headers['Origin'], headers['Location'])
                    self.conn.send(handshake + token)
                    self.handshaken = True
                    print 'Socket %s Handshaken with %s success!' % (self.index, self.remote)
                    sendMessage('Welcome, ' + self.name + ' !')
            else:
                self.buffer += self.conn.recv(64)
                if self.buffer.find("\xFF") != -1:
                    s = self.buffer.split("\xFF")[0][1:]
                    if s == 'quit':
                        print 'Socket %s Logout !' % (self.index)
                        sendMessage(self.name + ' Logout')
                        deleteconnection(str(self.index))
                        self.conn.close()
                        break
                    else:
                        print 'Socket %s Got msg: %s from %s!' % (self.index, s, self.remote)
                        sendMessage(self.name + ':' + s)
                        self.buffer = ""

    def generate_token_2(self, key):
        key =key+'258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
        ser_key = hashlib.sha1(key).digest()
        return base64.b64encode(ser_key)
    def generate_token(self, key1, key2, key3):
        num1 = int("".join([digit for digit in list(key1) if digit.isdigit()]))
        spaces1 = len([char for char in list(key1) if char == " "])
        num2 = int("".join([digit for digit in list(key2) if digit.isdigit()]))
        spaces2 = len([char for char in list(key2) if char == " "])
        combined = struct.pack(">II", num1 / spaces1, num2 / spaces2) + key3
        return hashlib.md5(combined).digest()

class WebSocketServer(object):
    def __init__(self):
        self.socket = None

    def begin(self):
        print "WebSocketSerber Start!"
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        IP ='localhost'
        PORT = 33333
        self.socket.bind((IP, PORT))
        self.socket.listen(50)

        global connectionlist

        i = 0
        while True:
            connection, address = self.socket.accept()
            username = address[0]

            newSocket = WebSocket(connection, i, username, address)
            newSocket.start()
            connectionlist['connection' + str(i)] = connection
            i = i + 1

if __name__ == "__main__":
    server = WebSocketServer()
    server.begin()