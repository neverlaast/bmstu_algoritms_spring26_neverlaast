from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs_level(root):
    
    if not root:
        return []
    
    res = []
    queue = deque([root])
    
    while queue:

        #размер очереди на текущем уровне и список для текущего уровня
        level_len = len(queue)
        level_current = []

        #цикл по текущему уровню
        for i in range(level_len):
            node = queue.popleft()
            level_current.append(node.val)

            #добавляем потомков в очередь
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        #добавляем список в результирующий список
        res.append(level_current)
    
    return res
