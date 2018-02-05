#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def add_left(tree, val):
    temp = TreeNode(val)
    if tree.left is None:
        tree.left = temp
        return tree
    else:
        tree = tree.left
        add_left(tree, val)


def add_right(tree, val):
    temp = TreeNode(val)
    if tree.right is None:
        tree.right = temp
        return tree
    else:
        tree = tree.right
        add_right(tree, val)


def add_tree1(tree, val_list):
    for i, val in enumerate(val_list):
        if i % 2 == 1:
            add_left(tree, val)
        else:
            add_right(tree, val)
    return tree

def add_tree(tree, val_list):
    for i, val in enumerate(val_list):
        temp = TreeNode(val)
        if i % 2 == 1:
            while tree:
                if tree.left is None:
                    tree.left = temp
                    break
                else:
                    tree = tree.left
        else:
            while tree:
                if tree.right is None:
                    tree.right = temp
                    break
                else:
                    tree = tree.right
    return tree

def print_tree(tree, res):  # 前序遍历：根-左-右
    if tree:
        res.append(tree.val)
        print_tree(tree.left, res)
        print_tree(tree.right, res)
    return res


def isSameTree(p, q):  # 判断两棵树是否相同
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    print(p, q)
    if (p == None) and (q == None):
        return True
    elif (p == None) or (q == None):
        return False
    if p.val != q.val:
        return False
    if not isSameTree(p.left, q.left):
        return False
    else:
        return isSameTree(p.right, q.right)
    return True
    # if p == None and q == None:
    #         return True
    # elif p == None or q== None:
    #     return False
    # return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)



if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree2 = TreeNode(1)
    # tree.left = TreeNode(2)
    # print(tree.val, tree.left.val)
    b1 = add_tree1(tree1, [2])
    b2 = add_tree1(tree2, [2, 3])
    # print(print_tree(b1, []))  #  [1, 3, 5, 2, 4, 6]
    # print(print_tree(b2, []))
    print(isSameTree(b1, b2))

