"""Arithmetic Operators"""
x = 10
y = 3

# Addition
print(x + y)  # Output: 13

# Subtraction
print(x - y)  # Output: 7

# Multiplication
print(x * y)  # Output: 30

# Division
print(x / y)  # Output: 3.3333...

# Modulus (remainder of division)
print(x % y)  # Output: 1

# Exponentiation (power)
print(x ** y)  # Output: 1000

# Floor Division (quotient without the remainder)
print(x // y)  # Output: 3


'''Python Assignment Operators:'''
x = 5

# Add and assign
x += 3  # Same as x = x + 3
print(x)  # Output: 8

# Subtract and assign
x -= 2  # Same as x = x - 2
print(x)  # Output: 6

# Multiply and assign
x *= 2  # Same as x = x * 2
print(x)  # Output: 12

# Divide and assign
x /= 3  # Same as x = x / 3
print(x)  # Output: 4.0

# Modulus and assign
x %= 3  # Same as x = x % 3
print(x)  # Output: 1.0

# Exponentiation and assign
x **= 2  # Same as x = x ** 2
print(x)  # Output: 1.0

# Floor division and assign
x = 10
x //= 3  # Same as x = x // 3
print(x)  # Output: 3

'''Python Comparison Operators:'''
x = 10
y = 3

# Equal to
print(x == y)  # Output: False

# Not equal to
print(x != y)  # Output: True

# Greater than
print(x > y)  # Output: True

# Less than
print(x < y)  # Output: False

# Greater than or equal to
print(x >= y)  # Output: True

# Less than or equal to
print(x <= y)  # Output: False


'''Python Logical Operators:'''
x = 5
y = 10

# AND (both conditions must be true)
print(x < 6 and y > 5)  # Output: True

# OR (one condition must be true)
print(x < 6 or y < 5)  # Output: True

# NOT (reverses the result)
print(not(x < 6 and y > 5))  # Output: False

'''Python Identity Operators:'''
x = [1, 2, 3]
y = [1, 2, 3]
z = x

# is (checks if two variables point to the same object)
print(x is z)  # Output: True
print(x is y)  # Output: False

# is not (checks if two variables do not point to the same object)
print(x is not y)  # Output: True

'''Python Membership Operators:'''
x = [1, 2, 3]

# in (checks if a value is in a sequence)
print(2 in x)  # Output: True

# not in (checks if a value is not in a sequence)
print(4 not in x)  # Output: True

'''Python Bitwise Operators:'''
x = 5  # 101 in binary
y = 3  # 011 in binary

# AND
print(x & y)  # Output: 1 (001 in binary)

# OR
print(x | y)  # Output: 7 (111 in binary)

# XOR
print(x ^ y)  # Output: 6 (110 in binary)

# NOT
print(~x)  # Output: -6 (inverts bits)

# Left Shift
print(x << 1)  # Output: 10 (1010 in binary)

# Right Shift
print(x >> 1)  # Output: 2 (10 in binary)


'''Python Operator Precedence:'''
# Example 1: Parentheses first
print((6 + 3) - (6 + 3))  # Output: 0

# Example 2: Exponentiation before multiplication
print(2 + 3 * 2 ** 2)  # Output: 14 (since 2**2 is done first)

# Example 3: Left to right for equal precedence
print(5 + 4 - 7 + 3)  # Output: 5
