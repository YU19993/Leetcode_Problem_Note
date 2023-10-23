class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            # Calculate maximum path sums for left and right children
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # Update the global maximum sum
            max_sum = max(max_sum, node.val + left_gain + right_gain)
            
            # Return the maximum path sum for the current node
            return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        dfs(root)
        return max_sum

# Test cases for validation
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
assert Solution().maxPathSum(root1) == 6

root2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert Solution().maxPathSum(root2) == 42
