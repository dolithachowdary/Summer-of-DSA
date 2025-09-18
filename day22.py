"""
Day 22: Arrays, Math & Greedy Important Problems

Problems included:
1. Third Maximum Number (LC 414)
2. Majority Element (Boyer-Moore Voting Algorithm)
3. Product of Array Except Self (LC 238)
4. Rotate Array (LC 189, O(1) space)
5. Best Time to Buy and Sell Stock (LC 121)
6. Gas Station (LC 134, Greedy)
"""

from typing import List

# 1) Third Maximum Number
def thirdMax(nums: List[int]) -> int:
    """
    LC 414: Third Maximum Number
    Find the 3rd distinct maximum. If it doesn’t exist, return max.
    Time: O(n), Space: O(1)
    """
    first = second = third = None
    for num in nums:
        if num == first or num == second or num == third:
            continue
        if first is None or num > first:
            third, second, first = second, first, num
        elif second is None or num > second:
            third, second = second, num
        elif third is None or num > third:
            third = num
    return third if third is not None else first


# 2) Majority Element (Boyer-Moore Voting Algorithm)
def majorityElement(nums: List[int]) -> int:
    """
    LC 169: Majority Element
    Element appears > n/2 times.
    Boyer-Moore Voting Algo.
    Time: O(n), Space: O(1)
    """
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate


# 3) Product of Array Except Self
def productExceptSelf(nums: List[int]) -> List[int]:
    """
    LC 238: Product of Array Except Self
    No division allowed. Prefix + Suffix product trick.
    Time: O(n), Space: O(1) (output not counted)
    """
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res


# 4) Rotate Array (reverse trick)
def rotate(nums: List[int], k: int) -> None:
    """
    LC 189: Rotate Array
    Rotate nums by k steps to the right.
    Uses reverse trick. O(n), O(1) space.
    """
    n = len(nums)
    k %= n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


# 5) Best Time to Buy and Sell Stock
def maxProfit(prices: List[int]) -> int:
    """
    LC 121: Best Time to Buy and Sell Stock
    One transaction allowed.
    Time: O(n), Space: O(1)
    """
    min_price, profit = float("inf"), 0
    for p in prices:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)
    return profit


# 6) Gas Station (Greedy)
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    """
    LC 134: Gas Station
    Return starting index to travel circuit, else -1.
    Greedy: if total gas < cost → impossible.
    Time: O(n), Space: O(1)
    """
    total, tank, start = 0, 0, 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:
            tank = 0
            start = i + 1
    return start if total >= 0 else -1


# Quick tests
if __name__ == "__main__":
    print("Day 22: Arrays, Math & Greedy")

    print("Third Max [3,2,1] →", thirdMax([3,2,1]))  # 1
    print("Majority [3,2,3] →", majorityElement([3,2,3]))  # 3
    print("Product Except Self [1,2,3,4] →", productExceptSelf([1,2,3,4]))  # [24,12,8,6]

    arr = [1,2,3,4,5,6,7]
    rotate(arr, 3)
    print("Rotate [1,2,3,4,5,6,7],k=3 →", arr)  # [5,6,7,1,2,3,4]

    print("Max Profit [7,1,5,3,6,4] →", maxProfit([7,1,5,3,6,4]))  # 5
    print("Gas Station →", canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))  # 3
