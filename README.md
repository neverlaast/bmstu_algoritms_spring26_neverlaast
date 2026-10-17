# Algorithms & Data Structures: VK Education

My solutions to algorithmic problems from the Algorithms and Data Structures course at VK Education (Technopark, Bauman Moscow State Technical University).
Every solution is written in Python and analyzed for time and space complexity.

| # | Topic | Problem | Approach | Time | Space |
|---|-------|---------|----------|------|-------|
| [01/1](01/Task1.py) | Linked lists | Intersection of two linked lists | Two pointers that switch heads | O(n + m) | O(1) |
| [01/2](01/Task2.py) | Stack | Sort a stack using one extra stack | Insertion via a temporary stack | O(n²) | O(n) |
| [02/1](02/Task1.py) | Strings, hashing | Longest substring without repeating characters | Sliding window + hash map of last positions | O(n) | O(σ) |
| [02/2](02/Task2.py) | Binary search | k-th smallest element in a sorted matrix | Binary search on values + staircase counting | O(n · log(max − min)) | O(1) |
| [03/1](03/Task1.py) | Trees, BFS | Binary tree level order traversal | BFS with a queue (`deque`) | O(n) | O(w) |
| [03/2](03/Task2.py) | Heap | k-th largest element in an array | Min-heap of size k (`heapq`) | O(n log k) | O(k) |
| [04/1](04/Task1.py) | Dynamic programming | Longest increasing subsequence | DP over prefixes | O(n²) | O(n) |
| [04/2](04/Task2.py) | Graphs, BFS | Distance to the nearest 0 in a binary matrix | Multi-source BFS | O(m · n) | O(m · n) |

σ is the alphabet size and w is the maximum width of the tree.

## Topics covered
Linked lists · stacks and queues · two pointers · sliding window · hash maps · binary search · trees · BFS · heaps · dynamic programming · graphs on grids
