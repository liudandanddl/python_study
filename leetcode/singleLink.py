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


def hasCycle(head):
    """
    判断链表是否有循环,如果有循环，返回循环开始处，没有返回None。
    如果有循环，一定在链表的中间有两个节点相等。
    使用一个慢指针，一个快指针，如果链表成环，则慢指针一定会被快指针追上。如果不成环，则快指针会先走到None节点退出循环。
    当两个指针相遇的时候，快指针可能在环内已经走了n圈，我们设相遇点为c，此时fp和sp都指向了c，接下来令fp继续指向c结点，sp指向链表头结点head，
    此时最大的不同是fp的步数变成为每次走一步，令fp和sp同时走，每次一步，那么它们再次相遇的时候即为环的入口结点
    :type head: ListNode
    :rtype: bool
    """
    fast = head
    slow = head
    while fast is not None and slow is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:  # 条件成立，则表示链表有循环
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return


def getIntersectionNode(headA, headB):
    """
    查找两个单链表交集的起始点.eg:
    headA=a1->a2->c1->c2->c3
    headB=b1->b2->b3->c1->c3->c3  则应该返回c1
    解法：A链表走完走B的；B链表走完走A的。
    a1->a2->c1->c2->c3->b1->b2->b3->c1->c3->c3
    b1->b2->b3->c1->c3->c3->a1->a2->c1->c2->c3
    这样A和B两个链表长度相同，如果走完之后都等于None，则两个链表没有交集，否则在交集出比相等
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    a = headA
    b = headB
    while a and b:  # 两个链表都走完了，没有相等的节点，最后返回None
        if a == b:
            return a
        a = a.next
        b = b.next
        if not a and b:  # A链表走完，但B链表没走完，则接着走B的
            a = headB
        if not b and a:  # B链表走完，单A链表没走完，则接着走A的
            b = headA
    return


def rotateRight(head, k):
    '''
    给定一个列表，将列表旋转到右边的k个位置，其中k是非负的
    Given 1->2->3->4->5->NULL and k = 2,
    return 4->5->1->2->3->NULL.
    解法：将链表形成一个环，在适当的位置断开连接。head指向结果链表的头部，p指向尾部。
    '''
    if head is None:
        return None
    if k == 0:
        return head
    p = head  # 用指针p来操作链表
    length = 1
    while p.next:  # 得到list的长度
        length += 1
        p = p.next
    # 循环结束后，p指向链表的最后一个节点
    p.next = head  # 形成一个环
    step = length-(k % length)  # k的数值可能大于链表长度
    while step > 0:   # 到新head的位置
        step -= 1
        p = p.next
    # 循环结束后，p指向返回值的尾部节点，即p.val=3
    head = p.next   # 将head指向返回值的头部节点
    p.next = None   # 断开环链表。
    return head


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
    head1 = Node(1)
    for temp in [2,3,4,5]:
        head1 = append_node(head1, temp)
    head = rotateRight(head1, 2)
    print_node(head)