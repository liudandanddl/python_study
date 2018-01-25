#!/usr/bin/env python
# coding=utf-8
import Queue

__author__ = 'ldd'


def twoSum(nums, target):
    """
    从数组中查找两数相加=target,返回对应两数的下标。
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
    """
    for i in range(0, nums.__len__(), 1):
        find = target - nums[i]
        if find in nums:
            print(find, nums)
            j = nums.index(find)
            if i != j:
                return i, j
    return


def reverse(x):
    '''
    有符号23位整数的反数
    如123 rew=321  -123 res=-321  120res=21
    '''
    a = int(str(abs(x))[::-1])
    if x <0:
        a = -a
    if (pow(-2,31)<= a <= pow(2,31)):  # 有符号32位整数的取值范围
        return a
    return 0


def reverse1(x):
    '''
    :param x:int
    :return: bool
    判断一个整数是否是回文数,负数不是回文数。不开辟额外的空间。
    '''
    if x == 0:
        return True
    if (x<0) or (x%10==0):
        return False
    res = 0
    temp = x
    while(temp>0):  # 利用取模方式将数反转
        res *=10
        i = temp % 10
        temp = temp /10
        res +=i
    return True if x==res else False


def isValid(s):
    """
    输入是['(', '[', '{']或者[')', ']', '}']，判断括号使用是否合法
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




