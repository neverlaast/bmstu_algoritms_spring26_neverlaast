from collections import deque

def matrix_01(mat):
    
    m, n = len(mat), len(mat[0])
    dist = [[float('inf')] * n for _ in range(m)]
    q = deque()

    # поиск начальных клеток с 0 для bfs
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                q.append((i, j)) # клетки с 0 добавляем в очередь
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while q:
        
        a, b = q.popleft()
        for dir_a, dir_b in directions: # проходимся по соседям
            new_a, new_b = a + dir_a, b + dir_b
            
            if (0 <= new_a < m) and (0 <= new_b < n): # проверяем, что не вышли за границы
                if dist[new_a][new_b] > dist[a][b] + 1:
                    dist[new_a][new_b] = dist[a][b] + 1
                    q.append((new_a, new_b)) # новую ячейку кладем в очередь
    
    return dist

mat1 = [
  [0, 0, 0],
  [0, 1, 0],
  [1, 1, 1]
]

mat2 = [
  [1, 1, 0],
  [1, 1, 1],
  [1, 1, 1]
]

assert matrix_01(mat1) == [[0, 0, 0],
                           [0, 1, 0],
                           [1, 2, 1]]

assert matrix_01(mat2) == [[2, 1, 0],
                           [3, 2, 1],
                           [4, 3, 2]]
