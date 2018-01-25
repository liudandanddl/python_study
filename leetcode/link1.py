#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'

class ListNode(object):
    def __init__(self, item):
        self.val = item
        self.next = None  # 初始化列表为空
        self.head = None  # 初始化列表为空
    def getVal(self):
        return self.val
    def getNext(self):
        return self.next
    def setVal(self, newVal):
        self.val = newVal
    def setNext(self, newNext):
        self.next = newNext
    def add(self, item):
        temp = ListNode(item)
        temp.setNext(self.head)
        self.head = temp
    def isEmpty(self):  # 检测列表是否为空
        return self.head == None


if __name__ == "__main__":
    s1 = ListNode(1)
    print(s1.val, s1.head, s1.next)
    s1.add(ListNode(2))
    print(s1.val, s1.head, s1.next)
    # s1.add(2)
    # s1.add(4)
    cur = s1.head
    while cur != None:
        print(cur.val, type(cur.val), cur)
        cur = cur.getNext()
    # s2.add(1)
    # s2.add(3)
    # s2.add(4)
    # # cur = s2.head
    # print('-----------------------')
    # l = mergeTwoLists(s1, s2)
    # print(l, type(l))
    # curt = l.head
    # while curt != None:
    #     print(curt.val)
    #     curt = curt.getNext()




