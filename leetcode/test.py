#!/usr/bin/env python
# coding=utf-8
from collections import Counter

__author__ = 'ldd'


def reverse(x):
    print(pow(2,31),pow(-2,31), x)
    if (pow(-2,31)<= x <= pow(2,31)):
        a = int(str(abs(x))[::-1])
        if x <0:
            a = -a
        return a
    return 0


def reverse1(x):
    '''
    :param x:int
    :return: bool
    判断一个整数是否是回文数,负数不是回文数。
    '''
    temp = abs(x)
    if x == 0:
        return True
    if temp%10 == 0:
        return False
    res = 0
    while(temp>0):
        res *=10
        i = temp % 10
        temp = temp /10
        res +=i
    return True if abs(x)==res else False


def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        编写一个函数来查找字符串数组中最长的公共前缀字符串。
        """
        if strs == []:
            return ""
        if strs.__len__() == 1:
            return strs[0]
        strs.sort()
        fir = strs[0]
        flag = True
        for i in range(0, fir.__len__(), 1):
            res = strs[0][0:fir.__len__()-i]
            for temp in strs:
                print(res, temp[0:fir.__len__()-i])
                if res != temp[0:fir.__len__()-i]:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                return res


def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        3个数相加等于0.
        For example, given array S = [-1, 0, 1, 2, -1, -4],
        A solution set is:
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]
        """
        res = []
        if nums.__len__() < 3:
            return res
        nums.sort()
        if nums[nums.__len__()-1]<0:
            return res
        for i in range(0, nums.__len__()-2, 1):
            if nums[i]>0:
                break
            if (i>1)and(nums[i] == nums[i-1]):
                continue
            k = i+1
            j = nums.__len__()-1
            while(k < j):
                target = nums[k]+nums[j]+nums[i]
                if target == 0:
                    ele = [nums[i], nums[k], nums[j]]
                    res.append(ele)

                    k += 1
                    j -= 1
                    while(k<j and nums[k] == nums[k-1]):
                        k +=1
                    while(k<j and nums[j] == nums[j+1]):
                        j -=1
                elif target < 0:
                    k += 1
                else:
                    j -= 1
        # res1 = []
        # for temp in res:
        #     if temp in res1:
        #         continue
        #     else:
        #         res1.append(temp)
        return res


def threeSum1(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        3个数相加等于0.
        For example, given array S = [-1, 0, 1, 2, -1, -4],
        A solution set is:
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]
        """
        left=0
        right = nums.__len__()
        res = []
        if right < 3:
            return res
        nums.sort()
        c = Counter(nums)
        ele = list(c.keys())
        ele.sort()
        new_nums = []
        for k in ele:
            ele_num = c[k]
            if k==0 and c[k]>=3:
                ele_num = 3
            if k!=0 and c[k]>=3:
                ele_num = 2
            for i in range(0, ele_num, 1):
                new_nums.append(k)

        while(True):
            r_flag = True
            l_flag = True
            len=new_nums.__len__()
            if new_nums[0] + new_nums[len-1] + new_nums[len-2] < 0:
                l_flag = False
                left +=1
            if new_nums[0] + new_nums[1] + new_nums[len-1] > 0:
                r_flag = False
                right -=1
            if (left >= right) or (len<=3) or (l_flag and r_flag):
                break
            new_nums = new_nums[left:right]
            left = 0
            right = new_nums.__len__()
        print(new_nums)
        for i,num1 in enumerate(new_nums):
            for j in range(i+1, new_nums.__len__(), 1):
                for k in range(j+1, new_nums.__len__(), 1):
                    if (num1+new_nums[j]+new_nums[k]==0):
                        temp = [num1,new_nums[j],new_nums[k]]
                        temp.sort()
                        if temp not in res:
                            res.append(temp)
        return res

def twoSum(nums, target):
    """
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


def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rty
    """
    nums.sort()
    if nums.__len__()<3:
        return
    for i in range(0, nums.__len__(), 1):
        pass


if __name__ == "__main__":
    l = [-1,0,1,2,-1,-4,-1]
    print(threeSum(l))


