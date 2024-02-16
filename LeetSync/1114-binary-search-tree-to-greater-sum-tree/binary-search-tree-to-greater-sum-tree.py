class Solution:
    def dfs(self, node):
        # print(f"input: {node}, accumulation = {self.accum}")
        # if node:
        if not node: return
        
        self.dfs(node.right)
        
        self.accum += node.val
        node.val = self.accum
        
        self.dfs(node.left)
            
    def bstToGst(self, root):
        self.accum = 0
        self.dfs(root)

        return root