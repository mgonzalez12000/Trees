'''
A valid BST is defined as follows
- The left subtree of a node contains only nodes with keys less than the
nodes key.
- The right subtree of a node contains only nodes with keys greater than
the nodes key
- Both the left and right subtrees must also be binary search trees.
'''
# Definition of a binary tree node.
# class TreeNode(object):
#   def _init_(self, val = 0, left = None, right = None):
#       self.val = val
#       self.left = left
#       self.right = right
class Solution (object):
    def isValidVST(self, root):
        '''
        :type root: TreeNode
        :rtype: bool
        '''
        