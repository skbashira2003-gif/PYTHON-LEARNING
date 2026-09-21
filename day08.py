# ============================================================
# PYTHON CONDITIONAL STATEMENTS - PRACTICE
# ============================================================


# ============================================================
# TASK 1 - HackerRank: If-Else
# ============================================================

# Test value
n = 3

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

# Output:
# Weird


# ============================================================
# TASK 2 - HackerRank: Write a Function - Leap Year
# ============================================================

def is_leap(year):

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(is_leap(2024))

# Output:
# True


# ============================================================
# TASK 3 - Day Name Using match-case
# ============================================================

n = 3

match n:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid day number")

# Output:
# Tuesday


# ============================================================
# TASK 4 - Day Name Using if-elif-else
# ============================================================

n = 5

if n == 1:
    print("Sunday")
elif n == 2:
    print("Monday")
elif n == 3:
    print("Tuesday")
elif n == 4:
    print("Wednesday")
elif n == 5:
    print("Thursday")
elif n == 6:
    print("Friday")
elif n == 7:
    print("Saturday")
else:
    print("Invalid day number")

# Output:
# Thursday