# Day 10: Matrices and Prime Numbers

# 1. Count Primes (Naive Method)
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def countPrimesNaive(n):
    count = 0
    for i in range(2, n):
        if isPrime(i):
            count += 1
    return count

print("Naive Prime Count (below 7):", countPrimesNaive(7))  # Output: 3


# 2. Count Primes using Sieve of Eratosthenes (Efficient)
# TC: O(n * log(log n))
def countPrimesSieve(n):
    if n < 2:
        return 0
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i*i, n, i):
                prime[j] = False
    return sum(prime)

print("Sieve Prime Count (below 100):", countPrimesSieve(100))  # Output: 25


# 3. Search an element in a sorted 2D matrix (starts top-right)
def search2DMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    row = 0
    col = m - 1
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False

mat = [[1, 2, 3, 4], [2, 3, 4, 5]]
tar = 5
print("Element Found in Matrix:", search2DMatrix(mat, tar))


# 4. Rotate matrix by 90 degrees (extra space)
def rotate90ExtraSpace(mat):
    n = len(mat)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = mat[i][j]
    return result

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Rotated Matrix (Extra Space):")
for row in rotate90ExtraSpace(mat):
    print(row)


# 5. Rotate matrix by 90 degrees (in-place)
def rotate90InPlace(mat):
    n = len(mat)
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    # Reverse each row
    for row in mat:
        row.reverse()
    return mat

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Rotated Matrix (In-place):")
for row in rotate90InPlace(mat):
    print(row)


# 6. Sum of diagonals in a matrix
def sumDiagonals(mat):
    n = len(mat)
    main_diag = 0
    sec_diag = 0
    for i in range(n):
        main_diag += mat[i][i]
        if i != n - i - 1:  # Avoid double counting the center
            sec_diag += mat[i][n - i - 1]
    return [main_diag, sec_diag]

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Diagonal Sums:", sumDiagonals(mat))  # Output: [15, 15]


# 7. Transpose of a matrix
def transpose(mat):
    n = len(mat)
    m = len(mat[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][i] = mat[i][j]
    return result

mat = [[1, 2], [3, 4], [5, 6]]
print("Transpose:")
for row in transpose(mat):
    print(row)


# 8. Spiral traversal of a matrix
def spiralOrder(matrix):
    res = []
    if not matrix:
        return res
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1): res.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1): res.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1): res.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1): res.append(matrix[i][left])
            left += 1
    return res

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Spiral Order:", spiralOrder(mat))  # Output: [1,2,3,6,9,8,7,4,5]


# 9. Count primes in a matrix
def countMatrixPrimes(mat):
    count = 0
    for row in mat:
        for val in row:
            if isPrime(val):
                count += 1
    return count

mat = [[2, 4, 5], [6, 7, 9], [11, 13, 14]]
print("Prime Count in Matrix:", countMatrixPrimes(mat))  # Output: 5

