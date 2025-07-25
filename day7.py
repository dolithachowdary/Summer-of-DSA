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
