class Solution(object):
    def inorderTraversal(self, root):
        inorder = []
        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)
        dfs(root)
        return inorder