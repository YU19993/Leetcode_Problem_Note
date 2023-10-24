class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def levelOrder(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    result, queue = [], deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for i in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

# Test cases for validation
root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert levelOrder(root1) == [[3],[9,20],[15,7]]

root2 = TreeNode(1)
assert levelOrder(root2) == [[1]]

assert levelOrder(None) == []
