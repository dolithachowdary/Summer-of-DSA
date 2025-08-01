### ✅ Day 12: Problems with Code and Comments
---

#### 📌 1. **Optimized Aggressive Cows**

```python
# Place cows in stalls so that the minimum distance between any two is maximized
def cows(stalls, k):
    def canplace(mindist, stalls, k):
        cow = stalls[0]
        placedcows = 1
        for i in range(1, len(stalls)):
            if stalls[i] - cow >= mindist:
                placedcows += 1
                cow = stalls[i]
                if placedcows == k:
                    return True
        return False

    stalls.sort()  # Sort the stall positions
    low, high = 1, stalls[-1] - stalls[0]
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if canplace(mid, stalls, k):
            result = mid
            low = mid + 1  # Try for a bigger minimum distance
        else:
            high = mid - 1  # Try for a smaller minimum distance
    return result

stalls = [1, 2, 4, 8, 9]
k = 3
print("Aggressive cows max min distance:", cows(stalls, k))
```

---

#### 📘 2. **Allocate Books (Binary Search on Answer)**

```python
# Allocate books to students such that the maximum number of pages assigned is minimized
def allocate_books(pages, students):
    def is_possible(limit):
        count = 1
        total = 0
        for page in pages:
            if page > limit:
                return False
            if total + page > limit:
                count += 1
                total = page
            else:
                total += page
        return count <= students

    if len(pages) < students:
        return -1

    low, high = max(pages), sum(pages)
    answer = -1

    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer

pages = [12, 34, 67, 90]
students = 2
print("Minimum max pages assigned:", allocate_books(pages, students))
```

---

#### 📗 3. **Search in Rotated Sorted Array**

```python
# Find target in a rotated sorted array using modified binary search
def search_rotated(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid

        # Left part sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right part sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

arr = [4,5,6,7,0,1,2]
target = 0
print("Target found at index:", search_rotated(arr, target))
```

---

#### 📙 4. **Find Peak Element (Binary Search)**

```python
# A peak element is greater than its neighbors
def find_peak(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1  # Go right
        else:
            high = mid  # Go left
    return low  # or return arr[low] for value

arr = [1, 2, 3, 1]
print("Peak element index:", find_peak(arr))
```

---

#### 📕 5. **Koko Eating Bananas (Binary Search on Answer)**

```python
# Find minimum eating speed to finish all bananas within H hours
def min_eating_speed(piles, h):
    def can_eat(speed):
        hours = 0
        for pile in piles:
            hours += -(-pile // speed)  # Ceiling division
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

piles = [3, 6, 7, 11]
h = 8
print("Minimum eating speed:", min_eating_speed(piles, h))
```

---

