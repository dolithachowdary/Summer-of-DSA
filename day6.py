"""
Day 6: Recursion - Part 3
This file includes recursive solutions to a variety of problems,
with function-level docstrings and inline comments for clarity.
"""

# 1. Product of Digits
def product_of_digits(n):
    """
    Recursively calculates the product of all digits in the integer n.
    Example: 123 → 1*2*3 = 6
    """
    if n == 0:
        return 0
    if n < 10:
        return n
    return (n % 10) * product_of_digits(n // 10)  # Multiply last digit with product of remaining
print("Product of digits (123):", product_of_digits(123))


# 2. Check Palindrome using Recursion
def is_palindrome(s, i=0):
    """
    Recursively checks if a string s is a palindrome.
    """
    j = len(s) - 1 - i
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return is_palindrome(s, i + 1)
print("Is 'madam' a palindrome?:", is_palindrome("madam"))


# 3. GCD (Greatest Common Divisor) using Recursion
def gcd(a, b):
    """
    Finds the GCD of two numbers using Euclidean algorithm recursively.
    """
    if b == 0:
        return a
    return gcd(b, a % b)  # GCD of b and remainder of a divided by b
print("GCD of 48 and 18:", gcd(48, 18))


# 4. Reverse a String
def reverse_string(s):
    """
    Reverses a string recursively and returns it.
    """
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]  # Reverse rest of string and add first char at end
print("Reverse of 'hello':", reverse_string("hello"))


# 5. Print all subsets of a string
def subsets(s, curr="", i=0):
    """
    Prints all possible subsets of a string using recursion.
    """
    if i == len(s):
        print(curr)
        return
    subsets(s, curr + s[i], i + 1)  # Include current char
    subsets(s, curr, i + 1)         # Exclude current char
print("Subsets of 'ab':")
subsets("ab")


# 6. Power of a number (x^n)
def power(x, n):
    """
    Recursively computes x raised to the power n.
    """
    if n == 0:
        return 1
    return x * power(x, n - 1)  # Multiply x with x^(n-1)
print("3^4:", power(3, 4))


# 7. Check if array is sorted (strictly increasing)
def is_sorted(arr, i=0):
    """
    Recursively checks if the array is sorted in strictly increasing order.
    """
    if i == len(arr) - 1:
        return True
    if arr[i] >= arr[i + 1]:
        return False
    return is_sorted(arr, i + 1)
print("Is [1, 2, 3, 5] sorted?:", is_sorted([1, 2, 3, 5]))


# 8. Recursive Binary Search
def binary_search(arr, target, left=0, right=None):
    """
    Performs binary search on a sorted list to find the target value.
    Returns True if found, else False.
    """
    if right is None:
        right = len(arr) - 1
    if left > right:
        return False
    mid = (left + right) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)
print("Is 5 in [1, 3, 5, 7, 9]?:", binary_search([1, 3, 5, 7, 9], 5))


# 9. First Index of Element
def first_index(arr, target, i=0):
    """
    Recursively finds the first index of the target element.
    Returns -1 if not found.
    """
    if i == len(arr):
        return -1
    if arr[i] == target:
        return i
    return first_index(arr, target, i + 1)
print("First index of 7 in [1, 7, 3, 7]:", first_index([1, 7, 3, 7], 7))


# 10. Last Index of Element
def last_index(arr, target, i=0):
    """
    Recursively finds the last index of the target element.
    Returns -1 if not found.
    """
    if i == len(arr):
        return -1
    res = last_index(arr, target, i + 1)  # Look ahead first
    if res != -1:
        return res
    if arr[i] == target:
        return i
    return -1
print("Last index of 7 in [1, 7, 3, 7]:", last_index([1, 7, 3, 7], 7))


# 11. Subsets (Power Set)
def subsets(nums):
    res = []

    def backtrack(start, path):
        res.append(path[:])  # Append a copy of the current path
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # Backtrack

    backtrack(0, [])
    return res


# 12. Combinations (n choose k)
def combine(n, k):
    res = []

    def backtrack(start, path):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return res


# 13. Letter Case Permutation
def letter_case_permutation(s):
    res = []

    def backtrack(index, path):
        if index == len(s):
            res.append("".join(path))
            return
        if s[index].isalpha():
            # Lowercase branch
            path.append(s[index].lower())
            backtrack(index + 1, path)
            path.pop()
            # Uppercase branch
            path.append(s[index].upper())
            backtrack(index + 1, path)
            path.pop()
        else:
            path.append(s[index])
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return res


# 14. Generate Well-Formed Parentheses
def generate_parentheses(n):
    res = []

    def backtrack(open_count, close_count, path):
        if len(path) == 2 * n:
            res.append("".join(path))
            return
        if open_count < n:
            path.append('(')
            backtrack(open_count + 1, close_count, path)
            path.pop()
        if close_count < open_count:
            path.append(')')
            backtrack(open_count, close_count + 1, path)
            path.pop()

    backtrack(0, 0, [])
    return res


# 15. Word Break using dictionary
def word_break(s, word_dict):
    res = []

    def backtrack(start, path):
        if start == len(s):
            res.append(" ".join(path))
            return
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_dict:
                path.append(word)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return res

✅ Sample Usage:

print(subsets([1, 2, 3]))
print(combine(4, 2))
print(letter_case_permutation("a1b2"))
print(generate_parentheses(3))
print(word_break("leetcode", {"leet", "code"}))

