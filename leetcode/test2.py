#!/usr/bin/env python
# coding=utf-8
import Queue
from collections import Counter

__author__ = 'ldd'

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    给定一个字符串，找到最长的子串的长度没有重复字符。
    Given "abcabcbb", the answer is "abc", which the length is 3.
    Given "bbbbb", the answer is "b", with the length of 1.
    Given "pwwkew", the answer is "wke", with the length of 3.
    """
    # if s.__len__() == 0:
    #     return 0
    # max_str = s[0]
    # for k in range(0, s.__len__(), 1):
    #     temp = s[k]
    #     for i in range(k+1, s.__len__(), 1):
    #         if s[i] not in temp:
    #             temp+=s[i]
    #             if i == s.__len__()-1 and temp.__len__()>max_str.__len__():
    #                 max_str = temp
    #                 break
    #         else:
    #             if temp.__len__()>max_str.__len__():
    #                 max_str = temp
    #             break
    # return max_str.__len__()
    index = 0
    max = 0
    len = s.__len__()
    if len == 0:
        return 0
    if len == 1:
        return 1

    for i in range(1, len, 1):
        for j in range(i-1, index,-1):
            if s[i] == s[j]:
                index = j+1
                break
            else:
                if max < i-j+1:
                    max = i-j+1
    return max


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    q = Queue.LifoQueue()  # 先进后出队列
    for ele in s:
        if ele in ['(', '[', '{']:
            q.put(ele)  # 元素从右侧插入队列
        if ele in [')', ']', '}']:
            if q.empty():  # 判断队列是否为空
                return False
            if ele == ')' and q.get()!='(':  # q.get()从队列尾部获取元素，并从队列中删除该元素
                return False
            if ele == '}' and q.get()!='{':
                return False
            if ele == ']' and q.get()!='[':
                return False
    if not q.empty():
        return False
    return True

def test(nums, val):
    if nums==[]:
        return 0
    if val==None or val not in nums:
        return nums.__len__()
    i =0
    k = -1
    while(i<nums.__len__()):
        print(i, k, nums[i], nums[k+1], nums)
        if nums[i]!=val:
            k += 1
            nums[k] = nums[i]
        i += 1
    return k+1

def removeDuplicates(nums):
    if nums==[]:
        return 0
    if nums.__len__() == 1:
        return 1
    i=1
    k=0
    nums.sort()
    res = nums.__len__()
    while(i<nums.__len__()):
        print(i,k,nums[i], nums[i-1], nums)
        if nums[i]==nums[i-1]:
            nums[k]=nums[i]
            res -= 1
        i+=1

    return res

def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)


def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)

        for i, ele in enumerate(nums):
            if ele > target:
                return i
        return nums.__len__()


def maxSubArray(nums):
    """
    求数组的最大子串和。
    eg:[59, 26, -53, 58, 97, -93, -23, 84] res=187, [59, 26, -53, 58, 97]
    [-2,1,-3,4,-1,2,1,-5,4]  res=6, [4, -1, 2, 1]
    :type nums: List[int]
    :rtype: int
    """
    if nums.__len__() == 0:
        return 0
    max_end = nums[0]  # 目前最大值
    max_far = nums[0]  # 已知最大值
    res_end = [nums[0]]
    res_far = [nums[0]]  # 最终结果的子序列
    for temp in nums[1:]:
        print(temp, max_far, max_end, res_far, res_end)
        if max_end < 0:
            max_end = temp
            res_end = [temp]
        else:
            max_end += temp
            res_end.append(temp)
        max_far = max(max_end, max_far)
        if max_far == max_end:
            res_far = []
            for temp in res_end:
                res_far.append(temp)
    return max_far, res_far

if __name__ == "__main__":
    # [4,-1,2,1] has the largest sum = 6.
    # [-2,1,-3,4,-1,2,1,-5,4] 187
    # [59, 26, -53, 58, 97, -93, -23, 84]
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
