# ✅ Day 12: Binary Search Advanced – Allocation, Search, Peaks

# 1. Optimized Aggressive Cows Problem
def aggressive_cows(stalls, k):
    """
    Place cows in stalls such that the minimum distance between any two cows is maximized.
    Uses binary search on answer + greedy placement.
    """
    def can_place(mindist):
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
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if can_place(mid):
            result = mid
            low = mid + 1  # try to maximize
        else:
            high = mid - 1
    return result

# Example
print("Aggressive Cows:", aggressive_cows([1, 2, 4, 8, 9], 3))  # Output: 3

# 2. Allocate Books to Minimize Max Pages
def allocate_books(pages, k):
    """
    Split array of pages to k students such that max pages assigned to a student is minimized.
    Binary search on the answer.
    """
    def is_possible(limit):
        students = 1
        current_sum = 0
        for page in pages:
            if page > limit:
                return False
            if current_sum + page > limit:
                students += 1
                current_sum = page
            else:
                current_sum += page
        return students <= k

    if k > len(pages):
        return -1

    low, high = max(pages), sum(pages)
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

# Example
print("Allocate Books:", allocate_books([12, 34, 67, 90], 2))  # Output: 113

# 3. Search in Rotated Sorted Array
def search_rotated(nums, target):
    """
    Search for an element in a rotated sorted array.
    Returns index or -1.
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:  # Left half is sorted
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

# Example
print("Search Rotated:", search_rotated([4,5,6,7,0,1,2], 0))  # Output: 4

# 4. Find Peak Element
def find_peak(nums):
    """
    Find a peak element using binary search.
    A peak is greater than its neighbors.
    """
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low  # index of the peak

# Example
print("Peak Element Index:", find_peak([1, 2, 1, 3, 5, 6, 4]))  # Output: 5 or 1

# 5. Koko Eating Bananas (Leetcode 875)
def min_eating_speed(piles, h):
    """
    Koko has to eat all the bananas in h hours. Minimize the eating speed.
    Binary search on answer.
    """
    def can_eat(speed):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed
        return hours <= h

    low, high = 1, max(piles)
    result = high
    while low <= high:
        mid = (low + high) // 2
        if can_eat(mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

# Example
print("Koko Eating Speed:", min_eating_speed([3, 6, 7, 11], 8))  # Output: 4

# 6. Minimum Maximum Distance Between Gas Stations
def minmax_gas_distance(stations, k):
    """
    Place k new gas stations between existing ones to minimize the max distance.
    Greedy + Binary Search on answer.
    """
    def required_stations(distance):
        count = 0
        for i in range(len(stations) - 1):
            diff = stations[i + 1] - stations[i]
            count += int(diff / distance)
        return count

    low, high = 0.0, stations[-1] - stations[0]
    eps = 1e-6
    while high - low > eps:
        mid = (low + high) / 2
        if required_stations(mid) > k:
            low = mid
        else:
            high = mid
    return round(high, 6)

# Example
print("Min Gas Station Distance:", minmax_gas_distance([1, 2, 3, 4, 5, 6, 7, 8], 1))  # Output: ~1.0

# 7. Painters Partition Problem
def painters_partition(boards, k):
    """
    Partition boards among k painters to minimize the time (max board sum).
    Similar to book allocation.
    """
    def is_possible(limit):
        painter = 1
        curr_sum = 0
        for board in boards:
            if board > limit:
                return False
            if curr_sum + board > limit:
                painter += 1
                curr_sum = board
            else:
                curr_sum += board
        return painter <= k

    low, high = max(boards), sum(boards)
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

# Example
print("Painter Partition:", painters_partition([10, 20, 30, 40], 2))  # Output: 60

# 8. Split Array Largest Sum (Leetcode 410)
def split_array(nums, k):
    """
    Split array into k subarrays to minimize the largest sum among them.
    """
    def can_split(limit):
        count = 1
        curr = 0
        for num in nums:
            if curr + num > limit:
                count += 1
                curr = num
            else:
                curr += num
        return count <= k

    low, high = max(nums), sum(nums)
    while low <= high:
        mid = (low + high) // 2
        if can_split(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low

# Example
print("Split Array Min Largest Sum:", split_array([7,2,5,10,8], 2))  # Output: 18

# 9. Median of Two Sorted Arrays (Optimal O(log(min(n, m))))
def find_median_sorted_arrays(nums1, nums2):
    """
    Binary search on the smaller array to find the median of two sorted arrays.
    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    n1, n2 = len(nums1), len(nums2)
    low, high = 0, n1
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = (n1 + n2 + 1) // 2 - cut1

        l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
        l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
        r1 = float('inf') if cut1 == n1 else nums1[cut1]
        r2 = float('inf') if cut2 == n2 else nums2[cut2]

        if l1 <= r2 and l2 <= r1:
            if (n1 + n2) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2
            else:
                return max(l1, l2)
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1

# Example
print("Median of Sorted Arrays:", find_median_sorted_arrays([1, 3], [2]))  # Output: 2.0
