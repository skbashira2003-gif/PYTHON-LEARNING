# ============================================================
# PYTHON OOP - CLASS, OBJECTS, VARIABLES AND METHODS
# ============================================================


# ------------------------------------------------------------
# 1. CLASS
# ------------------------------------------------------------

class Calculator:

    # Class Variable
    brand = "Casio"

    # Constructor
    def __init__(self, a, b):

        # Instance Variables
        self.a = a
        self.b = b

    # Instance Method
    def add(self):
        return self.a + self.b

    # Class Method
    @classmethod
    def sub(cls, a, b):
        return a - b

    # Static Method
    @staticmethod
    def mul(a, b):
        return a * b


# ------------------------------------------------------------
# 2. OBJECT CREATION
# ------------------------------------------------------------

calc1 = Calculator(10, 20)
calc2 = Calculator(100, 200)


# ------------------------------------------------------------
# 3. SEARCHING
# Object -> Class
# Python searches for variables/methods from object to class
# ------------------------------------------------------------

print("=== SEARCHING ====")

print(calc1.a)          # 10
print(calc2.b)          # 200

print(calc1.add())      # 30
print(calc2.add())      # 300

print(calc1.brand)      # Casio
print(calc2.brand)      # Casio

print()


# ------------------------------------------------------------
# 4. DYNAMIC NATURE OF PYTHON CLASSES
# ------------------------------------------------------------

print("=== DYNAMIC CLASSES ===")

# Add a variable only to calc1
calc1.c = 30

print(calc1.c)          # 30

# calc2 does not have c
# print(calc2.c)        # AttributeError

# Add a variable to the Calculator class
Calculator.version = 2

print(Calculator.version)   # 2
print(calc1.version)        # 2
print(calc2.version)        # 2

print()


# ------------------------------------------------------------
# 5. __dict__
# ------------------------------------------------------------

print("=== __dict__ ===")

print("Calculator.__dict__:")
print(Calculator.__dict__)

print()

print("calc1.__dict__:")
print(calc1.__dict__)

print()

print("calc2.__dict__:")
print(calc2.__dict__)

print()


# ------------------------------------------------------------
# 6. CREATING VARIABLES
# ------------------------------------------------------------

print("=== CREATING VARIABLES ===")

# Creating Class Variable
Calculator.build = "A"

# Creating Instance Variables
calc1.d = 400
calc2.e = 500

print("Calculator.__dict__:")
print(Calculator.__dict__)

print()

print("calc1.__dict__:")
print(calc1.__dict__)

print()

print("calc2.__dict__:")
print(calc2.__dict__)

print()


# ------------------------------------------------------------
# 7. UPDATING VARIABLES
# ------------------------------------------------------------

print("=== UPDATING VARIABLES ===")

# Updating Class Variable
Calculator.build = "B"

# Updating Instance Variables
calc1.d = 4000
calc2.e = 5000

print("Calculator.__dict__:")
print(Calculator.__dict__)

print()

print("calc1.__dict__:")
print(calc1.__dict__)

print()

print("calc2.__dict__:")
print(calc2.__dict__)

print()


# ------------------------------------------------------------
# 8. DELETING VARIABLES
# ------------------------------------------------------------

print("=== DELETING VARIABLES ===")

# Delete Class Variable
del Calculator.build

# Delete Instance Variables
del calc1.d
del calc2.e

print("Calculator.__dict__:")
print(Calculator.__dict__)

print()

print("calc1.__dict__:")
print(calc1.__dict__)

print()

print("calc2.__dict__:")
print(calc2.__dict__)

print()


# ------------------------------------------------------------
# 9. INSTANCE METHOD CALLING
# ------------------------------------------------------------

print("=== INSTANCE METHOD ===")

# Calling Instance Method using Object
print(calc1.add())          # 30

# Calling Instance Method using Class
# Object must be passed manually
print(Calculator.add(calc1))    # 30

print()


# ------------------------------------------------------------
# 10. CLASS METHOD CALLING
# ------------------------------------------------------------

print("=== CLASS METHOD ===")

# Calling Class Method using Object
# Class is automatically passed
print(calc1.sub(20, 10))        # 10

# Calling Class Method using Class
# Class is automatically passed
print(Calculator.sub(20, 10))   # 10

print()


# ------------------------------------------------------------
# 11. STATIC METHOD CALLING
# ------------------------------------------------------------

print("=== STATIC METHOD ===")

# Calling Static Method using Object
# No object/class is automatically passed
print(calc1.mul(10, 20))        # 200

# Calling Static Method using Class
# No object/class is automatically passed
print(Calculator.mul(10, 20))   # 200