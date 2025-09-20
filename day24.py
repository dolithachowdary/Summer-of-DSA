"""
✅ Day 24: Interesting + Fun + Important Problems

Problems:
1. Sudoku Solver (Backtracking)
2. Word Search II (Trie + DFS)
3. Snakes and Ladders (BFS)
4. LFU Cache Implementation (HashMap + DLL + Frequency Map)
5. Candy Distribution (Greedy)
6. Sliding Window Maximum (Deque)
7. Longest Consecutive Sequence (HashSet)
8. Clone Graph (DFS/BFS + HashMap)
"""

# ----------------------------
# 1. Sudoku Solver (Backtracking)
# ----------------------------
def solveSudoku(board):
    def is_valid(r, c, num):
        for i in range(9):
            if board[r][i] == num or board[i][c] == num:
                return False
        # Check 3x3 subgrid
        start_r, start_c = 3 * (r // 3), 3 * (c // 3)
        for i in range(start_r, start_r + 3):
            for j in range(start_c, start_c + 3):
                if board[i][j] == num:
                    return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for num in map(str, range(1, 10)):
                        if is_valid(r, c, num):
                            board[r][c] = num
                            if backtrack():
                                return True
                            board[r][c] = "."
                    return False
        return True

    backtrack()
# Time: O(9^(81)) worst-case | Space: O(81) recursion stack


# ----------------------------
# 2. Word Search II (Trie + DFS)
# ----------------------------
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def findWords(board, words):
    root = TrieNode()
    # Build trie
    for word in words:
        node = root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.word = word

    res = []
    rows, cols = len(board), len(board[0])

    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node.children:
            return
        nxt = node.children[ch]
        if nxt.word:
            res.append(nxt.word)
            nxt.word = None  # avoid duplicates
        board[r][c] = "#"
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                dfs(nr, nc, nxt)
        board[r][c] = ch

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)
    return res
# Time: O(M * 4^L) where M = total board cells, L = max word length
# Space: O(N) for trie, N = total chars in words


# ----------------------------
# 3. Snakes and Ladders (BFS)
# ----------------------------
from collections import deque

def snakesAndLadders(board):
    n = len(board)

    def get_pos(s):
        quot, rem = divmod(s-1, n)
        row = n-1-quot
        col = rem if quot%2==0 else n-1-rem
        return row, col

    visited = set()
    q = deque([(1,0)])  # (cell, moves)
    while q:
        s, moves = q.popleft()
        if s == n*n:
            return moves
        for i in range(1, 7):
            nxt = s+i
            if nxt > n*n: break
            r,c = get_pos(nxt)
            if board[r][c] != -1:
                nxt = board[r][c]
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, moves+1))
    return -1
# Time: O(n^2) | Space: O(n^2)


# ----------------------------
# 4. LFU Cache (HashMap + DLL + Frequency Map)
# ----------------------------
from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_val = {}
        self.key_freq = {}
        self.freq_map = defaultdict(OrderedDict)
        self.min_freq = 0

    def _update(self, key, val=None):
        freq = self.key_freq[key]
        self.freq_map[freq].pop(key)
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.key_freq[key] = freq+1
        self.freq_map[freq+1][key] = val if val is not None else self.key_val[key]

    def get(self, key: int) -> int:
        if key not in self.key_val: return -1
        self._update(key)
        return self.key_val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return
        if key in self.key_val:
            self.key_val[key] = value
            self._update(key, value)
            return
        if len(self.key_val) >= self.cap:
            k,_ = self.freq_map[self.min_freq].popitem(last=False)
            del self.key_val[k], self.key_freq[k]
        self.key_val[key] = value
        self.key_freq[key] = 1
        self.freq_map[1][key] = value
        self.min_freq = 1
# Time: O(1) | Space: O(capacity)


# ----------------------------
# 5. Candy Distribution (Greedy)
# ----------------------------
def candy(ratings):
    n = len(ratings)
    candies = [1]*n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1]+1
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1]+1)
    return sum(candies)
# Time: O(n) | Space: O(n)


# ----------------------------
# 6. Sliding Window Maximum (Deque)
# ----------------------------
from collections import deque

def maxSlidingWindow(nums, k):
    dq, res = deque(), []
    for i, num in enumerate(nums):
        # Remove smaller numbers
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        # Remove out-of-window indices
        if dq[0] <= i-k:
            dq.popleft()
        if i >= k-1:
            res.append(nums[dq[0]])
    return res
# Time: O(n) | Space: O(k)


# ----------------------------
# 7. Longest Consecutive Sequence (HashSet)
# ----------------------------
def longestConsecutive(nums):
    num_set, longest = set(nums), 0
    for num in num_set:
        if num-1 not in num_set:
            cur, streak = num, 1
            while cur+1 in num_set:
                cur += 1
                streak += 1
            longest = max(longest, streak)
    return longest
# Time: O(n) | Space: O(n)


# ----------------------------
# 8. Clone Graph (DFS + HashMap)
# ----------------------------
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def cloneGraph(node):
    old_to_new = {}
    def dfs(n):
        if not n: return None
        if n in old_to_new: return old_to_new[n]
        copy = Node(n.val)
        old_to_new[n] = copy
        for nei in n.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    return dfs(node)
# Time: O(V+E) | Space: O(V)
