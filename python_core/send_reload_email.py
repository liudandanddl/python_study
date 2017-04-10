#!/usr/bin/env python
# coding=utf-8
from poplib import POP3
from smtplib import SMTP
from time import sleep

__author__ = 'ldd'

'''
通过SMTP邮件服务器，发送一封测试电子邮件到目的地址，并马上通过POP3把电子邮件从服务器上取回来。
RFC2822要求消息头和正文需要用空行隔开。

'''
SMTPSVR = 'smtp.python.is.cool'
POP3SVR = 'pop.python.is.cool'
who = '1094684884@qq.com'
body = '''\
From: %(who)s
To: %(who)s
Subject: test msg
Hello World!
''' % {'who': who}

sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail(who, [who], body)
sendSvr.quit()
print(errs)
assert len(errs) == 0, errs
sleep(10)  # wait for mail to be delivered

recvSvr = POP3(POP3SVR)
recvSvr.user('wesley')
recvSvr.pass_('youllNeverGuess')
# 通过stat()方法得到可用消息列表，通过【0】符号选中第一条信息
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
# 遇到空行则表示在此之前是邮件头部，在此之后是邮件正文
sep = msg.index('')
recvBody = msg[sep+1:]
assert body == recvBody