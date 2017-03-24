#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'

'''
FTP文件传输协议，它可以上传或下载文件，用户需要输入有效的用户名和密码，但也允许匿名登录，匿名登录的用户名是’anonymous‘密码一般是用户的电子邮件地址
'''

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'


def main():
    try:
        f = ftplib.FTP(HOST)
    except(socket.error, socket.gaierror) as e:
        print('ERROR: cannot reach ', str(HOST))
        return  # 发生错误直接退出
    print('*** Connected to host "%s' % HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login anonymously')
        f.quit()
        return  # 发生错误直接退出
    print('*** Login in as "anonymous"')

    try:
        f.cwd(DIRN)  # cd 到DIRN路径下
    except ftplib.error_perm:
        print('ERROR: cannot CD to "%s"' % DIRN)
        return  # 发生错误直接退出
    print('*** change to "%s" folder' % DIRN)

    try:
        # RETR 和 STOP 命令是FTP协议中的下载和上传命令
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write())
    except ftplib.error_perm:
        print('ERROR: cannot read file ', str(FILE))
        os.unlink(FILE)  # 删除文件
    else:
        print('*** Downloaded "%s" to CWD' % HOST)
    f.quit()

if __name__ == "__main__":
    main()