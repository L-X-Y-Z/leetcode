# -*- coding: utf-8 -*-

import collections
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorder(self, root):
        order = []
        if not root:
            return order
        stack = collections.deque()
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                order.append(node)
                continue
            order.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return order

    def postorder(self, root):
        order = []
        if not root:
            return order
        stack = collections.deque()
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                order.insert(0, node)
                continue
            order.insert(0, node.val)
            stack.append(node.left)
            stack.append(node.right)
        return order

    def clone_symmetric_tree(self, root) -> TreeNode:
        if not root:
            return None
        current_t = TreeNode(root.val)
        current_t.left = self.clone_tree(root.right)
        current_t.right = self.clone_tree(root.left)
        return current_t

    def isEqual(self, root_a, root_b):
        if not root_a and not root_b:
            return True
        if root_a and root_b:
            if root_a.val != root_b.val:
                return False
            else:
                return self.isEqual(root_a.left, root_b.left) and self.isEqual(root_a.right, root_b.right);
        else:
            return False

    def isSymmetric_by_clone(self, root: TreeNode) -> bool:
        if not root: return True;
        clone_tree = self.clone_symmetric_tree(root)
        return self.isEqual(root, clone_tree)
    def isSymmetric_by_order(self, root: TreeNode) -> bool:
        if not root: return True;
        list_preorder = self.preorder(root.left)
        print(list_preorder)
        list_postorder = self.postorder(root.right)
        print(list_postorder)
        list_postorder.reverse()
        return list_preorder == list_postorder
    def isSymmetric_two(self, left, right):
        if not left and not right: return True
        if not left or not right: return False
        if left.val != right.val:
            return False
        return self.isSymmetric_two(left.left, right.right) and self.isSymmetric_two(left.right, right.left)
    def isSymmetric_by_recursion(self, root:TreeNode) -> bool:
        if not root: return True
        return self.isSymmetric_two(root.left, root.right)
    def isSymmetric(self, root:TreeNode) -> bool:
        if not root:
            return True
        left_queue = collections.deque()
        left_queue.append(root)
        right_queue = collections.deque()
        right_queue.append(root)
        while left_queue and right_queue:
            left_node = left_queue.pop()
            right_node = right_queue.pop()
            if not left_node and not right_node:
                continue
            if not left_node or not right_node:
                return False
            if left_node.val != right_node.val:
                return False
            left_queue.append(left_node.left)
            left_queue.append(left_node.right)
            right_queue.append(right_node.right)
            right_queue.append(right_node.left)
        return not left_node and not right_node


def construct_tree(list_val):
    list_node = []
    for i in range(len(list_val)):
        val = list_val[i]
        if not val:
            continue;
        node_cur = TreeNode(val)
        list_node.append(node_cur)
        if i > 0:
            if i % 2 == 0:
                list_node[i // 2 - 1].right = node_cur
            else:
                list_node[i // 2].left = node_cur
    return list_node[0]


if __name__ == '__main__':
    list_val = [1,2,2,3,4,4,3]
    # list_val = [1,2,2,None,3,None,3]
    tree_root = construct_tree(list_val)

    sol = Solution()
    is_symmetric = sol.isSymmetric(tree_root)
    print(is_symmetric)
