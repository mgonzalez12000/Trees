'''
Keep in mind that postorder traversal for a BST is: left, right, middle
'''
class Solution(object):
    def postorderTraversal(self, root):
        postorder = []
        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            dfs(node.right)
            postorder.append(node.val)
        dfs(root)
        return postorder