# 📘 Day 16 – Sliding Window, Subarrays & String Problems

# -----------------------------------------
# Pattern 1 - Subarray generation
# -----------------------------------------
arr = [5, 10, 8]
n = len(arr)

# Generate all subarrays
for i in range(0, n):
    for j in range(i, n):
        print(arr[i:j+1])


# -----------------------------------------
# Pattern 2 - Maximum/Minimum Subarray Sum
# -----------------------------------------

# Brute Force: Find maximum sum of subarray of size k
# TC : O(N^2)
def Max_Sum(arr, k):
    n = len(arr)
    Max = 0
    for i in range(0, n):
        for j in range(i, n):
            if len(arr[i:j+1]) == k:
                Max = max(Max, sum(arr[i:j+1]))
    return Max

print(Max_Sum([1, 3, 10, 7, 4], 3))  # Output: 21


# Optimal: Sliding Window
def Max_Sum(arr, k):
    n = len(arr)
    if n < k:
        return -1

    window_sum = sum(arr[:k])   # Initial window sum
    max_sum = window_sum

    for i in range(1, n-k+1):
        window_sum = window_sum - arr[i-1] + arr[i+k-1]  # Slide window
        max_sum = max(window_sum, max_sum)

    return max_sum

print(Max_Sum([2, 3, 5, 8, 10, 12, 3, 1], 4))  # Output: 35


# Expansion and Shrink method
def Max_Sum(arr, k):
    n = len(arr)
    left, right = 0, k-1
    Sum = sum(arr[:k])
    Max = Sum

    while right < n-1:
        Sum -= arr[left]    # Remove leftmost
        left += 1
        right += 1
        Sum += arr[right]   # Add rightmost
        Max = max(Sum, Max)
    return Max

print(Max_Sum([2, 3, 5, 8, 10, 12, 3, 1], 4))  # Output: 35


# -----------------------------------------
# Maximum length subarray with sum <= k
# -----------------------------------------

# Brute Force: O(N^2)
def Max_length(arr, k):
    n = len(arr)
    max_Len = 0
    for i in range(0, n):
        for j in range(i, n):
            if sum(arr[i:j+1]) <= k:
                max_Len = max(max_Len, j-i+1)
    return max_Len

print(Max_length([2, 3, 5, 8, 10, 12, 3, 1], 4))  # Output: 1


# Optimal Sliding Window: O(N)
def Max_Length(arr, k):
    n = len(arr)
    left, right = 0, 1
    Sum = arr[0]
    Max_Len = 1

    while right < n:
        if Sum + arr[right] <= k:
            Sum += arr[right]
            Max_Len = max(Max_Len, right - left + 1)
            right += 1
        else:
            Sum -= arr[left]
            left += 1
    return Max_Len

print(Max_Length([2, 5, 1, 7, 10], 14))  # Output: 3


# Sliding Window with while loop inside: O(N)
def Length(arr, k):
    n = len(arr)
    left, right = 0, 0
    Sum = 0
    Max_Len = 0
    while right < n:  # O(N)
        Sum += arr[right]
        while Sum > k:  # Shrink window
            Sum -= arr[left]
            left += 1
        Max_Len = max(Max_Len, right-left+1)
        right += 1
    return Max_Len

print(Length([2, 5, 1, 7, 10], 14))  # Output: 3


# -----------------------------------------
# Leetcode 1423: Max points from cards
# Sliding Window – pick from both ends
# -----------------------------------------
def practice(cardpoints, k):
    n = len(cardpoints)
    left = 0
    right = k-1
    left_sum = sum(cardpoints[left:right+1])  # First k elements
    right_sum = 0
    right_index = n-1
    maxSum = left_sum

    for i in range(k, -1, -1):
        if right_index >= 0:
            right_sum += cardpoints[right_index]
            right_index -= 1
        if left < n:
            left_sum -= cardpoints[left]
            left += 1
        maxSum = max(maxSum, left_sum + right_sum)
    return maxSum

print(practice([1, 2, 3, 4, 5, 6, 1], 3))  # Output: 12


# -----------------------------------------
# Longest Substring Without Repeating Characters
# -----------------------------------------

# Brute Force: O(N^2)
def lengthOfLongestSubstring(s):
    n = len(s)
    maxLength = 0
    for i in range(n):
        checker = [0] * 256   # Fixed array for ASCII chars
        for j in range(i, n):
            if checker[ord(s[j])] == 1:  # Repeated char
                break
            checker[ord(s[j])] = 1
            maxLength = max(maxLength, j-i+1)
    return maxLength

print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3


# Optimal using hashmap: O(N)
def length(s):
    n = len(s)
    maxLength = 0
    d = {}
    left, right = 0, 0

    while right < n:
        if s[right] in d and d[s[right]] >= left:
            left = d[s[right]] + 1   # Move left pointer
        d[s[right]] = right
        maxLength = max(maxLength, right-left+1)
        right += 1
    return maxLength

print(length("abcabcbb"))  # Output: 3


# -----------------------------------------
# Leetcode 1004: Longest subarray with at most K zeros
# -----------------------------------------

# Brute Force: O(N^2)
def longest(nums, k):
    n = len(nums)
    maxLen = 0
    for i in range(0, n):
        zero = 0
        for j in range(i, n):
            if nums[j] == 0:
                zero += 1
            if zero > k:
                break
            maxLen = max(maxLen, j-i+1)
    return maxLen

print(longest([1, 0, 0, 1, 0, 1, 0, 1], 2))  # Output: 5


# Optimal: Sliding Window O(N)
def one(arr, k):
    n = len(arr)
    maxLength = 0
    left, right = 0, 0
    count = 0

    while right < n:
        if arr[right] == 0:
            count += 1
        if count > k:
            while count > k:
                if arr[left] == 0:
                    count -= 1
                left += 1
        maxLength = max(maxLength, right - left + 1)
        right += 1
    return maxLength

print(one([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  # Output: 10
