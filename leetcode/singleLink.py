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


def deleteNode(node):
    """
    删除node节点
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next


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


def removeElements(head, val):
    """
    从列表中删除给定的元素
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    Example
    Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
    Return: 1 --> 2 --> 3 --> 4 --> 5
    """
    p = head
    while p:
        if p.next and p.next.val == val:
            p.next = p.next.next
        else:
            p = p.next
    q = head
    q1 = head
    if q and q.val == val:  # 判断列表的头元素
        q = q1.next
    return q


def reverseList(head):
    """
    反转链表
    :type head: Node
    :rtype: Node
    """
    if not head:
        return head
    val_list = []
    p = head
    while p:
        val_list.append(p.val)
        p = p.next
    val_list.reverse()
    resNode = Node(val_list[0])
    q = resNode
    for val in val_list[1:]:
        temp = Node(val)
        q.next = temp
        q = q.next
    return resNode


def reverseList2(head):
    """
    反转链表,直接在原链表上操作,通过迭代将节点重组，前面的节点转移到重组链表的后面。实际上就是头结点倒插操作。
    :type head: Node
    :rtype: Node
    """
    resNode = None
    while head:
        q = head
        head = head.next
        q.next = resNode
        resNode = q
    return resNode


def isPalindrome(head):
    """
    判断一个单向链表是不是回文串。时间负责度O(n) ，空间O(1)
    :type head: ListNode
    :rtype: bool
    """
    if not head or not head.next:
        return True
    # 查找单向列表的中间节点,mid指向单向链表的中间节点
    mid = q = head
    while q.next and q.next.next:
        mid = mid.next
        q = q.next.next
    mid = mid.next  # mid指向链表的后半段
    # 将mid所指向的后半段的单向链表原地反转
    mid_rever = None
    while mid:
        p = mid
        mid = mid.next
        p.next = mid_rever
        mid_rever = p
    # 将head的前半段(减去mid的)和mid_rever比较
    while mid_rever:
        if mid_rever.val != head.val:
            return False
        else:
            mid_rever = mid_rever.next
            head = head.next
    return True



if __name__ == "__main__":
    # head = Node(1)
    # l = [1, 1, 2, 3, 3]
    # for temp in l:
    #     head = append_node(head, temp)
    # head = deleteDuplicates(head)
    # print_node(head)

    # head1 = Node(1)
    # head2 = Node(1)
    # for temp in [2, 4]:
    #     head1 = append_node(head1, temp)
    # for temp in [3, 4,5]:
    #     head2 = append_node(head2, temp)
    # head = mergeTwoLists(head1, head2)
    # print_node(head)
    head1 = Node(6)
    for temp in [2,1,4]:
        head1 = append_node(head1, temp)
    head = reverseList2(head1)
    print_node(head)