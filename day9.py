# Day 9: Binary Search on Answers - GFG Practice
# Format: Each problem includes naive + optimized approach where applicable

from math import ceil

# -----------------------------------------------
# 1. Unique Element in a Sorted Array (GFG)
# Every element repeats exactly twice except one
# -----------------------------------------------
def unique(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    # Check corner cases
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n - 1] != nums[n - 2]:
        return nums[n - 1]

    low = 1
    high = n - 2

    # Binary Search to find unique element
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]

        # Check for pattern: if pair starts at mid or before
        elif (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or \
             (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(unique([1,1,2,2,3,3,4,5,5]))  # Output: 4

# -----------------------------------------------
# 2. Floor of Square Root (Naive)
# -----------------------------------------------
def perfectSquare(n):
    ans = 0
    for i in range(1, n + 1):
        if i * i <= n:
            ans = i
        else:
            break
    return ans

print(perfectSquare(11))  # Output: 3

# -----------------------------------------------
# 3. Floor of Square Root using Binary Search
# -----------------------------------------------
def perfectSquareBinary(n):
    low = 1
    high = n
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        root = mid * mid
        if root <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

print(perfectSquareBinary(5))  # Output: 2

# -----------------------------------------------
# 4. Nth Root of M (GFG)
# -----------------------------------------------
def nth_root(n, m):
    low = 1
    high = m

    while low <= high:
        mid = (low + high) // 2
        power = mid ** n
        if power == m:
            return mid
        elif power > m:
            high = mid - 1
        else:
            low = mid + 1

    return -1

print(nth_root(2, 49))  # Output: 7

# -----------------------------------------------
# 5. Smallest Divisor (Naive) - GFG
# -----------------------------------------------
def smallestDivisorNaive(arr, k):
    for div in range(1, max(arr) + 1):
        total = 0
        for num in arr:
            total += ceil(num / div)
        if total <= k:
            return div
    return -1

print(smallestDivisorNaive([1, 2, 5, 9], 6))  # Output: 5

# -----------------------------------------------
# 6. Smallest Divisor (Binary Search) - Optimal
# -----------------------------------------------
def smallestDivisorBinary(arr, k):
    low = 1
    high = max(arr)

    while low <= high:
        div = (low + high) // 2
        total = sum(ceil(num / div) for num in arr)
        if total <= k:
            high = div - 1
        else:
            low = div + 1
    return low

print(smallestDivisorBinary([1, 2, 5, 9], 6))  # Output: 5

# -----------------------------------------------
# 7. Koko Eating Bananas (Naive)
# -----------------------------------------------
def kokoNaive(arr, h):
    for i in range(1, max(arr) + 1):
        total_time = 0
        for bananas in arr:
            total_time += ceil(bananas / i)
        if total_time <= h:
            return i
    return -1

print(kokoNaive([3, 6, 7, 11], 8))  # Output: 4

# -----------------------------------------------
# 8. Koko Eating Bananas (Binary Search) - Optimal
# -----------------------------------------------
def kokoBinary(arr, h):
    low = 1
    high = max(arr)

    while low <= high:
        mid = (low + high) // 2
        total_time = sum(ceil(num / mid) for num in arr)

        if total_time <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low

print(kokoBinary([3, 6, 7, 11], 8))  # Output: 4

# -----------------------------------------------
# 9. Minimum Days to Make M Bouquets (GFG)
# -----------------------------------------------
def minDaysToMakeBouquets(bloomDay, m, k):
    def isPossible(days):
        bouquets = 0
        flowers = 0
        for day in bloomDay:
            if day <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m

    if m * k > len(bloomDay):
        return -1

    low = min(bloomDay)
    high = max(bloomDay)
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if isPossible(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

print(minDaysToMakeBouquets([1, 10, 3, 10, 2], 3, 1))  # Output: 3
