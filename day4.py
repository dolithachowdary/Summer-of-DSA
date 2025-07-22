# --------------------------------------------
# Recursion Day 2 - Advanced Recursive Problems
# --------------------------------------------

# 1. Sum of digits in integer
def summ(n):
    """
    Recursively calculates the sum of digits in an integer.

    Args:
    n (int): The number.

    Returns:
    int: Sum of digits.
    """
    if n == 0:
        return 0
    r = n % 10
    return r + summ(n // 10)

print("Sum of digits:", summ(1208))

# 2. Count number of digits
def count(n):
    """
    Recursively counts the number of digits in an integer.

    Args:
    n (int): The number.

    Returns:
    int: Number of digits.
    """
    if n == 0:
        return 0
    return 1 + count(n // 10)

print("Count of digits:", count(1234))

# 3. Find the minimum and maximum in the list
def minmax(nums):
    """
    Recursively finds the minimum and maximum in a list.

    Args:
    nums (list): List of integers.

    Returns:
    tuple: (minimum, maximum)
    """
    def rec(nums, i):
        if i == len(nums) - 1:
            return nums[i], nums[i]
        mini, maxi = rec(nums, i + 1)
        mini = mini if mini < nums[i] else nums[i]
        maxi = maxi if maxi > nums[i] else nums[i]
        return mini, maxi

    return rec(nums, 0)

print("Minimum and Maximum:", minmax([5, 3, 1, 9, 2]))

# 4. Reverse a number using recursion
def reverse_number(n, rev=0):
    """
    Recursively reverses a number.

    Args:
    n (int): The number to reverse.
    rev (int): Accumulator for reversed number.

    Returns:
    int: Reversed number.
    """
    if n == 0:
        return rev
    last_digit = n % 10
    rev = rev * 10 + last_digit
    return reverse_number(n // 10, rev)

print("Reversed number:", reverse_number(1234))

# 5. Check if a string is palindrome using recursion
def is_palindrome(s):
    """
    Recursively checks if a string is a palindrome.

    Args:
    s (str): The string.

    Returns:
    bool: True if palindrome, else False.
    """
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print("Is palindrome:", is_palindrome("madam"))

# 6. Product of digits of a number
def product_of_digits(n):
    """
    Recursively finds the product of digits in an integer.

    Args:
    n (int): The number.

    Returns:
    int: Product of digits.
    """
    if n == 0:
        return 0
    if n < 10:
        return n
    return (n % 10) * product_of_digits(n // 10)

print("Product of digits:", product_of_digits(1234))

# 7. Sum of elements in a list
def sum_list(lst):
    """
    Recursively sums all elements in a list.

    Args:
    lst (list): List of integers.

    Returns:
    int: Sum of elements.
    """
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print("Sum of list:", sum_list([1, 2, 3, 4, 5]))

# 8. Count number of zeros in a number
def count_zeros(n):
    """
    Recursively counts the number of zeros in an integer.

    Args:
    n (int): The number.

    Returns:
    int: Count of zeros.
    """
    if n == 0:
        return 1
    def helper(n):
        if n == 0:
            return 0
        return (1 if n % 10 == 0 else 0) + helper(n // 10)
    return helper(n)

print("Count of zeros:", count_zeros(1020300))

# 9. GCD (Greatest Common Divisor) using recursion
def gcd(a, b):
    """
    Recursively computes the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.

    Args:
    a (int): First number.
    b (int): Second number.

    Returns:
    int: GCD of a and b.
    """
    if b == 0:
        return a
    return gcd(b, a % b)

print("GCD:", gcd(36, 60))
