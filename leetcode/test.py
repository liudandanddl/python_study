#!/usr/bin/env python
# coding=utf-8
import Queue

__author__ = 'ldd'


def trailingZeroes(n):
    """
    求阶乘结果尾部0的个数.0是由2*5所得，计算能被多少个5，25，125.。。。。整除
    :type n: int
    :rtype: int
    """
    return 0 if n==0 else n/5 +trailingZeroes(n/5)


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


def threeSum(nums):
    '''
    先升序排序，然后用第一重for循环确定第一个数字。然后在第二重循环里，第二、第三个数字分别从两端往中间扫。时间复杂度：O(n2)
    如果三个数的sum等于0，得到一组解。如果三个数的sum小于0，说明需要增大，所以第二个数往右移。如果三个数的sum大于0，说明需要减小，所以第三个数往左移。
    :type nums: List[int]
    :rtype: List[List[int]]
    '''
    res = []
    length = len(nums)
    if length < 3:
        return res
    nums.sort()
    for i in range(length):
        if nums[i] > 0:  # 第一个数大于0
            break
        if i > 0 and nums[i] == nums[i-1]:  # 重复元素不重复计算
            continue
        begin = i+1
        end = length-1
        while begin < end:
            sum = nums[i]+nums[begin]+nums[end]
            if sum == 0:
                tmp = [nums[i], nums[begin], nums[end]]
                res.append(tmp)
                begin += 1
                end -= 1
                while begin < end and nums[begin] == nums[begin-1]:
                    begin += 1
                while begin < end and nums[end] == nums[end+1]:
                    end -= 1
            elif sum > 0:
                end -= 1
            else:
                begin += 1
    return res


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
    动态规划问题
    求数组的最大子串和。常规办法：for循环两边，第一遍遍历子串头，在内部遍历子串尾，算出所有子串和。
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
        if max_end < 0:  # 累加失败，重新开始
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


def mySqrt(x):
    '''
    用二分法求一个数的最近平方根
    对于一个非负数n，它的平方根不会大于n/2+1
    eg：4 res=2 ;  8 res=2 ; 9 res=3 ; 15 res=3 ; 16 res=4
    '''
    left = 1
    right = x/2+1
    if x in [0, 1]:
        return x
    while left < right-1:  # 比如输入35， 最后一次left=5 right=7 mid=6 经过while更改值之后left=6 right=7,不需要在while了，res肯定6或7
        mid = (left + right)/2
        print(left, right, mid)
        if mid == x / mid:
            return int(mid)
        if mid > x / mid:
            right = mid
        else:
            left = mid
    res = right if right*right<x else right-1
    return res


def countPrimes(n):
    """
    计算比n小的素数的个数
    :type n: int
    :rtype: int
    厄拉多塞筛法：先将 2~n 的各个数放入表中，然后在2的上面画一个圆圈，然后划去2的其他倍数；
    第一个既未画圈又没有被划去的数是3，将它画圈，再划去3的其他倍数；
    现在既未画圈又没有被划去的第一个数 是5，将它画圈，并划去5的其他倍数……
    依次类推，一直到所有小于或等于 n 的各数都画了圈或划去为止。这时，表中画了圈的以及未划去的那些数正好就是小于 n 的素数。
    当你要画圈的素数的平方大于 n 时，那么后面没有划去的数都是素数，就不用继续判了
    """
    # if n < 2:
    #     return 0
    # ditA = dict.fromkeys(range(2, n, 1), True)  # 默认都是素数
    # for key in range(2, int((n-1)**0.5)+1, 1):
    #     if ditA[key]:
    #         for i in range(2*key-1, n, 1):
    #             if i % key == 0:
    #                 ditA[i] = False
    # return sum(ditA.values())
    # 上面算法效率较低

    if n < 3:
        return 0
    primes = [True]*n  # 默认所有小于n的都是素数
    primes[:2] = [False, False]  # primes[0],primes[1]就是数字0和1，都不是素数
    for base in xrange(2, int((n-1)**0.5)+1):  # 当你要画圈的素数的平方大于 n 时，那么后面没有划去的数都是素数，就不用继续判了
        if primes[base]:
            primes[pow(base, 2)::base] = [False] * len(primes[pow(base, 2)::base])  # base的倍数都不是素数.巧用分片赋值操作。
    return sum(primes)  # 素数是True，是1，非素数是0，求和即可


def isUgly(num):
    """
    判断一个数能否被2、3、5整除
    :type num: int
    :rtype: bool
    """
    if num <=0:
        return False
    if num == 1:
        return True
    if num % 2 == 0:
        return isUgly(num/2)
    if num % 3 == 0:
        return isUgly(num/3)
    if num % 5 == 0:
        return isUgly(num/5)
    return False


def moveZeroes(nums):
    """
    将数组的所有0移到后面。必须在不复制数组的情况下完成此操作。最小化操作总数
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0]
    """
    a = len(nums)
    for i in range(0, a, 1):
        temp = nums[i]
        if temp == 0:
            nums.append(0)
            nums.remove(temp)  # 移除列表中某个值的第一个匹配项，修改列表无返回值。


def removeDuplicates(nums):
    """
    不增加额外空间，原地删除一个有序数组的重复元素，返回新数组的个数。
    Given nums = [1,1,2]，return length = 2, with the first two elements of nums being 1 and 2 respectively。
    It doesn't matter what you leave beyond the new length.
    :type nums: List[int]
    :rtype: int
    """
    if nums == []:
        return 0
    j = 0
    for i in range(1, len(nums), 1):
        if nums[j] != nums[i]:
            nums[j+1] = nums[i]
            j = j+1
    # for i in nums[j+1:]:
    #     nums.remove(i)    多余的重复元素在原地删除
    print(nums)
    return j+1


def isToeplitzMatrix(matrix):
    '''
    从左上角到右下角的每个对角线上的元素是否相等
    对角线遍历，注意对角线的性质：当前元素为matrix[i][j],下一元素为matrix[i+1][j+1]
    Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    Output: True
    Explanation:
    1234
    5123
    9512
    In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]",
    and in each diagonal all elements are the same, so the answer is True.
    '''
    n = len(matrix)
    m = len(matrix[0])
    for i in range(0, n-1, 1):
        for j in range(0, m-1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
    return True


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    原地反转一个数组，For example, k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]
    """
    nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]


def getSum(a, b):
    """
    位操作计算整数加法
    :type a: int
    :type b: int
    :rtype: int
    既然不能使用加法和减法，那么就用位操作。下面以计算5+4的例子说明如何用位操作实现加法：
    1. 用二进制表示两个加数，a=5=0101，b=4=0100；
    2. 用and（&）操作得到所有位上的进位carry=0100;
    3. 用xor（^）操作找到a和b不同的位，赋值给a，a=0001；
    4. 将进位carry左移一位，赋值给b，b=1000；
    5. 循环直到进位carry为0，此时得到a=1001，即最后的sum。
    因为Python的整数不是固定的32位，所以需要做一些特殊的处理。代码里的将一个数对0x100000000取模（注意：Python的取模运算结果恒为非负数），
    是希望该数的二进制表示从第32位开始到更高的位都同是0（最低位是第0位），以在0-31位上模拟一个32位的int。
    """
    while b != 0:
        carry = a & b
        a = (a ^ b) % 0x100000000
        b = (carry << 1) % 0x100000000
    return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)


if __name__ == "__main__":
    # [4,-1,2,1] has the largest sum = 6.
    # [-2,1,-3,4,-1,2,1,-5,4] 187
    # [59, 26, -53, 58, 97, -93, -23, 84]
    # print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(countPrimes(120))  # 30





