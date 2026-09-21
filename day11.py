# ============================================================
# IMPORTANT PYTHON PROBLEMS
# ============================================================


# 1. Print numbers from 1 to 10

for i in range(1, 11):
    print(i)

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


# ============================================================
# 2. Print even numbers from 5 to 30 and store in a list
# ============================================================

even_numbers = []

for i in range(5, 31):
    if i % 2 == 0:
        print(i)
        even_numbers.append(i)

print("List:", even_numbers)

# Output:
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# 22
# 24
# 26
# 28
# 30
# List: [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]


# ============================================================
# 3. Print odd numbers from 5 to 30 and store in a list
# ============================================================

odd_numbers = []

for i in range(5, 31):
    if i % 2 != 0:
        print(i)
        odd_numbers.append(i)

print("List:", odd_numbers)

# Output:
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19
# 21
# 23
# 25
# 27
# 29
# List: [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]


# ============================================================
# 4. Print numbers divisible by 5 from 1 to 30
# ============================================================

divisible_by_5 = []

for i in range(1, 31):
    if i % 5 == 0:
        print(i)
        divisible_by_5.append(i)

print("List:", divisible_by_5)

# Output:
# 5
# 10
# 15
# 20
# 25
# 30
# List: [5, 10, 15, 20, 25, 30]


# ============================================================
# 5. Print numbers divisible by both 5 and 7 from 1 to 100
# ============================================================

divisible_by_5_and_7 = []

for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
        divisible_by_5_and_7.append(i)

print("List:", divisible_by_5_and_7)

# Output:
# 35
# 70
# List: [35, 70]


# ============================================================
# 6. Sum of numbers from 10 to 25 and store in a list
# ============================================================

numbers_list = []
total_sum = 0

for i in range(10, 26):
    numbers_list.append(i)
    total_sum += i

print("List of numbers:", numbers_list)
print("Sum:", total_sum)

# Output:
# List of numbers: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# Sum: 280


# ============================================================
# 7. Multiplication table of a number
# ============================================================

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Example Input:
# Enter a number: 5

# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50


# ============================================================
# 8. Factorial
# ============================================================

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is {factorial}")

# Example Input:
# Enter a number: 5

# Output:
# Factorial of 5 is 120


# ============================================================
# 9. Fibonacci
# ============================================================

n = int(input("Enter number of terms: "))

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()

# Example Input:
# Enter number of terms: 10

# Output:
# 0 1 1 2 3 5 8 13 21 34


# ============================================================
# 10. Reverse a string
# ============================================================

text = input("Enter a string: ")

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print("Reversed string:", reversed_text)

# Example Input:
# Enter a string: python

# Output:
# Reversed string: nohtyp


# ============================================================
# 11. Count vowels in a string
# ============================================================

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

# Example Input:
# Enter a string: python programming

# Output:
# Number of vowels: 4


# ============================================================
# 12. Count z's and y's in a string
# ============================================================

text = input("Enter a string: ")

count = 0

for char in text:
    if char in "zyZY":
        count += 1

print("Number of z's and y's:", count)

# Example Input:
# Enter a string: lazy zebra

# Output:
# Number of z's and y's: 3


# ============================================================
# 13. Check whether a number is prime or not
# ============================================================

num = int(input("Enter a number: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# Example Input:
# Enter a number: 17

# Output:
# 17 is a prime number