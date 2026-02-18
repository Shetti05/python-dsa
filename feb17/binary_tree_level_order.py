from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)
    return result

# Example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
print(level_order(root))
