#!/usr/bin/env python
# coding=utf-8
from _socket import AF_INET, SOCK_STREAM
from socket import socket

__author__ = 'ldd'


HOST = '127.0.0.1'
PORT = 21571
BUFSIZ = 1024
ADDR = (HOST, PORT)


if __name__ == "__main__":
    # # 每次发送信息的时候都创建了一个新的套接字
    # while True:
    #     tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 创建客户端套接字, 用的是IPV4
    #     tcpCliSock.connect(ADDR)
    #     data = raw_input('>')
    #     if not data:
    #         break
    #     tcpCliSock.send('%s\r\n' % data)  # 需要增加额外的回车和换行符，因为服务器用的readline，像处理文件一样，所以必须发送行终止符
    #     data = tcpCliSock.recv(BUFSIZ)
    #     if not data:
    #         break
    #     print(data)
    #     tcpCliSock.close()



    tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 创建客户端套接字, 用的是IPV4
    tcpCliSock.connect(ADDR)
    # 每次发送信息的时候不创建一个新的套接字，使用一个套接字链接
    while True:
        data = raw_input('>')
        if not data:
            break
        tcpCliSock.send('%s\r\n' % data)  # 需要增加额外的回车和换行符，因为服务器用的readline，像处理文件一样，所以必须发送行终止符
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data)
    tcpCliSock.close()