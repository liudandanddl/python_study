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

def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_ji = 1
    now_ji = 1
    n = 0
    while n < len(nums):
        if nums[n] > 0:
            now_ji *= nums[n]
            n += 1
        else:
            if n+1 < len(nums):
                if nums[n+1] < 0:
                    now_ji *= nums[n]*nums[n+1]
                    n += 2
                else:
                    now_ji = nums[n+1]
                    n += 2
            else:
                if now_ji:
                    pass

        max_ji = max_ji if max_ji > now_ji else now_ji
    return max_ji




if __name__ == "__main__":
    print(maxProduct([[2,3,-2,4]]))