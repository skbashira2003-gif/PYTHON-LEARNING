#FUNCTIONS

# 1. Function for Palindrome Number

def palindrome_number(n):
    original = n
    reverse = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    if original == reverse:
        return "Palindrome"
    else:
        return "Not a Palindrome"


print(palindrome_number(121))       # Output: Palindrome
print(palindrome_number(123))       # Output: Not a Palindrome


# 2. Function for Palindrome String

def palindrome_string(s):
    reverse = ""

    for char in s:
        reverse = char + reverse

    if s == reverse:
        return "Palindrome"
    else:
        return "Not a Palindrome"


print(palindrome_string("madam"))    # Output: Palindrome
print(palindrome_string("hello"))    # Output: Not a Palindrome


# 3. Function to Check Prime Number

def check_prime(n):
    if n < 2:
        return "Not Prime"

    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"

    return "Prime"


print(check_prime(7))                # Output: Prime
print(check_prime(10))               # Output: Not Prime


# 4. Function to Reverse a String

def reverse_string(s):
    reverse = ""

    for char in s:
        reverse = char + reverse

    return reverse


print(reverse_string("Python"))      # Output: nohtyP
print(reverse_string("Hello"))       # Output: olleH


# 5. Function to Find Factorial

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print(factorial(5))                  # Output: 120
print(factorial(6))                  # Output: 720


# 6. Function to Find Fibonacci

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")

        a, b = b, a + b

    print()


fibonacci(10)                        # Output: 0 1 1 2 3 5 8 13 21 34


# 7. Function to Count Number of Digits

def count_digits(n):
    n = abs(n)

    if n == 0:
        return 1

    count = 0

    while n > 0:
        n //= 10
        count += 1

    return count


print(count_digits(12345))           # Output: 5
print(count_digits(987))             # Output: 3


# 8. Function to Find Armstrong Number

def check_armstrong(n):
    original = n
    digits = len(str(n))
    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == original:
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"


print(check_armstrong(153))          # Output: Armstrong Number
print(check_armstrong(123))          # Output: Not an Armstrong Number

# LAMBDA FUNCTIONS
# ============================================================


# 1. Lambda function to return square of x

square = lambda x: x ** 2

print(square(5))
# Output: 25


# ============================================================
# 2. Lambda function to return sum of x and y
# ============================================================

add = lambda x, y: x + y

print(add(10, 20))
# Output: 30


# ============================================================
# 3. Lambda function to return second element
# ============================================================

second = lambda sequence: sequence[1]

print(second([10, 20, 30, 40]))
# Output: 20

print(second("Python"))
# Output: y


# ============================================================
# 4. Lambda function to return sum of a list
# ============================================================

total = lambda numbers: sum(numbers)

print(total([10, 20, 30, 40]))
# Output: 100
check = lambda n: "Even" if n % 2 == 0 else "Odd"

print(check(4))
# Output: Even

print(check(7))
# Output: Odd


#LAMBDA WITH MAP()

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)
# Output: [1, 4, 9, 16, 25]


#LAMBDA WITH FILTER()

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
# Output: [2, 4, 6]


#LAMBDA WITH SORTED()

students = [("Ravi", 80), ("Bashira", 95), ("Ali", 75)]

result = sorted(students, key=lambda x: x[1])

print(result)
# Output: [('Ali', 75), ('Ravi', 80), ('Bashira', 95)]


#LAMBDA - FIND MAXIMUM

maximum = lambda a, b: a if a > b else b

print(maximum(10, 20))
# Output: 20