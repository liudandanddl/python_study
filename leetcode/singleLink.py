#!/usr/bin/env python
# coding=utf-8

__author__ = 'ldd'
'''
python 单向链表
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def append_node(node, val):
    p = node  # p相当于一个指针，指向node
    if not p:
        node = Node(val)
    else:
        while True:
            if p.next:
                p = p.next
            else:
                p.next = Node(val)
                break
    return node


def get_len(node):  # 获取链表长度
    length = 0
    p = node
    while p:
        length += 1
        p = p.next
    return length


def print_node(node):  # 打印链表
    head = node
    val_list = []
    while head:
        val_list.append(head.val)
        head = head.next
    print(val_list)


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    去掉链表中的重复元素Given 1->1->2->3->3, return 1->2->3.
    """
    p = head
    while p:
        if p.next and p.next.val == p.val:
            p.next = p.next.next
        else:
            p = p.next
    return head


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    将两个有序列表合并到一起Input: 1->2->4, 1->3->4 Output: 1->1->2->3->4->4
    """
    if not l1:
        return l2
    if not l2:
        return l1
    res = Node(0)  # 返回值，新建个链表
    p = res  # 建立指针，用来操作链表res
    while l1 and l2:
        print(l1.val, l2.val, p.val)
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next
    if l1:
        p.next = l1
    if l2:
        p.next = l2
    return res.next  # 第一个元素是自己加进去的0


if __name__ == "__main__":
    # head = Node(1)
    # l = [1, 1, 2, 3, 3]
    # for temp in l:
    #     head = append_node(head, temp)
    # head = deleteDuplicates(head)
    # print_node(head)
    head1 = Node(1)
    head2 = Node(1)
    for temp in [2, 4]:
        head1 = append_node(head1, temp)
    for temp in [3, 4,5]:
        head2 = append_node(head2, temp)
    head = mergeTwoLists(head1, head2)
    print_node(head)