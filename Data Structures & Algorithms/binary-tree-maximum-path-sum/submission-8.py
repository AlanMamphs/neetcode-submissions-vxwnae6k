class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, float('-inf')
            
            left_max, l_res = dfs(node.left)
            right_max, r_res = dfs(node.right)
            
            # Max path that extends from this node to one child
            max_through_node = node.val + max(left_max, right_max, 0)
            
            # Max path that bends at this node (uses both children)
            max_bent_at_node = node.val + max(left_max, 0) + max(right_max, 0)
            
            # Global max in this subtree
            global_max = max(l_res, r_res, max_through_node, max_bent_at_node)
            
            return max_through_node, global_max
        
        return dfs(root)[1]