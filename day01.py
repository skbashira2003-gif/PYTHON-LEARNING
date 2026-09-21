
# ============================
# TASK 1: TOKENS & STATEMENTS
# ============================

name = "Bashira"
age = 23
city = "Guntur"

print("Name:", name)   # Output: Name: Bashira
print("Age:", age)     # Output: Age: 23
print("City:", city)   # Output: City: Guntur

#=======================
# TASK 2: IDENTIFIERS
# ======================

student_name = "Bashira"
student_age = 23
student_marks = 65

print("Student Name:", student_name)    # Output: Student Name: Bashira
print("Student Age:", student_age)      # Output: Student Age: 23
print("Student Marks:", student_marks)  # Output: Student Marks: 65

# student-name = "Bashira"
# Invalid because '-' is not allowed in Python identifiers.
# ===============================
# TASK 3: SINGLE-LINE COMMENTS
# ===============================

# Stores the student's name
name = "Bashira"

# Stores the student's age
age = 23

print("Name:", name)  # Output: Name: Bashira
print("Age:", age)    # Output: Age: 23

# =============================
# TASK 4: MULTI-LINE COMMENTS
# =============================

# This program prints
# three messages about
# learning Python.

print("Welcome to Python")              # Output: Welcome to Python
print("I am learning programming")      # Output: I am learning programming
print("Python is easy to learn")        # Output: Python is easy to learn

# ===================
# TASK 5: VARIABLES
# ===================

name = "Bashira"
age = 23
height = 5.4
is_student = True

print("Name:", name)              # Output: Name: Bashira
print("Age:", age)                # Output: Age: 23
print("Height:", height)          # Output: Height: 5.4
print("Is Student:", is_student)  # Output: Is Student: True

# =============================
# TASK 6: MULTIPLE ASSIGNMENT
# =============================

name, age, city = "Bashira", 23, "Guntur"

print("Name:", name)   # Output: Name: Bashira
print("Age:", age)     # Output: Age: 23
print("City:", city)   # Output: City: Guntur

# ======================
# TASK 7: REASSIGNMENT
# ======================

age = 23

print("Current Age:", age)  # Output: Current Age: 23

age = 24

print("New Age:", age)      # Output: New Age: 24

# ============================
# TASK 8: SWAPPING VARIABLES
# ============================

a = 10
b = 20

print("Before:", a, b)  # Output: Before: 10 20

a, b = b, a

print("After:", a, b)   # Output: After: 20 10

# =============================
# TASK 9: DELETING VARIABLES
# =============================

name = "Bashira"

print("Name:", name)  # Output: Name: Bashira

del name

# print(name)
# Output: NameError: name 'name' is not defined


# ======================
# TASK 10: KEYWORDS
# ======================

import keyword

print("Python Keywords:", keyword.kwlist)
# Output: Python Keywords: [Python keyword list]

print("Total Number of Keywords:", len(keyword.kwlist))
# Output: Total Number of Keywords: 35