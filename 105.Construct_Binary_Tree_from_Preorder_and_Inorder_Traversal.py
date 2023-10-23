class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None

        root_val = preorder[0]
        root = TreeNode(val=root_val)

        inorder_root_index = inorder.index(root_val)

        # divide into left and right subarrays
        inorder_left = inorder[:inorder_root_index]
        inorder_right = inorder[inorder_root_index+1:]

        preorder_left = preorder[1:1+inorder_root_index]  # Using inorder_root_index directly to slice preorder
        preorder_right = preorder[1+inorder_root_index:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root
