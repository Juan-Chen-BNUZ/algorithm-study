# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
题目描述
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
"""


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):

        def dfs(root):
            if not root:
                return ListAll
            list.append(root.val)
            if sum(list) == expectNumber and not root.left and not root.right:
                ListAll.append(list[:])
            else:
                dfs(root.left)
                dfs(root.right)
            list.pop()

        ListAll = []
        list = []
        dfs(root)
        return ListAll
    # write code here
