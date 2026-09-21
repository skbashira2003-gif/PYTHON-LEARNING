# ============================================================
# DAY 05 - LIST AND TUPLE OPERATIONS
# ============================================================


# ============================================================
# INSERT OPERATIONS
# ============================================================

# Create a list with 3 elements
a = [10, 20, 30]
print(a)
# Output: [10, 20, 30]


# ------------------------------------------------------------
# APPENDING
# ------------------------------------------------------------

# Add 5 types of NON-SEQUENCE elements using append()

a = [10, 20, 30]

a.append(40)              # int
a.append(10.5)            # float
a.append(2 + 3j)          # complex
a.append(True)            # bool
a.append(None)            # None

print(a)
# Output: [10, 20, 30, 40, 10.5, (2+3j), True, None]


# Add 5 types of SEQUENCE elements using append()

a = [10, 20, 30]

a.append("Python")        # string
a.append([1, 2])          # list
a.append((3, 4))          # tuple
a.append(range(1, 4))     # range
a.append("ABC")           # string

print(a)
# Output:
# [10, 20, 30, 'Python', [1, 2], (3, 4), range(1, 4), 'ABC']

# IMPORTANT:
# append() adds the complete element as ONE element.


# ------------------------------------------------------------
# EXTENDING
# ------------------------------------------------------------

# Add 5 types of NON-SEQUENCE elements using extend()

# NOTE:
# extend() requires an iterable.
# So we use single-element containers to demonstrate the types.

a = [10, 20, 30]

a.extend([40])            # int inside list
a.extend([10.5])          # float inside list
a.extend([2 + 3j])        # complex inside list
a.extend([True])          # bool inside list
a.extend([None])          # None inside list

print(a)
# Output:
# [10, 20, 30, 40, 10.5, (2+3j), True, None]


# Add 5 types of SEQUENCE elements using extend()

a = [10, 20, 30]

a.extend("ABC")            # string
a.extend([1, 2])           # list
a.extend((3, 4))           # tuple
a.extend(range(5, 7))      # range
a.extend("XY")             # string

print(a)
# Output:
# [10, 20, 30, 'A', 'B', 'C', 1, 2, 3, 4, 5, 6, 'X', 'Y']

# IMPORTANT:
# extend() adds elements individually.


# ------------------------------------------------------------
# INSERTING
# ------------------------------------------------------------

a = [10, 20, 30]

a.insert(1, 100)
print(a)
# Output: [10, 100, 20, 30]


a = [10, 20, 30]

a.insert(-1, 200)
print(a)
# Output: [10, 20, 200, 30]


a = [10, 20, 30]

a.insert(10000, 300)
print(a)
# Output: [10, 20, 30, 300]


a = [10, 20, 30]

a.insert(-10000, 400)
print(a)
# Output: [400, 10, 20, 30]


# ============================================================
# DELETE OPERATIONS
# ============================================================

a = [1, 2, 1, 3, 4, 1]


# pop element at index 3

element = a.pop(3)

print("Popped element:", element)
print("List:", a)

# Output:
# Popped element: 3
# List: [1, 2, 1, 4, 1]


# pop last element

element = a.pop()

print("Popped element:", element)
print("List:", a)

# Output:
# Popped element: 1
# List: [1, 2, 1, 4]


# remove first 1

a.remove(1)

print("List:", a)

# Output:
# List: [2, 1, 4]


# clear all elements

a.clear()

print("List:", a)

# Output:
# List: []


# ============================================================
# UPDATE OPERATIONS
# ============================================================

# Sort ascending

a = [3, 2, 1, 5, 4]

a.sort()

print(a)
# Output: [1, 2, 3, 4, 5]


# Sort descending

a = [3, 2, 1, 5, 4]

a.sort(reverse=True)

print(a)
# Output: [5, 4, 3, 2, 1]


# Reverse the list

a = [3, 2, 1, 5, 4]

a.reverse()

print(a)
# Output: [4, 5, 1, 2, 3]


# ============================================================
# READ OPERATIONS
# ============================================================

a = [1, 2, 1, 3, 1, 2]

# Find count of 1

print(a.count(1))
# Output: 3


# Find count of 2

print(a.count(2))
# Output: 2


# Find index of 1 from start

print(a.index(1))
# Output: 0


# Find index of 1 from 2nd index

print(a.index(1, 2))
# Output: 2


# Find index of 1 from 5th index

# There is no 1 at index 5 or after it.
# So index() gives ValueError.

# print(a.index(1, 5))
# Output: ValueError


# ============================================================
# TUPLE OPERATIONS
# ============================================================

t = (1, 2, 1, 3, 1, 2)


# Find count of 1

print(t.count(1))
# Output: 3


# Find count of 2

print(t.count(2))
# Output: 2


# Find index of 1 from start

print(t.index(1))
# Output: 0


# Find index of 1 from 2nd index

print(t.index(1, 2))
# Output: 2


# Find index of 1 from 5th index

# No 1 exists from index 5 onwards.
# So index() gives ValueError.

# print(t.index(1, 5))
# Output: ValueError
