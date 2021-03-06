# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        '''
        # BFS

        if not root:
            return root
        queue = [root]
        while queue:
            for i in range(len(queue)-1):
                queue[i].next = queue[i+1]
            #queue[-1].next = None #b/c default value is already None
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        '''

        # DFS
        # more intuitive, but need to consider more

        while root and root.left:
            temp = root.left
            while root:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
                root = root.next
            root = temp