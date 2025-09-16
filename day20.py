"""
Day 20: Advanced DSA Problems (with docstrings + inline comments + complexities)

Problems included:
1. Binary Tree Level Order Traversal (BFS)
2. Lowest Common Ancestor (LCA in Binary Tree)
3. Detect Cycle in Directed Graph (DFS)
4. Topological Sort (Kahn’s Algorithm)
5. Dijkstra’s Algorithm (Shortest Path in Graph)
6. Kth Largest Element in an Array (Heap / Quickselect)
7. Median of Two Sorted Arrays (Binary Search Partition)
8. Sliding Window Maximum (Deque)
"""

from typing import List, Optional
import heapq
from collections import deque, defaultdict


# Definition for binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1) Binary Tree Level Order Traversal (BFS) - O(n), O(n) space
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Traverse binary tree level by level using BFS.
    """
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res


# 2) Lowest Common Ancestor (Binary Tree) - O(n), O(h) recursion stack
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Recursively find the lowest common ancestor of nodes p and q.
    """
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if left and right else left or right


# 3) Detect Cycle in Directed Graph (DFS) - O(V+E), O(V) stack space
def has_cycle_directed(n: int, edges: List[List[int]]) -> bool:
    """
    Detect cycle in directed graph using DFS and recursion stack.
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited, rec_stack = [0] * n, [0] * n  # 0 = unvisited, 1 = visiting, 2 = visited

    def dfs(u):
        visited[u] = 1
        rec_stack[u] = 1
        for v in graph[u]:
            if not visited[v] and dfs(v):
                return True
            elif rec_stack[v]:
                return True
        rec_stack[u] = 0
        return False

    return any(dfs(u) for u in range(n) if not visited[u])


# 4) Topological Sort (Kahn’s Algorithm) - O(V+E), O(V) space
def topo_sort(n: int, edges: List[List[int]]) -> List[int]:
    """
    Perform topological sorting using BFS (Kahn’s Algorithm).
    """
    graph = defaultdict(list)
    indegree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    q = deque([i for i in range(n) if indegree[i] == 0])
    res = []
    while q:
        u = q.popleft()
        res.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    return res if len(res) == n else []  # if not all nodes processed -> cycle


# 5) Dijkstra’s Algorithm (Shortest Path) - O((V+E) log V), O(V+E)
def dijkstra(n: int, edges: List[List[int]], src: int) -> List[int]:
    """
    Compute shortest paths from src to all nodes using Dijkstra’s algorithm.
    Graph is weighted and non-negative.
    """
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))

    dist = [float('inf')] * n
    dist[src] = 0
    pq = [(0, src)]  # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist


# 6) Kth Largest Element in Array (Heap) - O(n log k), O(k)
def kth_largest(nums: List[int], k: int) -> int:
    """
    Find kth largest element using min-heap of size k.
    """
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


# 7) Median of Two Sorted Arrays (Binary Search Partition) - O(log(min(n,m))), O(1)
def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Find median of two sorted arrays using binary search on partitions.
    """
    if len(nums1) > len(nums2):  # ensure nums1 is smaller
        nums1, nums2 = nums2, nums1
    n1, n2 = len(nums1), len(nums2)
    total = n1 + n2
    half = total // 2

    l, r = 0, n1
    while True:
        i = (l + r) // 2  # partition index nums1
        j = half - i      # partition index nums2

        left1 = nums1[i - 1] if i > 0 else float('-inf')
        right1 = nums1[i] if i < n1 else float('inf')
        left2 = nums2[j - 1] if j > 0 else float('-inf')
        right2 = nums2[j] if j < n2 else float('inf')

        if left1 <= right2 and left2 <= right1:
            if total % 2:
                return min(right1, right2)
            return (max(left1, left2) + min(right1, right2)) / 2
        elif left1 > right2:
            r = i - 1
        else:
            l = i + 1


# 8) Sliding Window Maximum (Deque) - O(n), O(k)
def sliding_window_max(nums: List[int], k: int) -> List[int]:
    """
    Find maximum in each sliding window of size k.
    """
    q, res = deque(), []
    for i, num in enumerate(nums):
        # remove indices outside window
        while q and q[0] <= i - k:
            q.popleft()
        # remove smaller values at end
        while q and nums[q[-1]] <= num:
            q.pop()
        q.append(i)
        if i >= k - 1:
            res.append(nums[q[0]])
    return res


# Quick test block
if __name__ == "__main__":
    print("Day 20: Advanced DSA Problems - quick tests")

    # Binary tree tests
    root = TreeNode(3, TreeNode(5), TreeNode(1))
    print("Level Order:", level_order(root))  # [[3], [5,1]]

    # Graph tests
    print("Cycle in Directed Graph:", has_cycle_directed(3, [[0, 1], [1, 2], [2, 0]]))  # True
    print("Topo Sort:", topo_sort(4, [[0, 1], [0, 2], [1, 3], [2, 3]]))  # [0,1,2,3]

    # Dijkstra
    print("Dijkstra:", dijkstra(5, [[0, 1, 2], [0, 2, 4], [1, 2, 1], [1, 3, 7], [2, 4, 3]], 0))

    # Kth largest
    print("Kth Largest (2nd):", kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5

    # Median of two arrays
    print("Median:", find_median_sorted_arrays([1, 3], [2]))  # 2

    # Sliding window max
    print("Sliding Window Max:", sliding_window_max([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
