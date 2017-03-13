#!/usr/bin/env python
# coding=utf-8
from _socket import AF_INET, SOCK_STREAM
from socket import socket

__author__ = 'ldd'


HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


if __name__ == "__main__":
    tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 创建客户端套接字, 用的是IPV4
    tcpCliSock.connect(ADDR)
    while True:
        data = raw_input('>')
        if not data:
            break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8'))
    tcpCliSock.close()