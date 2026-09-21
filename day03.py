# ============================================================
# DAY 03 - OPERATORS
# ============================================================


# =========================
# 1. ARITHMETIC OPERATORS
# =========================

print(10 + 5 * 2)
# Output: 20

print(2 ** 3 ** 2)
# Output: 512

print(10 // 3)
# Output: 3

print(10 % 3)
# Output: 1

print(5 / 2)
# Output: 2.5

print([1, 2, 3] + [4, 5, 6])
# Output: [1, 2, 3, 4, 5, 6]

print((1, 2, 3) + (4, 5, 6))
# Output: (1, 2, 3, 4, 5, 6)

# Set + Set is NOT supported
# print({1, 2, 3} + {4, 5, 6})
# Output: TypeError

print([1, 2, 3] * 4)
# Output: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

print(*[1, 2, 43])
# Output: 1 2 43

# List + Tuple is NOT supported
# print([1, 2, 3] + (1, 2, 3))
# Output: TypeError

# List + String is NOT supported
# print([1, 2, 3] + 'dog')
# Output: TypeError


# ====================================
# 2. RELATIONAL AND LOGICAL OPERATORS
# ====================================

print(10 > 5 and 20 < 30)
# Output: True

print(10 > 20 and 5 < 10)
# Output: False

print(not 1 == 1)
# Output: False

print(1 < 2 < 3)
# Output: True

print(1 > 2 > 3)
# Output: False

print('abc' > 'def')
# Output: False

print([1, 2, 3] < [1, 3, 4])
# Output: True


# ==================================
# 3. ASSIGNMENT AND WALRUS OPERATOR
# ==================================

# Normal assignment
a = 10
print(a)
# Output: 10

# NOTE:
# print(a=10)
# This gives TypeError because print() does not use
# assignment in this way.

# Walrus operator :=
print(a := 10)
# Output: 10

# Walrus operator inside if
if (n := 34) > 10:
    print(n)
# Output: 34


# ===================================
# 4. IDENTITY AND EQUALITY OPERATORS
# ===================================

# LIST
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
# Output: True

print(a is b)
# Output: False


# STRING
a = 'abc'
b = 'abc'

print(a == b)
# Output: True

print(a is b)
# Output: True
# Note: Python may reuse the same string object.


# TUPLE
a = (1, 2, 3)
b = (1, 2, 3)

print(a == b)
# Output: True

print(a is b)
# Output: True
# Note: Python may reuse the same immutable tuple object.


# ========================
# 5. MEMBERSHIP OPERATORS
# ========================

a = [1, 2, 3, 4, 5]

print(6 in a)
# Output: False

print(6 not in a)
# Output: True

print('abc' in 'abcde')
# Output: True
