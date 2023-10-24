class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        def dfs(node):
            if not node:
                return "null,"
            return str(node.val) + "," + dfs(node.left) + dfs(node.right)
        return dfs(root)
        
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        values = iter(data.split(','))
        def dfs():
            val = next(values)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

# Test cases for validation
codec = Codec()
root1 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
serialized_data = codec.serialize(root1)
assert codec.deserialize(serialized_data).val == 1
