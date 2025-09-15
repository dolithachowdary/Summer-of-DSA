"""
Day 19: Important Dynamic Programming Problems (with docstrings + inline comments)

Problems included:
1. Longest Increasing Subsequence (n log n)
2. 0/1 Knapsack (classic DP)
3. Unbounded Knapsack / Coin Change (min coins)
4. Edit Distance (Levenshtein distance)
5. Partition Equal Subset Sum
6. House Robber (linear DP)
7. Unique Paths (grid DP)
8. Longest Common Subsequence (LCS)
"""

from typing import List


# 1) Longest Increasing Subsequence (LIS) - O(n log n)
def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    Find length of the Longest Increasing Subsequence in nums.
    Uses patience sorting approach with a tails array and binary search -> O(n log n).
    """
    if not nums:
        return 0

    import bisect
    tails = []  # tails[i] = smallest tail value of an increasing subsequence of length i+1
    for x in nums:
        # find insertion position for x in tails (first >= x)
        pos = bisect.bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x
    return len(tails)


# 2) 0/1 Knapsack (classic DP) - O(n * W)
def knapsack_01(weights: List[int], values: List[int], W: int) -> int:
    """
    0/1 knapsack: maximize total value without exceeding weight W.
    Bottom-up DP: dp[i] = max value achievable with capacity i (space-optimized).
    """
    n = len(weights)
    # dp[c] = max value for capacity c
    dp = [0] * (W + 1)
    for i in range(n):
        w, v = weights[i], values[i]
        # iterate capacities from high to low to avoid reuse of item
        for c in range(W, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[W]


# 3) Unbounded Knapsack / Min Coin Change (min number of coins to make amount) - O(n * amount)
def coin_change_min(coins: List[int], amount: int) -> int:
    """
    Find minimum number of coins to make 'amount' when coins can be used unlimited times.
    Returns -1 if impossible.
    """
    INF = amount + 1
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != INF else -1


# 4) Edit Distance (Levenshtein) - O(n*m)
def edit_distance(word1: str, word2: str) -> int:
    """
    Classic DP computing min edits (insert/delete/replace) to transform word1 -> word2.
    Uses O(n * m) time and O(min(n,m)) space if optimized; here we do O(m) space.
    """
    n, m = len(word1), len(word2)
    # ensure word2 is shorter to use less space (optional)
    if n < m:
        # swap to keep m <= n (so we use O(m) space)
        return edit_distance(word2, word1)

    prev = list(range(m + 1))  # dp for empty prefix of word1 -> cost = j (insert all)
    for i in range(1, n + 1):
        curr = [i] + [0] * m  # cost of converting first i chars of word1 to empty word2 = i (all deletes)
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]  # characters equal -> no operation
            else:
                # replace, insert (into word1), delete (from word1)
                curr[j] = 1 + min(prev[j - 1],    # replace
                                  curr[j - 1],    # insert
                                  prev[j])        # delete
        prev = curr
    return prev[m]


# 5) Partition Equal Subset Sum - subset sum via DP (boolean)
def can_partition_equal_subset(nums: List[int]) -> bool:
    """
    Determine if array can be partitioned into two subsets with equal sum.
    Equivalent to checking if subset with sum total_sum/2 exists.
    """
    total = sum(nums)
    # if total is odd, cannot partition equally
    if total % 2 != 0:
        return False
    target = total // 2
    # dp[a] True if some subset sums to a
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        # iterate downward to avoid using an item multiple times
        for a in range(target, num - 1, -1):
            dp[a] = dp[a] or dp[a - num]
    return dp[target]


# 6) House Robber (linear DP)
def house_robber(nums: List[int]) -> int:
    """
    Given array of non-negative numbers representing amount of money, find maximum you can rob,
    without robbing adjacent houses.
    O(n) time, O(1) space solution using two variables.
    """
    prev2, prev1 = 0, 0  # prev2 = dp[i-2], prev1 = dp[i-1]
    for x in nums:
        curr = max(prev1, prev2 + x)  # choose skip (prev1) or rob current (prev2 + x)
        prev2, prev1 = prev1, curr
    return prev1


# 7) Unique Paths (grid DP)
def unique_paths(m: int, n: int) -> int:
    """
    Count unique paths in an m x n grid from top-left to bottom-right moving only right or down.
    Uses 1D DP where dp[j] = #paths to reach cell in current row at column j.
    """
    dp = [1] * n  # first row all 1s
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]


# 8) Longest Common Subsequence (LCS) - O(n*m)
def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Return length of longest common subsequence between text1 and text2.
    Uses bottom-up DP with O(min(n,m)) space optimization.
    """
    n, m = len(text1), len(text2)
    if n < m:
        # ensure text2 is the shorter string for less space
        return longest_common_subsequence(text2, text1)

    prev = [0] * (m + 1)
    for i in range(1, n + 1):
        curr = [0] * (m + 1)
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr
    return prev[m]


# Optional: small tests when running this file directly
if __name__ == "__main__":
    print("Day 19: Dynamic Programming - quick tests")

    # LIS
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print("LIS length (expected 4):", longest_increasing_subsequence(arr))

    # 0/1 knapsack
    wts = [3, 2, 1]
    vals = [5, 3, 2]
    W = 3
    print("0/1 Knapsack (expected 5):", knapsack_01(wts, vals, W))

    # coin change
    coins = [1, 2, 5]
    amount = 11
    print("Min coins for 11 (expected 3):", coin_change_min(coins, amount))

    # edit distance
    print("Edit distance 'kitten'->'sitting' (expected 3):", edit_distance("kitten", "sitting"))

    # partition equal subset
    print("Can partition [1,5,11,5] (expected True):", can_partition_equal_subset([1, 5, 11, 5]))

    # house robber
    print("House robber [2,7,9,3,1] (expected 12):", house_robber([2, 7, 9, 3, 1]))

    # unique paths
    print("Unique paths 3x7 (expected 28):", unique_paths(3, 7))

    # LCS
    print("LCS 'abcde' & 'ace' (expected 3):", longest_common_subsequence("abcde", "ace"))
