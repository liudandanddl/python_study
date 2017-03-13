#!/usr/bin/env python
# coding=utf-8
from SocketServer import StreamRequestHandler, TCPServer
import socket
from time import ctime
import traceback

__author__ = 'ldd'

HOST = ''
PORT = 21571
BUFSIZ = 1024
ADDR = (HOST, PORT)


class MyRequestHandler(StreamRequestHandler):

    # def handle(self):  # 重新handle方法,父类中该方法是空的，配合客户端每次都是一个新的套接字链接看print的输出可知
    #     print('...connected from : ', self.client_address)
    #     data = '[%s] %s' % (ctime().encode('utf-8'), self.rfile.readline())
    #     print(data)
    #     self.wfile.write(data)  # 将输入和输出套接字看成类似文件的对象，用readline来获取客户端信息和write将字符串发送给客户端

    # 配合客户端，为每个客户端维持并使用单链接，而不是上面那张每个请求一个链接
    def handle(self):  # 重新handle方法,父类中该方法是空的，
        while True:
            try:
                print('...connected from : ', self.client_address)
                data = self.rfile.readline()
                if data:
                    data = '[%s] %s' % (ctime().encode('utf-8'), data)
                    print(data)
                    self.wfile.write(data)  # 将输入和输出套接字看成类似文件的对象，用readline来获取客户端信息和write将字符串发送给客户端
                else:
                    break
            except:
                traceback.print_exc()
                break

if __name__ == "__main__":
    tcpServer=TCPServer(ADDR, MyRequestHandler, bind_and_activate=True)  # 用给定的主机信息和请求处理类创建了TCP服务器
    print('waiting for connection...')
    tcpServer.serve_forever()  # 无限循环的等待并服务于客户端请求