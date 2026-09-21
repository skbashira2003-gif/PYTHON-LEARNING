 #=============================================================
# DAY 14 - NESTED LOOPS
# ============================================================

# 1. Nested loops

# Outer loop
colors = ["red", "green", "blue"]

# Inner loop
items = ["apple", "banana", "pencil"]

for color in colors:
    for item in items:
        print(color, item)

# Output:
# red apple
# red banana
# red pencil
# green apple
# green banana
# green pencil
# blue apple
# blue banana
# blue pencil

# ============================================================
# 2. Matrix Traversal - Row-wise
# ============================================================

matrix = [
    [4, 5, 6],
    [1, 2, 3],
    [7, 8, 9]
]

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        print(matrix[r][c], end=" ")
    print()

# Output:
# 4 5 6
# 1 2 3
# 7 8 9


print()

# ============================================================
# 3. Matrix Traversal - Column-wise
#    Works for a square matrix
# ============================================================

for c in range(len(matrix[0])):
    for r in range(len(matrix)):
        print(matrix[r][c], end=" ")
    print()

# Output:
# 4 1 7
# 5 2 8
# 6 3 9