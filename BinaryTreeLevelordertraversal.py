# TC : O(n); n is no.of nodes in tree
# SC : O(n); n is no.of nodes in tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if(root==None):
            return res
        
        q = deque()
        q.append(root)
        
        currLevel = []
        size = len(q) #because we added root to queue already
        
        while(q):
            node = q.popleft()
            currLevel.append(node.val)
            
            if(node.left!=None): q.append(node.left)
            if(node.right!=None): q.append(node.right)
            
            size -= 1
            
            if size == 0:
                res.append(currLevel)
                currLevel = []
                size = len(q)
        
        return res
