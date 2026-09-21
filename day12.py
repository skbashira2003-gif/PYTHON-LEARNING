# ============================================================
# DAY 12 - LIST SLICING & FORMATTING
# ============================================================


# SLICING

numbers = [10, 20, 30, 40, 50, 60]


# 1. Start index 1, stop before index 4
print(numbers[1:4])
# Output: [20, 30, 40]


# 2. Start from beginning, stop before index 3
print(numbers[:3])
# Output: [10, 20, 30]


# 3. Start from index 3 until the end
print(numbers[3:])
# Output: [40, 50, 60]


# 4. Last two elements
print(numbers[-2:])
# Output: [50, 60]


# 5. Every second element
print(numbers[::2])
# Output: [10, 30, 50]


# 6. Reverse the list
print(numbers[::-1])
# Output: [60, 50, 40, 30, 20, 10]


# ============================================================
# STRING FORMATTING - f-strings
# ============================================================

name = "Bashira"
age = 30


# 7. f-string approach (Recommended)
print(f"Hello, my name is {name} and I am {age} years old.")

# Output:
# Hello, my name is Bashira and I am 23 years old.


# 8. .format() approach
print("Hello, my name is {} and I am {} years old.".format(name, age))

# Output:
# Hello, my name is Bashira and I am 23 years old.