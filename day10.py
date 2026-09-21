# =======================================================
# LIST + LOOPS + BREAK + CONTINUE + FOR ELSE
# =======================================================


# 1. Print elements in list with for-each loop

my_list = [4, 3, 2, 5]

for x in my_list:
    print(x)

# Output:
# 4
# 3
# 2
# 5


# ============================================================
# 2. Print elements in list with index-based for loop
# ============================================================

for i in range(len(my_list)):
    print(i, my_list[i])

# Output:
# 0 4
# 1 3
# 2 2
# 3 5


# ============================================================
# 3. Print elements in list with while loop
# ============================================================

i = 0

while i < len(my_list):
    print(i, my_list[i])
    i += 1

# Output:
# 0 4
# 1 3
# 2 2
# 3 5


# ============================================================
# 4. Skip printing even numbers in list
# ============================================================

for x in my_list:
    if x % 2 == 0:
        continue
    print(x)

# Output:
# 3
# 5


# ============================================================
# 5. Skip printing odd numbers in list
# ============================================================

for x in my_list:
    if x % 2 != 0:
        continue
    print(x)

# Output:
# 4
# 2


# ============================================================
# 6. When number 2 comes, stop printing
# ============================================================

for x in my_list:
    if x == 2:
        break
    print(x)

# Output:
# 4
# 3


# ============================================================
# 7. When first odd number comes, stop printing
# ============================================================

for x in my_list:
    if x % 2 != 0:
        break
    print(x)

# Output:
# Nothing is printed
#
# Because the first number 4 is even,
# but the next number 3 is odd.
# So break happens before printing 3.


# ============================================================
# 8. Print numbers from 1 to 10
#    After all numbers are printed, print message
# ============================================================

for i in range(1, 11):
    print(i)
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


# ============================================================
# 9. Print numbers from 1 to 10
#    Skip even numbers
#    After all numbers are printed, print message
# ============================================================

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
else:
    print("All numbers printed")

# Output:
# 1
# 3
# 5
# 7
# 9
# All numbers printed


# ============================================================
# 10. Print numbers from 10 to 1
#     When 5 comes, stop printing
#     If all numbers are printed, print message
# ============================================================

for i in range(10, 0, -1):
    if i == 5:
        break
    print(i)
else:
    print("All numbers printed")

# Output:
# 10
# 9
# 8
# 7
# 6
#
# "All numbers printed" is NOT printed
# because break stopped the loop.