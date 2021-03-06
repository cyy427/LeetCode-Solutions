# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive_Iterative(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ans, stack = 0, [(root, 1)]
        while stack:
            node, length = stack.pop()
            ans = max(ans, length)
            for child in [node.left, node.right]:
                if child:
                    l = length + 1 if child.val == node.val +1 else 1
                    stack.append((child, l))
        return ans
    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.helper(root, root.val - 1, 0)

    def helper(self, root, pre, cur_length):
        if not root:
            return cur_length
        if root.val - pre == 1:
            cur_length += 1
        else:
            cur_length = 1
        return max(max(cur_length, self.helper(root.left, root.val, cur_length)), self.helper(root.right, root.val, cur_length))

