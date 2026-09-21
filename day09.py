# ============================================================
# DAY 09 - FOR LOOP, BREAK, CONTINUE & FOR-ELSE
# ============================================================


# TASK 1
# Print elements in list with for-each loop

numbers = [4, 3, 2, 5, 6]


for x in numbers:
    print(x)

# Output:
# 4
# 3
# 2
# 5
# 6


# =================================================
# TASK 2
# Print elements in list with index-based for loop
# ==================================================

numbers = [4, 3, 2, 5, 6]

for x in range(len(numbers)):
    print(numbers[x])

# Output:
# 4
# 3
# 2
# 5
# 6


# ======================================
# TASK 3
# Skip printing even numbers in list
# ======================================

numbers = [4, 3, 2, 5, 6]

for x in numbers:
    if x % 2 == 0:
        continue
    print(x, end=" ")

print()

# Output:
# 3 5


# =================================
# TASK 4
# Skip printing odd numbers in list
# =================================

numbers = [4, 3, 2, 5, 6]

for x in numbers:
    if x % 2 != 0:
        continue
    print(x, end=" ")

print()

# Output:
# 4 2 6


# ======================================
# TASK 5
# When number 2 comes, stop printing
# =======================================

numbers = [4, 3, 2, 5, 6]

for x in numbers:
    if x == 2:
        break
    print(x)

# Output:
# 4
# 3


# =============================================
# TASK 6
# When first odd number comes, stop printing
# =============================================

numbers = [4, 3, 2, 5, 6]

for x in numbers:
    if x % 2 != 0:
        break
    print(x)

# Output:
# 4


# =================================================
# TASK 7
# Print numbers from 1 to 10
# After all numbers are printed, print message
# ================================================

for x in range(1, 11):
    print(x)
else:
    print("All numbers printed")

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# All numbers printed


# =================================
# TASK 8
# Print numbers from 1 to 10
# Skip even numbers
# ==================================

for x in range(1, 11):
    if x % 2 == 0:
        continue
    print(x)
else:
    print("All numbers printed")

# Output:
# 1
# 3
# 5
# 7
# 9
# All numbers printed


# ==============================
# TASK 9
# Print numbers from 10 to 1
# When 5 comes, stop printing
# =============================

for x in range(10, 0, -1):
    if x == 5:
        break
    print(x)

# Output:
# 10
# 9
# 8
# 7
# 6


# =================================
# TASK 10
# Skip even numbers from 0 to 9
# =================================

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9


# ============================
#TASK 11
# Skip numbers divisible by 3
# =============================
for i in range(10):
    if i % 3 == 0:
        continue
    print(i)

# Output:
# 1
# 2
# 4
# 5
# 7
# 8


# =======================================
# TASK 12
# When number 3 comes, stop printing
# =======================================
for i in range(1, 5):
    if i == 3:
        break
    print(i)

# Output:
# 1
# 2


# ============================================================
# TASK 13
# When first number divisible by 4 comes, stop printing
# ============================================================

for i in range(1, 10):
    if i % 4 == 0:
        break
    print(i)

# Output:
# 1
# 2
# 3


# =======================
# TASK 14
# for-else with break
# =======================

numbers = [4, 3, 2, 5, 6]

for x in numbers:
    if x == 10:
        break
    print(x)
else:
    print("Number not found")

# Output:
# 4
# 3
# 2
# 5
# 6
# Number not found