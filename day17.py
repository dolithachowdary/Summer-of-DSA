# Day 17 - Important DSA Problems with Inline Comments

# 1. Next Greater Element (Using Stack)
def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n  # Initialize with -1
    stack = []  # Monotonic decreasing stack

    for i in range(n - 1, -1, -1):  # Traverse from right to left
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result

print("Next Greater Element:", next_greater_element([4, 5, 2, 25]))


# 2. Trapping Rain Water
def trap(height):
    n = len(height)
    left, right = 0, n - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

print("Trapping Rain Water:", trap([0,1,0,2,1,0,1,3,2,1,2,1]))


# 3. LRU Cache Implementation (Using OrderedDict)
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Mark as recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print("LRU Get 1:", lru.get(1))  # Returns 1
lru.put(3, 3)  # Removes key 2
print("LRU Get 2:", lru.get(2))  # Returns -1


# 4. Minimum Spanning Tree (Kruskal’s Algorithm)
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    ds = DisjointSet(n)
    mst_weight = 0
    mst_edges = []

    for u, v, w in edges:
        if ds.union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))

    return mst_weight, mst_edges

edges = [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
print("Kruskal’s MST:", kruskal(4, edges))


# 5. Word Ladder (BFS)
from collections import deque

def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    q = deque([(beginWord, 1)])
    while q:
        word, steps = q.popleft()
        if word == endWord:
            return steps
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i+1:]
                if new_word in wordSet:
                    wordSet.remove(new_word)
                    q.append((new_word, steps + 1))
    return 0

print("Word Ladder Length:", word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
