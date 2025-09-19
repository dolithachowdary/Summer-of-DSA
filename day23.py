"""
Day 23: Interesting DSA Problems with Inline Comments and Explanations
"""

from typing import List
import heapq
from collections import deque


# 1) Sliding Window Maximum
def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    Return maximum value in every sliding window of size k.
    Approach: Monotonic Deque (store indices).
    Time: O(n), Space: O(k)
    """
    dq = deque()  # stores indices, elements in decreasing order
    res = []
    for i, num in enumerate(nums):
        # Remove indices out of current window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # Maintain decreasing order in deque
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Window ready, append max
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res


# 2) Top K Frequent Elements
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements.
    Approach: Count + Heap
    Time: O(n log k), Space: O(n)
    """
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    # heap of (-count, num)
    heap = [(-count, num) for num, count in freq.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]


# 3) Kth Largest Element in Array
def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Find kth largest element in array.
    Approach: Min-heap of size k
    Time: O(n log k), Space: O(k)
    """
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


# 4) Longest Substring Without Repeating Characters
def length_of_longest_substring(s: str) -> int:
    """
    Sliding window + hashmap.
    Time: O(n), Space: O(128) ≈ O(1)
    """
    seen = {}
    l = 0
    maxlen = 0
    for r, ch in enumerate(s):
        if ch in seen and seen[ch] >= l:
            l = seen[ch] + 1  # move left pointer
        seen[ch] = r
        maxlen = max(maxlen, r - l + 1)
    return maxlen


# 5) Median of Two Sorted Arrays
def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Binary search on smaller array.
    Time: O(log(min(m,n))), Space: O(1)
    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        px = (low + high) // 2
        py = (x + y + 1) // 2 - px

        max_left_x = float('-inf') if px == 0 else nums1[px - 1]
        min_right_x = float('inf') if px == x else nums1[px]

        max_left_y = float('-inf') if py == 0 else nums2[py - 1]
        min_right_y = float('inf') if py == y else nums2[py]

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (x + y) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            else:
                return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            high = px - 1
        else:
            low = px + 1
    raise ValueError("Input arrays not sorted")


# 6) Word Search (Backtracking)
def exist(board: List[List[str]], word: str) -> bool:
    """
    Check if word exists in grid.
    DFS + backtracking
    Time: O(N * 4^L), Space: O(L) recursion stack
    """
    n, m = len(board), len(board[0])

    def dfs(i, j, k):
        if k == len(word):
            return True
        if i < 0 or j < 0 or i >= n or j >= m or board[i][j] != word[k]:
            return False

        tmp = board[i][j]
        board[i][j] = '#'  # mark visited
        res = (dfs(i + 1, j, k + 1) or
               dfs(i - 1, j, k + 1) or
               dfs(i, j + 1, k + 1) or
               dfs(i, j - 1, k + 1))
        board[i][j] = tmp  # unmark
        return res

    for i in range(n):
        for j in range(m):
            if dfs(i, j, 0):
                return True
    return False

# 7) Course Schedule (Detect Cycle in Directed Graph)
def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Detect if all courses can be finished.
    Approach: Topological Sort (Kahn's Algo)
    Time: O(V+E), Space: O(V+E)
    """
    indegree = [0] * numCourses
    graph = [[] for _ in range(numCourses)]
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1

    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    visited = 0
    while q:
        node = q.popleft()
        visited += 1
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    return visited == numCourses


# 8) Merge Intervals
def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals.
    Time: O(n log n), Space: O(n)
    """
    intervals.sort()
    res = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)  # merge
        else:
            res.append([start, end])
    return res


# 9) Spiral Matrix Traversal
def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Traverse matrix in spiral order.
    Time: O(m*n), Space: O(1)
    """
    res = []
    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
    while top <= bottom and left <= right:
        for j in range(left, right+1):
            res.append(matrix[top][j])
        top += 1
        for i in range(top, bottom+1):
            res.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left-1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
    return res




# -------------------------
# Quick Tests
# -------------------------
if __name__ == "__main__":
    print("Day 23 Quick Tests:")

    print("Sliding Window Maximum:", max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
    print("Top K Frequent:", top_k_frequent([1,1,1,2,2,3], 2))  # [1,2]
    print("Kth Largest:", find_kth_largest([3,2,1,5,6,4], 2))  # 5
    print("Longest Substring:", length_of_longest_substring("abcabcbb"))  # 3
    print("Median of Two Arrays:", find_median_sorted_arrays([1,3],[2]))  # 2
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    print("Word Search (ABCCED):", exist(board, "ABCCED"))  # True
