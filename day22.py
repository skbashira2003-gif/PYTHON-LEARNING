# FILE HANDLING IN PYTHON

# ============================================================
# 1. CREATE / WRITE A FILE
# ============================================================

file = open("student.txt", "w")

file.write("Name: Bashira\n")
file.write("Age: 23\n")
file.write("Course: Python\n")

file.close()

print("File created and data written successfully")


# ============================================================
# 2. READ A FILE
# ============================================================

file = open("student.txt", "r")

data = file.read()

print("\nFile Content:")
print(data)

file.close()


# ============================================================
# 3. READLINE()
# ============================================================

file = open("student.txt", "r")

line1 = file.readline()
line2 = file.readline()

print("First line:", line1)
print("Second line:", line2)

file.close()


# ============================================================
# 4. READLINES()
# ============================================================

file = open("student.txt", "r")

lines = file.readlines()

print("\nAll Lines:")
print(lines)

file.close()


# ============================================================
# 5. APPEND DATA
# ============================================================

file = open("student.txt", "a")

file.write("City: Guntur\n")
file.write("Skill: Python\n")

file.close()

print("\nNew data appended successfully")


# ============================================================
# 6. READ AFTER APPENDING
# ============================================================

file = open("student.txt", "r")

print("\nUpdated File Content:")
print(file.read())

file.close()


# ============================================================
# 7. USING WITH STATEMENT
# ============================================================

with open("student.txt", "r") as file:
    data = file.read()

print("\nUsing with statement:")
print(data)


# ============================================================
# 8. WRITE MULTIPLE LINES
# ============================================================

students = [
    "Bashira\n",
    "Narmaja\n",
    "sravan\n",
    "poojitha\n"
]

with open("students.txt", "w") as file:
    file.writelines(students)

print("\nMultiple lines written successfully")


# ============================================================
# 9. READ FILE USING FOR LOOP
# ============================================================

print("\nReading using for loop:")

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())


# ============================================================
# 10. CHECK FILE EXISTENCE
# ============================================================

import os

if os.path.exists("student.txt"):
    print("\nstudent.txt exists")
else:
    print("\nstudent.txt does not exist")


# ============================================================
# 11. FILE NAME
# ============================================================

with open("student.txt", "r") as file:
    print("File name:", file.name)


# ============================================================
# 12. FILE MODE
# ============================================================

with open("student.txt", "r") as file:
    print("File mode:", file.mode)


# ============================================================
# 13. FILE CLOSED OR NOT
# ============================================================

file = open("student.txt", "r")

print("Before closing:", file.closed)

file.close()

print("After closing:", file.closed)


# ============================================================
# 14. WRITE AND READ
# ============================================================

with open("example.txt", "w+") as file:
    file.write("Hello Python")

    # Move cursor to beginning
    file.seek(0)

    print("\nWrite and Read:")
    print(file.read())


# ============================================================
# 15. TELL() - CURRENT FILE POSITION
# ============================================================

with open("example.txt", "r") as file:
    print("\nInitial position:", file.tell())

    file.read(5)

    print("Position after reading 5 characters:", file.tell())


# ============================================================
# 16. SEEK() - CHANGE FILE POSITION
# ============================================================

with open("example.txt", "r") as file:
    print("\nBefore seek:", file.read(5))

    file.seek(0)

    print("After seek:", file.read())


# ============================================================
# 17. DELETE A FILE
# ============================================================

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("\nexample.txt deleted successfully")
else:
    print("\nexample.txt does not exist")


# ============================================================
# 18. FILE HANDLING WITH EXCEPTION HANDLING
# ============================================================

try:
    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("\nError: File not found")


# ============================================================
# 19. DIFFERENT FILE MODES
# ============================================================

print("\nFile Modes:")

print("r  - Read")
print("w  - Write")
print("a  - Append")
print("x  - Create")
print("r+ - Read and Write")
print("w+ - Write and Read")
print("a+ - Append and Read")
