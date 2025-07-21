# ----------------------------
# 📅 Day 3 – Bit Manipulation & Recursion
# ----------------------------

def binary(a):
    """
    Convert a decimal number to binary using division method.
    
    Parameters:
        a (int): The decimal number.
    
    Returns:
        str: Binary representation as a string.
    
    Example:
        binary(8) → '1000'
    """
    res = ""
    while a:
        res += str(a % 2)
        a = a // 2
    return res[::-1]

print("Decimal to Binary:", binary(8))


def deci(a):
    """
    Convert a binary string to decimal.
    
    Parameters:
        a (str): Binary number in string format.
    
    Returns:
        int: Decimal equivalent.
    
    Example:
        deci('1010') → 10
    """
    res = 0
    a = a[::-1]
    for i in range(len(a)):
        res += int(a[i]) * (2 ** i)
    return res

print("Binary to Decimal:", deci('1010'))


def decitobinary(a):
    """
    Convert a decimal number to binary using bitwise operations.
    
    Parameters:
        a (int): Decimal number.
    
    Returns:
        str: Binary representation.
    
    Example:
        decitobinary(8) → '1000'
    """
    res = ""
    while a:
        res += str(a & 1)
        a = a >> 1
    return res[::-1]

print("Decimal to Binary (Bitwise):", decitobinary(8))


def count_ones(a):
    """
    Count number of 1s in the binary representation of a number.
    
    Parameters:
        a (int): Input number.
    
    Returns:
        int: Number of 1s.
    
    Example:
        count_ones(7) → 3   # binary: 111
    """
    count = 0
    while a:
        if a & 1 == 1:
            count += 1
        a = a >> 1
    return count

print("Count 1's:", count_ones(7))


def count_zeros(a):
    """
    Count number of 0s in the binary representation of a number.
    
    Parameters:
        a (int): Input number.
    
    Returns:
        int: Number of 0s.
    
    Example:
        count_zeros(10) → 2   # binary: 1010
    """
    count = 0
    while a:
        if a & 1 == 0:
            count += 1
        a = a >> 1
    return count

print("Count 0's:", count_zeros(10))


def first_set_bit_right(a):
    """
    Return the position (1-indexed) of the first set bit (1) from the right.
    
    Parameters:
        a (int): Input number.
    
    Returns:
        int: Position of first 1-bit from the right.
    
    Example:
        first_set_bit_right(8) → 4  # binary: 1000
    """
    i = 1
    while a & 1 == 0:
        i += 1
        a = a >> 1
    return i

print("First set bit from right:", first_set_bit_right(8))


def first_set_bit_left(a):
    """
    Return the position (0-indexed) of the first set bit (1) from the left using `bin()`.
    
    Parameters:
        a (int): Input number.
    
    Returns:
        int: Position of first 1-bit from left.
    
    Example:
        first_set_bit_left(8) → 0  # binary: 1000
    """
    b = bin(a)
    for i in range(len(b)):
        if b[i] == '1':
            return i - 2  # subtracting 2 for '0b'
    return -1

print("First set bit from left:", first_set_bit_left(8))


def first_set_bit_left_manual(a):
    """
    Return the position (1-indexed) of the first set bit from the left without using bin().
    
    Parameters:
        a (int): Input number.
    
    Returns:
        int: Position of most significant bit.
    
    Example:
        first_set_bit_left_manual(9) → 4  # binary: 1001
    """
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


def set_ith_bit(a, i):
    """
    Set the i-th bit (0-indexed) of a number to 1.
    
    Parameters:
        a (int): Original number.
        i (int): Bit position to set.
    
    Returns:
        int: Modified number with i-th bit set.
    
    Example:
        set_ith_bit(8, 2) → 12
    """
    mask = 1 << i
    return a | mask

print("Set 2nd bit of 8:", set_ith_bit(8, 2))


def get_ith_bit(a, i):
    """
    Get the value (0 or 1) at the i-th bit (0-indexed) of the number.
    
    Parameters:
        a (int): Input number.
        i (int): Bit position.
    
    Returns:
        int: 1 if bit is set, else 0.
    
    Example:
        get_ith_bit(8, 3) → 1
    """
    mask = 1 << i
    return 1 if mask & a else 0

print("Get 3rd bit of 8:", get_ith_bit(8, 3))


def is_power_of_two(a):
    """
    Check if a number is a power of 2.
    
    Parameters:
        a (int): Input number.
    
    Returns:
        bool: True if power of 2, else False.
    
    Example:
        is_power_of_two(8) → True
        is_power_of_two(10) → False
    """
    return a != 0 and (a & (a - 1)) == 0

print("Is 8 power of 2:", is_power_of_two(8))


def find_unique(arr):
    """
    Find the unique element in an array where all others appear twice.
    
    Parameters:
        arr (list): List of integers.
    
    Returns:
        int: Unique element.
    
    Example:
        find_unique([1,1,2,2,3]) → 3
    """
    res = 0
    for i in arr:
        res ^= i
    return res

print("Unique number in array:", find_unique([1, 1, 5, 2, 3, 4, 2, 3, 4]))


# ----------------------------
# 📌 Recursion Problems
# ----------------------------

def count_digits(a):
    """
    Count the number of digits in an integer using recursion.
    
    Parameters:
        a (int): Input number.
    
    Returns:
        int: Number of digits.
    
    Example:
        count_digits(1234) → 4
    """
    if a == 0:
        return 0
    return 1 + count_digits(a // 10)

print("Count digits (recursion):", count_digits(12345))
