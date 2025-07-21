# ----------------------------
# 📅 Day 3 – Bit Manipulation & Recursion
# ----------------------------

# ✅ Decimal to Binary Number (using division)
def binary(a):
    res = ""
    while a:
        res += str(a % 2)
        a = a // 2
    return res[::-1]

print("Decimal to Binary:", binary(8))


# ✅ Binary to Decimal
def deci(a):
    res = 0
    a = a[::-1]
    for i in range(len(a)):
        res += int(a[i]) * (2 ** i)
    return res

print("Binary to Decimal:", deci('1010'))


# ✅ Decimal to Binary using Bitwise Operator
def decitobinary(a):
    res = ""
    while a:
        res += str(a & 1)
        a = a >> 1
    return res[::-1]

print("Decimal to Binary (Bitwise):", decitobinary(8))


# ✅ Count Number of 1's in Binary Representation
def count_ones(a):
    count = 0
    while a:
        if a & 1 == 1:
            count += 1
        a = a >> 1
    return count

print("Count 1's:", count_ones(7))


# ✅ Count Number of 0's in Binary Representation
def count_zeros(a):
    count = 0
    while a:
        if a & 1 == 0:
            count += 1
        a = a >> 1
    return count

print("Count 0's:", count_zeros(10))


# ✅ First Set Bit from Right (1-indexed)
def first_set_bit_right(a):
    i = 1
    while a & 1 == 0:
        i += 1
        a = a >> 1
    return i

print("First set bit from right:", first_set_bit_right(8))


# ✅ First Set Bit from Left (Using bin())
def first_set_bit_left(a):
    b = bin(a)
    for i in range(len(b)):
        if b[i] == '1':
            return i - 2  # because '0b' prefix
    return -1

print("First set bit from left:", first_set_bit_left(8))


# ✅ First Set Bit from Left (Without bin())
def first_set_bit_left_manual(a):
    count = 0
    temp = a
    while a:
        a = a >> 1
        count += 1
    while temp & 1 == 0:
        temp = temp >> 1
        count -= 1
    return count

print("First set bit (manual):", first_set_bit_left_manual(9))


# ✅ Set i-th Bit to 1
def set_ith_bit(a, i):
    mask = 1 << i
    return a | mask

print("Set 2nd bit of 8:", set_ith_bit(8, 2))


# ✅ Get i-th Bit (Check if 1 or 0)
def get_ith_bit(a, i):
    mask = 1 << i
    return 1 if mask & a else 0

print("Get 3rd bit of 8:", get_ith_bit(8, 3))


# ✅ Check if Number is Power of 2
def is_power_of_two(a):
    return a != 0 and (a & (a - 1)) == 0

print("Is 8 power of 2:", is_power_of_two(8))


# ✅ Find Unique Number using XOR (All others are duplicates)
def find_unique(arr):
    res = 0
    for i in arr:
        res ^= i
    return res

print("Unique number in array:", find_unique([1, 1, 5, 2, 3, 4, 2, 3, 4]))


# ----------------------------
# 📌 Recursion Problems
# ----------------------------

# ✅ Count Digits in Integer using Recursion
def count_digits(a):
    if a == 0:
        return 0
    return 1 + count_digits(a // 10)

print("Count digits (recursion):", count_digits(12345))
