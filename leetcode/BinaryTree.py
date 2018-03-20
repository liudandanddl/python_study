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
    判断一棵树是否是镜像树：左子树和右子树的值相比较。
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
    if root is None:
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
def minDepth(root):
    """
    求二叉树的最小深度：分3种情况：（1）树为空，则为0；
    （2）根节点如果只存在左子树或者只存在右子树，则返回值应为左子树或者右子树的最小深度+1;
    （3）如果根节点的左子树和右子树都存在，则返回值为左右子树的最小深度的较小值+1.
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    if root.left is None and root.right is not None:
        return minDepth(root.right)+1
    if root.left is not None and root.right is None:
        return minDepth(root.left)+1
    return min(minDepth(root.right), minDepth(root.left))+1

def isBalanced(root):
    """
    判断一个树是否是平衡二叉树
    平衡二叉树：是二叉树的任意节点的两颗子树之间的高度差小于等于1.
    递归求解每个节点的左右子树的高度差，如果有大于1的，则return FALSE，如果高度差小于等于1，在继续递归求解。
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True
    if abs(maxDepth(root.left)-maxDepth(root.right)) <= 1:
        return isBalanced(root.left) and isBalanced(root.right)
    else:
        return False
'''
二叉树如下：
       D
   B        E
A    C   NULL  G
              F  NULL
'''
def hasPathSum(root, sum):  # 深度优先遍历
    """
    给定一个二叉树和一个总和，确定树是否有根到叶路径的所有值等于给定的和。
    root-to-leaf路径，必须是从根节点一直到叶子节点，中间取一段是不行的
    节点值是可以为负的。
    空的二叉树，不存在和为0的路径。
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if root is None:
        return False
    else:
        if sum == root.val and root.left is None and root.right is None:
            return True
        else:
            return hasPathSum(root.left, sum-root.val) or hasPathSum(root.right, sum-root.val)


def mergeTrees(t1, t2):
    """
    合并两个二叉树，将相关节点值相加。
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if t1 is None and t2 is None:
        return
    elif t1 is None:
        return t2
    elif t2 is None:
        return t1
    else:
        t1.val+=t2.val
    t1.right = mergeTrees(t1.right, t2.right)
    t1.left = mergeTrees(t1.left, t2.left)
    return t1


if __name__ == "__main__":
    # l = ['D', 'B', 'E', 'A', 'C', None, 'G', None,None,None,None,None,None,'F']
    # root = add_tree(l)
    root = TreeNode('D',TreeNode('B',TreeNode('A'),TreeNode('C')),TreeNode('E',right=TreeNode('G',left=TreeNode('F'))))
    print('先根遍历：res=DBACEGF')
    # print(beforeTree(root))
    # print('中根遍历：res=ABCDEFG')
    # midTree(root)
    # print('后根遍历：res=ACBFGED')
    # afterTree(root)

    # print('广度优先遍历：res=DBEACGF')
    # print(levelTree(root))  # ['D', 'B', 'E', 'A', 'C', 'G', 'F']
    # print(levelOrderBottom(root))  # [['D'], ['B', 'E'], ['A', 'C', 'G'], ['F']]
    print(hasPathSum(root, 22))
