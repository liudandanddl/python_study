#!/usr/bin/env python
# coding=utf-8
from Queue import Queue

__author__ = 'ldd'


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
    #
    # def __init__(self, x):
    #     self.val = x
    #     self.left = None
    #     self.right = None

def add_tree(val_list):
    if not val_list:
        return None
    tree = TreeNode(None)
    queue = Queue()
    queue.put(tree)
    for temp in val_list:
        node = queue.get()
        node.val = temp
        node.left = TreeNode(None)
        node.right = TreeNode(None)
        queue.put(node.left)
        queue.put(node.right)
    return tree



def beforeTree(root):  # 先跟遍历
    res = []
    if root is None:
        return
    res.append(root.val)
    # res.append(beforeTree(root.left))
    # res.append(beforeTree(root.right))
    if beforeTree(root.left):
        res.append(beforeTree(root.left))
    if beforeTree(root.right):
        res.append(beforeTree(root.right))
    return res


def midTree(root):  # 中跟遍历
    if root is None:
        return
    midTree(root.left)
    print(root.val)
    midTree(root.right)


def afterTree(root):  # 后根遍历
    if root is None:
        return
    afterTree(root.left)
    afterTree(root.right)
    print(root.val)


def levelTree(root):  # 广度优先遍历/层次遍历 ['D', 'B', 'E', 'A', 'C', 'G', 'F']
    if root is None:
        return None
    res = []
    queue = Queue()  # 先进先出队列
    queue.put(root)  # 首先把根节点放入队列
    while not queue.empty():  # 只要队列不为空，则遍历节点，并分别把左右子节点放入队列
        node = queue.get()
        res.append(node.val)
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)
    return res

def levelOrderBottom(root):
    '''
    广度优先遍历二叉树，返回结果中，明确区分每层的节点。[['D'], ['B', 'E'], ['A', 'C', 'G'], ['F']]
    '''
    if root is None:
        return None
    l = [root]
    res = []
    while l:
        temp_res = []  # 保留每层节点
        for i in range(0, len(l)):
            temp = l.pop(0)
            temp_res.append(temp.val)
            if temp.left:
                l.append(temp.left)
            if temp.right:
                l.append(temp.right)
        res.append(temp_res)
    return res

def isSymmetricSub(self, p, q):
    '''
    1.停止条件是 left==None & right==None
    2. left.val==right.val 比较left.left right.right & left.right right.left
    '''
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    return (p.val == q.val) and self.isS(p.left, q.right) and self.isS(p.right, q.left)
def isSymmetric(root):
    """
    判断一棵树是否是镜像树
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True
    return isSymmetricSub(root.left, root.right)


def isSameTree(p, q):  # 判断两棵树是否相同
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
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


def maxDepth(root):
    """
    求一棵树的深度:深度优先算法，递归求解
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return 0
    depth_l = maxDepth(root.left) + 1
    depth_r = maxDepth(root.right) + 1
    return max(depth_l, depth_r)
def maxDepth2(root):
    # 求一棵树的深度：广度优先算法
    if root is None:
        return 0
    depth = 0
    q = [root]  # 只保留当前一层的子节点
    while len(q) != 0:
        depth += 1
        for i in range(0, len(q)):  # 将list中上一层的子节点都弹出，list中保留的是当前的子节点。
            temp = q.pop(0)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
    return depth
'''
二叉树如下：
       D
   B        E
A    C   NULL  G
              F  NULL
'''


if __name__ == "__main__":
    # l = ['D', 'B', 'E', 'A', 'C', None, 'G', None,None,None,None,None,None,'F']
    # root = add_tree(l)
    root = TreeNode('D',TreeNode('B',TreeNode('A'),TreeNode('C')),TreeNode('E',right=TreeNode('G',left=TreeNode('F'))))
    # print('先根遍历：res=DBACEGF')
    # print(beforeTree(root))
    # print('中根遍历：res=ABCDEFG')
    # midTree(root)
    # print('后根遍历：res=ACBFGED')
    # afterTree(root)

    print('广度优先遍历：res=DBEACGF')
    print(levelTree(root))  # ['D', 'B', 'E', 'A', 'C', 'G', 'F']
    # print(levelOrderBottom(root))  # [['D'], ['B', 'E'], ['A', 'C', 'G'], ['F']]

