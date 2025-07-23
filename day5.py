

# 📘 Day 5: Recursion & Backtracking

# Power function (iterative)
def mypow(n, x):
    """
    Calculate x raised to the power n without using ** operator (iterative).
    Handles negative powers by inverting x.
    Time complexity: O(n)
    """
    if n < 0:
        x = 1 / x
        n = abs(n)
    ans = 1
    for i in range(n):
        ans *= x
    return ans

print(mypow(2, 3))


# Power function (recursive)
def mypow2(n, x):
    """
    Recursive version to calculate x^n.
    Uses divide-and-conquer method for O(log n) time.
    """
    if n == 0:
        return 1
    if n % 2 == 1:
        return x * mypow2(n - 1, x)
    return mypow2(n // 2, x * x)

print(mypow2(2, 5))


# Generate all subsets of a list (power set)
def generate_subsets(nums):
    """
    Generates all subsets of a given list using recursion.
    Time complexity: O(2^n)
    """
    def gen(ind, curr, ans):
        if ind == len(nums):
            ans.append(curr.copy())
            return
        curr.append(nums[ind])
        gen(ind + 1, curr, ans)
        curr.pop()
        gen(ind + 1, curr, ans)

    ans = []
    gen(0, [], ans)
    return ans

print(generate_subsets([1, 2, 3]))


# Subsequence sum

def subsequence_sum(nums, target):
    """
    Find if there is any subsequence that sums up to the target.
    """
    def helper(i, total):
        if i == len(nums):
            return total == target
        return helper(i + 1, total + nums[i]) or helper(i + 1, total)

    return helper(0, 0)

print(subsequence_sum([1, 2, 3, 4], 6))


# Acronym matching
def acronym_match(words, short_form):
    """
    Check if the first letter of each word in list forms the short_form.
    """
    acronym = "".join(w[0] for w in words)
    return acronym == short_form

print(acronym_match(["alice", "bob", "charlie"], "abc"))


# Combination Sum (elements can be reused)
def combination_sum(candidates, target):
    """
    Return all combinations that sum up to target.
    Elements can be used unlimited times.
    """
    def gen(ind, curr, total):
        if total == target:
            ans.append(curr.copy())
            return
        if total > target or ind == len(candidates):
            return
        curr.append(candidates[ind])
        gen(ind, curr, total + candidates[ind])
        curr.pop()
        gen(ind + 1, curr, total)

    ans = []
    gen(0, [], 0)
    return ans

print(combination_sum([2, 3, 6, 7], 7))


# Combination Sum II (each number used once)
def combination_sum2(candidates, target):
    """
    Return all unique combinations that sum up to target.
    Each number may be used only once.
    """
    def backtrack(start, target, path):
        if target == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            backtrack(i + 1, target - candidates[i], path + [candidates[i]])

    candidates.sort()
    res = []
    backtrack(0, target, [])
    return res

print(combination_sum2([10, 1, 2, 7, 6, 1, 5], 8))


# Generate Valid Parentheses
def generate_parenthesis(n):
    """
    Generate all combinations of n pairs of valid parentheses.
    """
    def gen(curr, open_count, close_count):
        if len(curr) == 2 * n:
            res.append(curr)
            return
        if open_count < n:
            gen(curr + "(", open_count + 1, close_count)
        if close_count < open_count:
            gen(curr + ")", open_count, close_count + 1)

    res = []
    gen("", 0, 0)
    return res

print(generate_parenthesis(3))


# ------------------ Additional Problems ------------------ #

# Factorial (recursive)
def factorial(n):
    """Calculate factorial of a number recursively."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# Fibonacci (recursive)
def fibonacci(n):
    """Return nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))


# Palindrome Check (recursive)
def is_palindrome(s):
    """Check if a string is palindrome using recursion."""
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))


# Sum of digits (recursive)
def sum_of_digits(n):
    """Return sum of digits of a number recursively."""
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(1234))


# Reverse a string (recursive)
def reverse_string(s):
    """Reverse a string using recursion."""
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))


# Tower of Hanoi
def tower_of_hanoi(n, source, helper, target):
    """Solve Tower of Hanoi problem recursively."""
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, helper)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, helper, source, target)

tower_of_hanoi(3, 'A', 'B', 'C')


# String Permutations
def permute(s):
    """Generate all permutations of a string using recursion."""
    def backtrack(path, used):
        if len(path) == len(s):
            res.append("".join(path))
            return
        for i in range(len(s)):
            if not used[i]:
                used[i] = True
                path.append(s[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

    res = []
    backtrack([], [False] * len(s))
    return res

print(permute("abc"))
# 11. Power of a number using recursion
def power(base, exp):
    """Recursively computes base raised to the power of exp (base^exp)."""
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# 12. Check if a number is a palindrome using recursion
def is_palindrome_num(n, temp=None):
    """Recursively checks if a number is a palindrome."""
    if temp is None:
        temp = n
    if n == 0:
        return 0
    rev = (10 * is_palindrome_num(n // 10, temp)) + (n % 10)
    return rev == temp if n == temp else rev

# 13. Print numbers from 1 to n using recursion
def print_1_to_n(n):
    """Prints numbers from 1 to n recursively."""
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n, end=' ')

# 14. Print numbers from n to 1 using recursion
def print_n_to_1(n):
    """Prints numbers from n to 1 recursively."""
    if n == 0:
        return
    print(n, end=' ')
    print_n_to_1(n - 1)

# 15. Sum of first n natural numbers using recursion
def sum_n(n):
    """Returns the sum of first n natural numbers recursively."""
    if n == 0:
        return 0
    return n + sum_n(n - 1)

# 16. Check if an array is sorted (recursively)
def is_sorted(arr, i=0):
    """Checks recursively if the array is sorted in ascending order."""
    if i == len(arr) - 1:
        return True
    return arr[i] <= arr[i+1] and is_sorted(arr, i+1)

# 17. Find the first index of an element in array using recursion
def first_index(arr, x, i=0):
    """Recursively finds the first index of x in array arr."""
    if i == len(arr):
        return -1
    if arr[i] == x:
        return i
    return first_index(arr, x, i+1)

# 18. Find the last index of an element in array using recursion
def last_index(arr, x, i=0):
    """Recursively finds the last index of x in array arr."""
    if i == len(arr):
        return -1
    rest = last_index(arr, x, i+1)
    if rest != -1:
        return rest
    if arr[i] == x:
        return i
    return -1

# 19. Replace all occurrences of 'pi' in a string with '3.14'
def replace_pi(s):
    """Recursively replaces all occurrences of 'pi' with '3.14'."""
    if len(s) <= 1:
        return s
    if s[:2] == 'pi':
        return '3.14' + replace_pi(s[2:])
    return s[0] + replace_pi(s[1:])

# 20. Remove adjacent duplicates in a string using recursion
def remove_adjacent_duplicates(s):
    """Recursively removes adjacent duplicate characters in a string."""
    if len(s) <= 1:
        return s
    if s[0] == s[1]:
        return remove_adjacent_duplicates(s[1:])
    return s[0] + remove_adjacent_duplicates(s[1:])

