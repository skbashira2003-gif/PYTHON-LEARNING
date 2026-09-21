# =====================
# DAY 02 - DATA TYPES
# =====================

# 1. INTEGER (int)
age = 23
print("Age:", age)
print("Type:", type(age))
# Output:
# Age: 23
# Type: <class 'int'>


# 2. FLOAT (float)
height = 5.4
print("Height:", height)
print("Type:", type(height))
# Output:
# Height: 5.4
# Type: <class 'float'>


# 3. COMPLEX (complex)
number = 3 + 4j
print("Complex Number:", number)
print("Type:", type(number))
# Output:
# Complex Number: (3+4j)
# Type: <class 'complex'>


# 4. BOOLEAN (bool)
is_student = True
print("Is Student:", is_student)
print("Type:", type(is_student))
# Output:
# Is Student: True
# Type: <class 'bool'>


# 5. NONE TYPE (NoneType)
value = None
print("Value:", value)
print("Type:", type(value))
# Output:
# Value: None
# Type: <class 'NoneType'>


# 6. STRING (str)
name = "Bashira"
print("Name:", name)
print("Type:", type(name))
# Output:
# Name: Bashira
# Type: <class 'str'>


# 7. RANGE (range)
numbers = range(1, 6)
print("Range:", numbers)
print("Type:", type(numbers))
# Output:
# Range: range(1, 6)
# Type: <class 'range'>


# 8. LIST (list)
marks = [65, 70, 80]
print("Marks:", marks)
print("Type:", type(marks))
# Output:
# Marks: [65, 70, 80]
# Type: <class 'list'>


# 9. TUPLE (tuple)
cities = ("Guntur", "Hyderabad", "Chennai")
print("Cities:", cities)
print("Type:", type(cities))
# Output:
# Cities: ('Guntur', 'Hyderabad', 'Chennai')
# Type: <class 'tuple'>


# 10. SET (set)
colors = {"Red", "Green", "Blue"}
print("Colors:", colors)
print("Type:", type(colors))
# Output:
# Colors: {'Red', 'Green', 'Blue'}
# Type: <class 'set'>


# 11. DICTIONARY (dict)
student = {
    "name": "Bashira",
    "age": 23,
    "marks": 65
}
print("Student:", student)
print("Type:", type(student))
# Output:
# Student: {'name': 'Bashira', 'age': 23, 'marks': 65}
# Type: <class 'dict'>


# =================
# TYPE CONVERSION
# =================

# 1. INT TO FLOAT
num1 = 10
result1 = float(num1)

print("Int:", num1)
print("Float:", result1)
print("Type:", type(result1))
# Output:
# Int: 10
# Float: 10.0
# Type: <class 'float'>


# 2. FLOAT TO INT
num2 = 10.5
result2 = int(num2)

print("Float:", num2)
print("Int:", result2)
print("Type:", type(result2))
# Output:
# Float: 10.5
# Int: 10
# Type: <class 'int'>


# 3. INT TO STRING
num3 = 100
result3 = str(num3)

print("Int:", num3)
print("String:", result3)
print("Type:", type(result3))
# Output:
# Int: 100
# String: 100
# Type: <class 'str'>


# 4. STRING TO INT
num4 = "200"
result4 = int(num4)

print("String:", num4)
print("Int:", result4)
print("Type:", type(result4))
# Output:
# String: 200
# Int: 200
# Type: <class 'int'>


# 5. LIST TO TUPLE
list1 = [10, 20, 30]
result5 = tuple(list1)

print("List:", list1)
print("Tuple:", result5)
print("Type:", type(result5))
# Output:
# List: [10, 20, 30]
# Tuple: (10, 20, 30)
# Type: <class 'tuple'>


# 6. TUPLE TO LIST
tuple1 = (10, 20, 30)
result6 = list(tuple1)

print("Tuple:", tuple1)
print("List:", result6)
print("Type:", type(result6))
# Output:
# Tuple: (10, 20, 30)
# List: [10, 20, 30]
# Type: <class 'list'>


# 7. LIST TO SET
list2 = [10, 20, 20, 30, 30]
result7 = set(list2)

print("List:", list2)
print("Set:", result7)
print("Type:", type(result7))
# Output:
# List: [10, 20, 20, 30, 30]
# Set: {10, 20, 30}
# Type: <class 'set'>


# 8. RANGE TO LIST
range1 = range(1, 6)
result8 = list(range1)

print("Range:", range1)
print("List:", result8)
print("Type:", type(result8))
# Output:
# Range: range(1, 6)
# List: [1, 2, 3, 4, 5]
# Type: <class 'list'>