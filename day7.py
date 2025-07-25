"""
Day 7: Advanced Recursion and Backtracking Problems
Includes function-level docstrings and inline comments for better understanding.
"""

def permutations(s):
    """Generate all permutations of a given string."""
    if len(s) == 0:
        return ['']

    result = []
    for i in range(len(s)):
        ch = s[i]
        rest = s[:i] + s[i+1:]
        for perm in permutations(rest):
            result.append(ch + perm)
    return result


def combination_sum(candidates, target):
    """Find all unique combinations of candidates that sum up to target."""
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(list(path))
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result


def n_queens(n):
    """Solve the N-Queens problem for a given n."""
    board = [[0] * n for _ in range(n)]
    result = []

    def is_safe(row, col):
        for i in range(row):
            if board[i][col]:
                return False
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j]:
                return False
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j]:
                return False
        return True

    def solve(row):
        if row == n:
            solution = [''.join(['Q' if c == 1 else '.' for c in r]) for r in board]
            result.append(solution)
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)
    return result


def solve_maze(maze):
    """Solve a maze using backtracking. 1 = open path, 0 = wall."""
    n = len(maze)
    sol = [[0 for _ in range(n)] for _ in range(n)]
    result = []

    def is_safe(x, y):
        return 0 <= x < n and 0 <= y < n and maze[x][y] == 1

    def solve(x, y):
        if x == n - 1 and y == n - 1:
            sol[x][y] = 1
            result.append([row[:] for row in sol])
            sol[x][y] = 0
            return

        if is_safe(x, y):
            sol[x][y] = 1
            solve(x + 1, y)
            solve(x, y + 1)
            sol[x][y] = 0

    solve(0, 0)
    return result


def generate_binary_strings(n):
    """Generate binary strings of length n with no consecutive 1s."""
    result = []

    def backtrack(s):
        if len(s) == n:
            result.append(s)
            return

        backtrack(s + '0')
        if not s or s[-1] == '0':
            backtrack(s + '1')

    backtrack('')
    return result


if __name__ == "__main__":
    # Testing each function
    print("Permutations of 'abc':", permutations("abc"))
    print("Combination sum of [2,3,6,7] to get 7:", combination_sum([2, 3, 6, 7], 7))
    print("N-Queens for n=4:")
    for solution in n_queens(4):
        for row in solution:
            print(row)
        print("--")

    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]
    print("Maze solutions:")
    for sol in solve_maze(maze):
        for row in sol:
            print(row)
        print("--")

    print("Binary strings with no consecutive 1s of length 3:", generate_binary_strings(3))


# 📅 Day 7 - Advanced Backtracking Problems (Extended Set)
from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations that sum to target (elements can repeat).
    """
    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()

    result = []
    backtrack(0, [], 0)
    return result


def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations that sum to target (elements used once).
    """
    candidates.sort()
    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return
        prev = -1
        for i in range(start, len(candidates)):
            if candidates[i] == prev:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, total + candidates[i])
            path.pop()
            prev = candidates[i]

    result = []
    backtrack(0, [], 0)
    return result


def permutations(nums: List[int]) -> List[List[int]]:
    """
    Return all permutations of nums.
    """
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    result = []
    backtrack([], [False]*len(nums))
    return result


def combination_k_sum(k: int, n: int) -> List[List[int]]:
    """
    Find combinations of k numbers (1-9) that sum to n.
    """
    def backtrack(start, path, total):
        if len(path) == k and total == n:
            result.append(path[:])
            return
        for i in range(start, 10):
            if total + i > n:
                break
            path.append(i)
            backtrack(i + 1, path, total + i)
            path.pop()

    result = []
    backtrack(1, [], 0)
    return result


def n_queens(n: int) -> List[List[str]]:
    """
    Solve the N-Queens problem.
    """
    def is_safe(r, c):
        return c not in cols and (r - c) not in neg_diag and (r + c) not in pos_diag

    def backtrack(r):
        if r == n:
            result.append(["".join(row) for row in board])
            return
        for c in range(n):
            if is_safe(r, c):
                board[r][c] = 'Q'
                cols.add(c)
                neg_diag.add(r - c)
                pos_diag.add(r + c)

                backtrack(r + 1)

                board[r][c] = '.'
                cols.remove(c)
                neg_diag.remove(r - c)
                pos_diag.remove(r + c)

    result = []
    board = [["."] * n for _ in range(n)]
    cols = set()
    neg_diag = set()
    pos_diag = set()
    backtrack(0)
    return result


def palindrome_partitioning(s: str) -> List[List[str]]:
    """
    Partition a string such that every substring is a palindrome.
    """
    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(end, path)
                path.pop()

    result = []
    backtrack(0, [])
    return result


def restore_ip_addresses(s: str) -> List[str]:
    """
    Restore valid IP addresses from string of digits.
    """
    def backtrack(start, path):
        if len(path) == 4 and start == len(s):
            result.append(".".join(path))
            return
        if len(path) >= 4:
            return
        for length in range(1, 4):
            if start + length > len(s):
                break
            part = s[start:start+length]
            if (part.startswith('0') and len(part) > 1) or int(part) > 255:
                continue
            backtrack(start + length, path + [part])

    result = []
    backtrack(0, [])
    return result


def generate_abbreviations(word: str) -> List[str]:
    """
    Generate all generalized abbreviations for a word.
    """
    def backtrack(pos, cur, count):
        if pos == len(word):
            if count > 0:
                cur += str(count)
            result.append(cur)
            return
        # Abbreviate this character
        backtrack(pos + 1, cur, count + 1)
        # Keep this character
        backtrack(pos + 1, cur + (str(count) if count > 0 else "") + word[pos], 0)

    result = []
    backtrack(0, "", 0)
    return result

def subset_with_dup(nums: List[int]) -> List[List[int]]:
    """
    Return all possible subsets (the power set) with duplicates removed.
    """
    nums.sort()
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result


# Optional Test Section
if __name__ == "__main__":
    print("Palindrome Partitioning:", palindrome_partitioning("aab"))
    print("Restore IPs:", restore_ip_addresses("25525511135"))
    print("Abbreviations:", generate_abbreviations("word"))
    print("Subsets with Duplicates:", subset_with_dup([1,2,2]))

