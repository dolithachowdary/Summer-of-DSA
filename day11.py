# Day 11 Practice Problems with inline comments

# 1. Spiral Matrix Traversal
def spiral_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    sr, er = 0, n - 1  # Start and End row
    sc, ec = 0, m - 1  # Start and End column
    result = []

    while sr <= er and sc <= ec:
        # Traverse Left to Right
        for i in range(sc, ec + 1):
            result.append(matrix[sr][i])
        sr += 1

        # Traverse Top to Bottom
        for i in range(sr, er + 1):
            result.append(matrix[i][ec])
        ec -= 1

        # Traverse Right to Left
        if sr <= er:
            for i in range(ec, sc - 1, -1):
                result.append(matrix[er][i])
            er -= 1

        # Traverse Bottom to Top
        if sc <= ec:
            for i in range(er, sr - 1, -1):
                result.append(matrix[i][sc])
            sc += 1

    return result


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
print("Spiral Matrix:", spiral_matrix(matrix))


# 2. Lexicographically Minimal String after one operation
def lexi(s):
    lst = []
    for m in range(len(s)):
        lst.append(s[m] + s[:m] + s[m + 1:])  # Move s[m] to front and delete original
    lst.sort()
    return lst[0]


s = "baca"
print("Lexi Min String:", lexi(s))


# 3. Aggressive Cows (Binary Search)
def cows(stalls, k):
    def canplace(mindist, stalls, k):
        cow = stalls[0]
        placed = 1
        for i in range(1, len(stalls)):
            if stalls[i] - cow >= mindist:
                placed += 1
                cow = stalls[i]
                if placed == k:
                    return True
        return False

    stalls.sort()
    low = 1
    high = stalls[-1] - stalls[0]
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if canplace(mid, stalls, k):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


stalls = [1, 2, 4, 8, 9]
k = 3
print("Aggressive Cows Max Distance:", cows(stalls, k))


# 4. Trapping Rain Water
def trap(height):
    if not height: return 0
    n = len(height)
    left = [0] * n
    right = [0] * n

    left[0] = height[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], height[i])

    right[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], height[i])

    water = 0
    for i in range(n):
        water += min(left[i], right[i]) - height[i]
    return water


print("Trapped Water:", trap([4, 2, 0, 3, 2, 5]))


# 5. Subarray Sum Equals K
def subarraySum(nums, k):
    from collections import defaultdict
    count = 0
    curr_sum = 0
    prefix = defaultdict(int)
    prefix[0] = 1

    for num in nums:
        curr_sum += num
        if curr_sum - k in prefix:
            count += prefix[curr_sum - k]
        prefix[curr_sum] += 1
    return count


nums = [1, 1, 1]
k = 2
print("Subarrays with Sum =", k, ":", subarraySum(nums, k))


# 6. Kth Largest Element in an Array
def findKthLargest(nums, k):
    import heapq
    return heapq.nlargest(k, nums)[-1]


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(f"{k}th Largest Element:", findKthLargest(nums, k))


# 7. Merge Intervals
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = result[-1][1]
        if start <= last_end:
            result[-1][1] = max(last_end, end)
        else:
            result.append([start, end])
    return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print("Merged Intervals:", merge(intervals))
