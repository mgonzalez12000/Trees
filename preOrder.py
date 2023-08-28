'''
Keep in mind that preorder traversal for a BST is MIDDLE, LEFT, RIGHT
'''
class Solution(object):
    def preorderTraversal(self, root):
        pre_order = []
        def dfs(node):
            if node == None:
                return
            pre_order.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return pre_order