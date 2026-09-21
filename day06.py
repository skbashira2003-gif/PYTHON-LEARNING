# ============================================================
# DAY 06 - SET METHODS AND DICTIONARY METHODS
# ============================================================


# =============
# SET METHODS
# =============
# Create an empty dictionary and print its type

k = {}

print(type(k))
# Output: <class 'dict'>


# Create an empty set and print its type

k = set()

print(type(k))
# Output: <class 'set'>

# =============
# ADD METHOD
# =============
# Create an empty set

k = set()

# Add elements using add()

k.add(2002)              # int
k.add(20.02)             # float
k.add(20 + 20j)          # complex
k.add(True)              # bool
k.add(None)              # NoneType

print(k)
# Output: Order may vary because set is unordered.


# Add sequence elements using add()

k.add("Bashira")         # string
k.add((4, 5, 6))         # tuple
k.add(range(1, 4))       # range

# List and dictionary cannot be added directly because
# they are unhashable.
#
# k.add([1, 2, 3])       # TypeError
# k.add({1: 2, 2: 3})    # TypeError

print(k)
# Output: Order may vary.


# ===============
# UPDATE METHOD
# ===============
k = set()

# update() requires an iterable.

k.update("ABC")
k.update(range(1, 4))
k.update({4, 5, 6})
k.update((7, 8, 9))
k.update([10, 11, 12])

print(k)
# Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 'A', 'B', 'C'}
# Order may vary.


# NOTE:
# update() cannot directly accept non-iterable values.

# k.update(2002)          # TypeError
# k.update(20.02)         # TypeError
# k.update(20 + 20j)      # TypeError


# =================
# POP METHOD
# =================
print(k)
# Output: Set elements

element = k.pop()

print("Removed element:", element)
print("Set after pop:", k)

# Output:
# Removed element: One element from the set
# Set after pop: Remaining elements
# NOTE: Which element is removed is not guaranteed.

#================
# REMOVE METHOD
#================
k = {"a", "b", "c", "d"}

k.remove("a")

print(k)
# Output: {'b', 'c', 'd'}
# Order may vary.


# If element does not exist, remove() gives KeyError.

# k.remove("z")
# Output: KeyError


# ==================
# DISCARD METHOD
# ==================

k = {"a", "b", "c", "d"}

k.discard("a")

print(k)
# Output: {'b', 'c', 'd'}

# discard() does NOT give an error for a missing element.

k.discard("z")

print(k)
# Output: {'b', 'c', 'd'}


# ================
# CLEAR METHOD
# ================

k.clear()

print(k)
# Output: set()


# =================
# SET OPERATIONS
# =================

s = {1, 2, 3, 4}
l = {3, 4, 5, 6}

# NOTE:
# l is a SET here, not a list.


# UNION

print(s.union(l))
# Output: {1, 2, 3, 4, 5, 6}


# INTERSECTION

print(s.intersection(l))
# Output: {3, 4}


# DIFFERENCE

print(s.difference(l))
# Output: {1, 2}


# SYMMETRIC DIFFERENCE

print(s.symmetric_difference(l))
# Output: {1, 2, 5, 6}


# ===================
# SET OPERATORS
# ===================

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1 | s2)
# Output: {1, 2, 3, 4, 5, 6}

print(s1 & s2)
# Output: {3, 4}

print(s1 - s2)
# Output: {1, 2}

print(s1 ^ s2)
# Output: {1, 2, 5, 6}


# =======================
# DICTIONARY METHODS
# =======================

# Create an empty dictionary

d = {}


# ===========================================
# UPDATE DICTIONARY WITH ANOTHER DICTIONARY
# ===========================================

d.update({1: "a", 2: "b"})

print(d)
# Output: {1: 'a', 2: 'b'}


# ===============================
# UPDATE DICTIONARY WITH A LIST
# ===============================

d.update([[3, "c"], [4, "d"]])

print(d)
# Output: {1: 'a', 2: 'b', 3: 'c', 4: 'd'}


# ===============================
# UPDATE DICTIONARY WITH A TUPLE
# ===============================

d.update(((5, "e"), (6, "f")))

print(d)
# Output: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}


# ===============================
# UPDATE DICTIONARY WITH A SET
# ==============================

d.update({(7, "g"), (8, "h")})

print(d)
# Output: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
# Order may vary.


# =============
# POP METHOD
# =============

d = {1: "a", 2: "b", 3: "c", 4: "d"}

element = d.pop(4)

print("Removed value:", element)
print("Dictionary:", d)

# Output:
# Removed value: d
# Dictionary: {1: 'a', 2: 'b', 3: 'c'}


# Key 100 does not exist.
# d.pop(100)
# Output: KeyError


# If key does not exist, return 'z'

print(d.pop(100, "z"))
# Output: z


# ================
# POPITEM METHOD
# ================

d = {1: "a", 2: "b", 3: "c", 4: "d"}

element = d.popitem()

print("Removed pair:", element)
print("Dictionary:", d)

# Output:
# Removed pair: (4, 'd')
# Dictionary: {1: 'a', 2: 'b', 3: 'c'}


# =============
# CLEAR METHOD
# =============
d.clear()

print(d)
# Output: {}


# ============
# GET METHOD
# ============

d = {1: "a", 2: "b", 3: "c", 4: "d"}

print(d.get(4))
# Output: d


# Key 100 does not exist

print(d.get(100))
# Output: None


# If key does not exist, return 'z'

print(d.get(100, "z"))
# Output: z


# ===================
# SETDEFAULT METHOD
# ===================

print(d.setdefault(4))
# Output: d


# Key 100 does not exist.
# setdefault() adds the key with value None.

print(d.setdefault(100))
# Output: None

print(d)
# Output: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 100: None}


# Key 101 does not exist.
# Add key 101 with value 'z'

print(d.setdefault(101, "z"))
# Output: z

print(d)
# Output: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 100: None, 101: 'z'}


# ============
# KEYS METHOD
# ============

a = d.keys()

print(a)
# Output: dict_keys([1, 2, 3, 4, 100, 101])

print(type(a))
# Output: <class 'dict_keys'>


# ==============
# VALUES METHOD
# ==============

b = d.values()

print(b)
# Output: dict_values(['a', 'b', 'c', 'd', None, 'z'])

print(type(b))
# Output: <class 'dict_values'>


# ==============
# ITEMS METHOD
# ==============

c = d.items()

print(c)
# Output: dict_items([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (100, None), (101, 'z')])

print(type(c))
# Output: <class 'dict_items'>

