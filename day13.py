# ============================================================
# DAY 13 - WHILE LOOP & IMPORTANT PROBLEMS
# ============================================================


# 1. While True - Stop when user types exit

while True:
    user_input = input("Type 'exit' to stop the loop: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    print(f"You typed: {user_input}")


# ============================================================
# 2. Print 5 to 0 using while loop
# ============================================================

n = 5

while n >= 0:
    print(n, end=" ")

    n -= 1

print("Outside")

# Output:
# 5 4 3 2 1 0 Outside


# ============================================================
# 3. Print 5 to 10 using while loop
# ============================================================

n = 5

while n <= 10:
    print(n, end=" ")
    n += 1

print("Outside")

# Output:
# 5 6 7 8 9 10 Outside


# ============================================================
# 4. Skip 7 using continue
# ============================================================

n = 5

while n <= 10:

    if n == 7:
        n += 1
        continue

    print(n, end=" ")
    n += 1

else:
    print("Loop Successful")

# Output:
# 5 6 8 9 10 Loop Successful


# ============================================================
# 5. Stop when number 3 comes using break
# ============================================================

n = 5

while n >= 0:

    if n == 3:
        break

    print(n, end=" ")
    n -= 1

else:
    print("Loop Successful")

print()

# Output:
# 5 4


# ============================================================
# 6. Print 1 to 20 using while loop
# ============================================================

n = 1

while n <= 20:
    print(n, end=" ")
    n += 1

print()

# Output:
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20


# ============================================================
# 7. Print even numbers from 1 to 20
# ============================================================

n = 2

while n <= 20:
    print(n, end=" ")
    n += 2

print()

# Output:
# 2 4 6 8 10 12 14 16 18 20


# ============================================================
# 8. Numbers divisible by both 5 and 7 from 1 to 500
# ============================================================

n = 1

while n <= 500:

    if n % 5 == 0 and n % 7 == 0:
        print(n, end=" ")

    n += 1

print()

# Output:
# 35 70 105 140 175 210 245 280 315 350 385 420 455 490


# ============================================================
# 9. Count digits in a number
# ============================================================

n = 123456789

count = 0

while n > 0:
    n = n // 10
    count += 1

print(f"Number of digits in the given number is: {count}")

# Output:
# Number of digits in the given number is: 9


# ============================================================
# 10. Reverse a number
# ============================================================

n = 123456789

temp = abs(n)
rev = 0

while temp > 0:
    last_digit = temp % 10
    rev = rev * 10 + last_digit
    temp //= 10

if n < 0:
    rev = -rev

print(f"Reverse of the given number is {rev}")

# Output:
# Reverse of the given number is 987654321


# ============================================================
# 11. Palindrome number
# ============================================================

n = 12121

temp = abs(n)
rev = 0

while temp > 0:
    last_digit = temp % 10
    rev = rev * 10 + last_digit
    temp //= 10

if n < 0:
    rev = -rev

if rev == n:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Output:
# Palindrome


# ============================================================
# 12. Armstrong number
# ============================================================

n = 153

total_digits = len(str(n))

total = 0
temp = n

while temp > 0:
    last_digit = temp % 10
    total += last_digit ** total_digits
    temp //= 10

if n == total:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# Output:
# Armstrong Number


# ============================================================
# 13. Palindrome string using slicing
# ============================================================

def is_palindrome(text):

    # Convert to lowercase
    # Remove spaces
    cleaned_text = text.lower().replace(" ", "")

    # Compare with reverse
    return cleaned_text == cleaned_text[::-1]


word1 = "Racecar"
word2 = "Python"
phrase = "A nut for a jar of a tuna"

print(f"'{word1}' is a palindrome: {is_palindrome(word1)}")
print(f"'{word2}' is a palindrome: {is_palindrome(word2)}")
print(f"'{phrase}' is a palindrome: {is_palindrome(phrase)}")

# Output:
# 'Racecar' is a palindrome: True
# 'Python' is a palindrome: False
# 'A nut for a jar of a tuna' is a palindrome: True