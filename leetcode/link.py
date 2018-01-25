#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def getVal(self):
        return self.val
    def getNext(self):
        return self.next
    def setVal(self, newVal):
        self.val = newVal
    def setNext(self, newNext):
        self.next = newNext
    def __repr__(self):
        '''
        用来定义Node的字符输出，
        print为输出data
        '''
        return str(self.val)

class ListNode():
    def __init__(self):
        self.head = None  # 初始化列表为空
        self.size = 0

    def isEmpty(self):  # 检测列表是否为空
         return self.head == None

    def add(self, item):   # 在链表前端添加元素
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp

    def append(self, item):
        temp=Node(item)
        if self.isEmpty():
            self.head=temp  # 若为空表，将添加的元素设为第一个元素
        else:
            current = self.head
            while current.getNext() != None:
                current=current.getNext() # 遍历链表
            current.setNext(temp)  # 此时current为链表最后的元素

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    cur1 = l1.head
    cur2 = l2.head
    res = ListNode()
    while ((cur1 != None) or (cur2 != None)):
        if cur1 == None:
            res.add(cur2.val)
            cur2 = cur2.getNext()
            continue
        if cur2 == None:
            res.add(cur1.val)
            cur1 = cur1.getNext()
            continue
        if cur1.val > cur2.val:
            res.add(cur1.val)
            cur1 = cur1.getNext()
        else:
            res.add(cur2.val)
            cur2 = cur2.getNext()
    return res

if __name__ == "__main__":
    #     l1='(2 -> 4 -> 3) +
    #     l2=(5 -> 6 -> 4)
    #     Output: 7 -> 0 -> 8
    #  Explanation: 342 + 465 = 807.
    s1 = ListNode()
    s2 = ListNode()
    s1.add(1)
    s1.add(2)
    s1.add(4)
    # cur = s1.head
    # while cur != None:
    #     print(cur.val, type(cur.val))
    #     cur = cur.getNext()
    s2.add(1)
    s2.add(3)
    s2.add(4)
    # cur = s2.head
    print('-----------------------')
    l = mergeTwoLists(s1, s2)
    print(l, type(l))
    curt = l.head
    while curt != None:
        print(curt.val)
        curt = curt.getNext()




