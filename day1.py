# Day 1 - DSA Practice with Strings, Numbers, and Frequency Problems

def uni(a):
    """
    Prints unique (non-repeating) elements in the given list.

    Parameters:
    a (list): A list of integers.

    Example:
    >>> uni([1, 2, 3, 4, 4, 4])
    1
    2
    3
    """
    d = {}
    for i in a:
        d[i] = d.get(i, 0) + 1
    for key, value in d.items():
        if value == 1:
            print(key)


def isprime(c):
    """
    Checks if a number is prime.

    Parameters:
    c (int): The number to check.

    Returns:
    bool: True if prime, False otherwise.

    Example:
    >>> isprime(7)
    True
    """
    if c <= 1:
        return False
    for i in range(2, c):
        if c % i == 0:
            return False
    return True


def vowel(s):
    """
    Counts the number of vowels in a given string.

    Parameters:
    s (str): Input string.

    Returns:
    int: Number of vowels.

    Example:
    >>> vowel('abced')
    2
    """
    v = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for i in s:
        if i in v:
            count += 1
    return count


def ascii_sum(s):
    """
    Calculates a weighted sum of uppercase letters based on their positions in the alphabet.

    Parameters:
    s (str): Uppercase string (e.g., 'ABC').

    Returns:
    int: Weighted sum.

    Example:
    >>> ascii_sum('ABC')
    6  # A=1, B=2, C=3 → 1+2+3
    """
    l = [chr(i) for i in range(65, 91)]
    count = 0
    for i in s:
        count += 1 + l.index(i)
    return count


def to_uppercase_vowels(s):
    """
    Converts all vowels in the string to uppercase, leaves consonants as-is.

    Parameters:
    s (str): Input string.

    Returns:
    str: Modified string.

    Example:
    >>> to_uppercase_vowels('abceik')
    'AbcEIk'
    """
    v = {'a', 'e', 'i', 'o', 'u'}
    a = ''
    for i in s:
        if i in v:
            a += chr(ord(i) - 32)
        else:
            a += i
    return a


def toggle_case(s):
    """
    Toggles the case of each character in the string:
    - Uppercase becomes lowercase.
    - Lowercase becomes uppercase.

    Parameters:
    s (str): Input string.

    Returns:
    str: Case-toggled string.

    Example:
    >>> toggle_case("AbDf")
    'aBdF'
    """
    a = ''
    for i in s:
        if 'A' <= i <= 'Z':
            a += chr(ord(i) + 32)
        else:
            a += chr(ord(i) - 32)
    return a


def zip_and_upper(a, b):
    """
    Zips two strings character by character.
    If one string is longer, appends the remaining characters in uppercase.

    Parameters:
    a (str): First string.
    b (str): Second string.

    Example:
    >>> zip_and_upper('abcd', 'jk')
    'ajbkCD'
    """
    res = ''
    n = min(len(a), len(b))
    for i in range(n):
        res += a[i] + b[i]
    if len(a) > len(b):
        res += a[n:].upper()
    else:
        res += b[n:].upper()
    print(res)


def sub(a, b):
    """
    Checks whether string `b` is a substring of `a`.

    Parameters:
    a (str): The main string.
    b (str): The substring to check.

    Returns:
    bool: True if `b` is a substring of `a`.

    Example:
    >>> sub('abcd', 'bc')
    True
    """
    return b in a


def cir(a, b):
    """
    Checks if one string is a rotation of another.

    Parameters:
    a (str): Original string.
    b (str): Rotated string.

    Example:
    >>> cir('abcd', 'cda')
    True
    """
    r = a + a
    print(b in r)


def first(s):
    """
    Decodes a string of format like '3a4b' → 'aaabbbb'.

    Parameters:
    s (str): Encoded string with digit-character pairs.

    Example:
    >>> first('3a4b')
    'aaabbbb'
    """
    for i in range(0, len(s), 2):
        n = int(s[i])
        print(s[i + 1] * n, end='')


def second(s):
    """
    Decodes a string of format like '10a11b' → 'aaaaaaaaaabbbbbbbbbbb'.

    Parameters:
    s (str): Encoded string with multi-digit numbers.

    Returns:
    str: Decoded string.
    """
    num = ""
    res = ""
    for i in s:
        if i.isdigit():
            num += i
        else:
            res += int(num) * i
            num = ""
    return res


def third(s):
    """
    Decodes a string with number+char(s) groups like '10ab3cd' → 'ababababababababababcdcdcd'.

    Parameters:
    s (str): Encoded string with repeated character groups.

    Returns:
    str: Decoded string.
    """
    res = ""
    num = ""
    a = ""
    i = 0
    while i < len(s):
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        while i < len(s) and s[i].isalpha():
            a += s[i]
            i += 1
        res += int(num) * a
        num = ""
        a = ""
    return res
