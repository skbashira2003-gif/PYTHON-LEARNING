# ============================================================
# DAY 17 - LIST COMPREHENSIONS AND GENERATORS
# ============================================================


# 1. LIST COMPREHENSION
list_comp = [x ** 2 for x in range(10)]
print(list_comp)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 2. DICTIONARY COMPREHENSION
dict_comp = {x: x ** 2 for x in range(10)}
print(dict_comp)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


# 3. LIST COMPREHENSION WITH IF CONDITION
list_comp_if_even = [
    x ** 2 for x in range(10) if x % 2 == 0
]

print(list_comp_if_even)
# Output: [0, 4, 16, 36, 64]


# 4. LIST COMPREHENSION WITH IF-ELSE
list_comp_if_else_even_odd = [
    x ** 2 if x % 2 == 0 else x ** 3
    for x in range(10)
]

print(list_comp_if_else_even_odd)
# Output: [0, 1, 4, 27, 16, 125, 36, 343, 64, 729]


# 5. LIST COMPREHENSION WITH NESTED FOR LOOP
matrix = [[1, 2], [3, 4], [5, 6]]

flattened = [num for row in matrix for num in row]

print(flattened)
# Output: [1, 2, 3, 4, 5, 6]


# ============================================================
# GENERATORS
# ============================================================


# 6. GENERATOR FUNCTION USING YIELD

def my_generator(max_limit):
    current = 1

    while current <= max_limit:
        yield current
        current += 1


# 7. ITERATING GENERATOR USING FOR LOOP

print("Iterating with a for loop:")

for num in my_generator(3):
    print(num)

# Output:
# Iterating with a for loop:
# 1
# 2
# 3


# 8. GENERATOR USING next()

print("\nStepping through manually:")

gen_instance = my_generator(2)

print(next(gen_instance))  # Output: 1
print(next(gen_instance))  # Output: 2