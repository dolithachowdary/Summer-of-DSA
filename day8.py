"""
Day 8: Binary Search and Variations
Includes binary search basics and advanced problems like lower/upper bound, rotated array search, etc.
"""

def binary_search(arr, k):
    """Standard binary search to find index of k."""
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def lower_bound(arr, k):
    """Smallest index such that arr[index] >= k."""
    low = 0
    n = len(arr)
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def upper_bound(arr, k):
    """Smallest index such that arr[index] > k."""
    low = 0
    n = len(arr)
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def floor_ceil(arr, x):
    """Return the floor and ceil value of x from a sorted array."""
    def get_floor():
        low, high = 0, len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                ans = arr[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def get_ceil():
        low, high = 0, len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = arr[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans

    return [get_floor(), get_ceil()]


def first_last_index(nums, target):
    """Find first and last index of a target in sorted array."""
    def get_lower():
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def get_upper():
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    lb = get_lower()
    if lb == -1 or nums[lb] != target:
        return [-1, -1]
    return [lb, get_upper() - 1]


def rotated_array_search(arr, key):
    """Search in rotated sorted array without duplicates."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def rotated_array_search_duplicates(arr, key):
    """Search in rotated sorted array with duplicates."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
        elif arr[low] <= arr[mid]:
            if arr[low] <= key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def find_min_in_rotated(arr):
    """Find the minimum element in a rotated sorted array."""
    low, high = 0, len(arr) - 1
    Min = float('inf')
    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[mid]:
            Min = min(Min, arr[low])
            low = mid + 1
        else:
            Min = min(Min, arr[mid])
            high = mid - 1
    return Min


def find_rotation_index(arr):
    """Find index of minimum element (number of rotations)."""
    low, high = 0, len(arr) - 1
    Min = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[mid]:
            if arr[low] < arr[Min]:
                Min = low
            high = mid - 1
        else:
            if arr[mid] < arr[Min]:
                Min = mid
            low = mid + 1
    return Min


if __name__ == "__main__":
    print("Binary Search:", binary_search([1, 2, 3, 4, 5, 6], 4))
    print("Lower Bound:", lower_bound([1, 2, 3, 3, 4, 4, 5, 6], 4))
    print("Upper Bound:", upper_bound([1, 2, 3, 3, 4, 4, 5, 6], 4))
    print("Floor and Ceil:", floor_ceil([1, 2, 3, 4, 5, 7], 6))
    print("First and Last Index:", first_last_index([1, 2, 3, 4, 4, 5, 7], 4))
    print("Rotated Array Search:", rotated_array_search([7, 8, 9, 1, 2, 3, 4, 5, 6], 4))
    print("Rotated Array Search with Duplicates:", rotated_array_search_duplicates([3, 2, 1, 2, 3, 3, 4], 3))
    print("Minimum in Rotated Array:", find_min_in_rotated([9, 8, 7, 1, 2, 3, 4]))
    print("Rotation Index:", find_rotation_index([9, 8, 7, 1, 2, 3, 4]))
