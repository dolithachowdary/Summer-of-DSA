# Day 12: Optimized Problems with Explanations and Inline Comments

# Problem 1: Optimised Aggressive Cows
# Goal: Place 'k' cows in 'n' stalls such that the minimum distance between any two cows is maximized.
# Approach:
# 1. Sort the positions of the cows.
# 2. Use binary search to find the maximum minimum distance.
# 3. Check if it is possible to place cows with the given minimum distance.
# 4. If it is possible, try for a larger distance, otherwise try a smaller distance.    
# 5. Return the maximum minimum distance found.
# 6. The time complexity is O(n log m), where n is the number of cows and m is the maximum distance.
# 7. The space complexity is O(1), as we are using only a few variables to store the positions and distances.

def cows(stalls, k):
    def canplace(mindist, stalls, k):
        cow = stalls[0]  # Place first cow at the first stall
        placedcows = 1
        for stall in range(1, len(stalls)):
            if stalls[stall] - cow >= mindist:
                placedcows += 1
                cow = stalls[stall]  # Place next cow here
                if placedcows == k:
                    return True
        return False

    stalls.sort()
    low = 1  # Minimum possible distance
    high = stalls[-1] - stalls[0]  # Maximum possible distance
    res = 0
    while low <= high:
        mindist = (low + high) // 2
        if canplace(mindist, stalls, k):
            res = mindist  # Try for a bigger minimum distance
            low = mindist + 1
        else:
            high = mindist - 1
    return res

stalls = [1, 2, 4, 8, 9]
k = 3
print("Aggressive Cows Result:", cows(stalls, k))


# Problem 2: Allocate Minimum Number of Pages
# Goal: Allocate books to students such that the maximum number of pages assigned is minimized.
# Approach:
# 1. Use binary search over the range [max(book), sum(books)].
# 2. Check if it’s possible to allocate pages within mid as max to all students.
# 3. If possible, try for smaller max. Else increase.

def is_possible(books, students, max_pages):
    count = 1  # At least one student
    pages_sum = 0
    for pages in books:
        if pages > max_pages:
            return False
        if pages_sum + pages > max_pages:
            count += 1  # Allocate to next student
            pages_sum = pages
        else:
            pages_sum += pages
    return count <= students

def allocate_books(books, students):
    if len(books) < students:
        return -1  # Not enough books
    low = max(books)
    high = sum(books)
    res = high
    while low <= high:
        mid = (low + high) // 2
        if is_possible(books, students, mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

books = [12, 34, 67, 90]
students = 2
print("Book Allocation Result:", allocate_books(books, students))


# Problem 3: Painter's Partition Problem
# Goal: Partition boards to painters such that the time to paint is minimized.
# Similar to book allocation: assign contiguous segments to minimize max time

# Given: k painters, and boards[] with lengths of boards to paint

def is_paint_possible(boards, k, max_len):
    count = 1
    total = 0
    for board in boards:
        if board > max_len:
            return False
        if total + board > max_len:
            count += 1
            total = board
        else:
            total += board
    return count <= k

def painters_partition(boards, k):
    low = max(boards)
    high = sum(boards)
    res = high
    while low <= high:
        mid = (low + high) // 2
        if is_paint_possible(boards, k, mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

boards = [10, 20, 30, 40]
k = 2
print("Painter Partition Result:", painters_partition(boards, k))


# Problem 4: Koko Eating Bananas
# Goal: Find the minimum eating speed so that all bananas can be eaten in h hours.
# Use binary search between 1 and max(piles)

def is_enough(piles, h, speed):
    hours = 0
    for pile in piles:
        hours += (pile + speed - 1) // speed  # ceil division
    return hours <= h

def min_eating_speed(piles, h):
    low = 1
    high = max(piles)
    res = high
    while low <= high:
        mid = (low + high) // 2
        if is_enough(piles, h, mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

piles = [3, 6, 7, 11]
h = 8
print("Koko Eating Speed Result:", min_eating_speed(piles, h))


# Problem 5: Minimum Number in Rotated Sorted Array
# Goal: Find the minimum element in a rotated sorted array.
# Approach: Binary search to find the rotation point (smallest element)

def find_min_rotated(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]

nums = [4, 5, 6, 7, 0, 1, 2]
print("Minimum in Rotated Sorted Array:", find_min_rotated(nums))
