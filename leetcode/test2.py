#!/usr/bin/env python
# coding=utf-8
from collections import Counter
import copy
import sys

__author__ = 'ldd'


def minWindow(s, t):
    # res = ''  # 返回的最小窗口
    # t_d = {}
    # for i in t:
    #     t_d[i] = t_d.get(i, 0)+1
    # start = 0
    # l_s = len(s)
    # end = l_s-1
    # s_d = copy.copy(t_d)
    # flag = True
    # while end < l_s and start < l_s:
    #     if s[start] not in t:
    #         start += 1
    #         continue
    #     if flag:
    #         end = start
    #         flag = False
    #     if s[end] in s_d.keys():
    #         s_d[s[end]] -= 1
    #         if s_d[s[end]] == 0:
    #             s_d.pop(s[end])
    #     if not s_d:
    #         res_now = s[start: end+1]
    #         res = res_now if (len(res) >= len(res_now) or res == '') else res
    #         start += 1
    #         end = l_s-1
    #         s_d = copy.copy(t_d)
    #         flag = True
    #         continue
    #     end += 1
    # return res

    res = s
    t_d = {}
    flag = True
    for i in range(len(s)):
        if s[i] in t:
            flag = False
            start = i  # 初始位置
            end = start
            break
    if flag:
        return ''
    for i in t:
        t_d[i] = t_d.get(i, 0) + 1
    s_d = copy.copy(t_d)
    flag1 = False
    while end < len(s) and start < len(s):
        print(res, start, end)
        if s[end] in s_d.keys():
            if s_d[s[end]] == 1:
                s_d.pop(s[end])
            else:
                s_d[s[end]] -= 1
        if not s_d:
            flag1 = True
            res_now = s[start: end+1]
            res = res_now if len(res) >= len(res_now) else res
            s_d = copy.copy(t_d)
        if flag1:
            if s[end] != s[start]:
                end += 1
            else:
                start += 1
                if s[start] == s[end]:
                    res_now = s[start: end+1]
                    res = res_now if len(res) >= len(res_now) else res
                    end += 1
        else:
            end += 1
    return res


class testA():
    def p(self):
        print('A')

class testB():
    def p(self):
        print('B')

class testC(testB, testA):
    def p(self):
        pass


if __name__ == "__main__":
    c = testC()
    c.p()