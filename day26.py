# ============================================================
# ADVANCED PYTHON OOP CONCEPTS
# ============================================================


# ============================================================
# 1. CONSTRUCTOR
# ============================================================

class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        return None


# Implicit Constructor Call
calc1 = Calculator(10, 20)

print("1. CONSTRUCTOR")
print(calc1.a)
print(calc1.b)

# Explicit Constructor Call
# __init__() must return None
calc3 = Calculator.__init__(calc1, 100, 200)

print(calc3)
print(calc1.a)
print(calc1.b)

print()


# ============================================================
# 2. DESTRUCTOR
# ============================================================

class Calculator:

    def __init__(self, a, b):
        print("Constructor")
        self.a = a
        self.b = b

    def __del__(self):
        print("Destructor")


print("2. DESTRUCTOR")

calc1 = Calculator(1, 2)

# Explicitly calling destructor method
calc1.__del__()

print()


# ============================================================
# 3. PRIVATE VARIABLES AND PRIVATE METHODS
# ============================================================

class Calculator:

    # Public Class Variable
    brand = "Casio"

    # Private Class Variable
    __version = 2

    def __init__(self, a, b):

        # Public Instance Variable
        self.a = a

        # Private Instance Variable
        self.__b = b

    # Public Method
    def display(self):
        print("Brand:", Calculator.brand)
        print("Version:", Calculator.__version)
        print("a:", self.a)
        print("b:", self.__b)

    # Private Method
    def __add(self):
        return self.a + self.__b


print("3. PRIVATE VARIABLES AND METHODS")

calc1 = Calculator(10, 20)

calc1.display()

# Accessing public variable
print(calc1.a)

# Private variables cannot normally be accessed directly
# print(Calculator.__version)  # AttributeError
# print(calc1.__b)             # AttributeError

# Name Mangling
print(Calculator._Calculator__version)
print(calc1._Calculator__b)

# Private method
# print(calc1.__add())  # AttributeError

# Accessing private method using name mangling
print(calc1._Calculator__add())

print()


# ============================================================
# 4. PROPERTY METHODS
# Getter, Setter and Deleter
# ============================================================

class Person:

    def __init__(self):
        self._age = None

    # Getter
    @property
    def age(self):
        print("Property / Getter Method")
        return self._age

    # Setter
    @age.setter
    def age(self, age):
        print("Setter Method")

        if age > 18:
            self._age = age
        else:
            raise ValueError("Age must be greater than 18")

    # Deleter
    @age.deleter
    def age(self):
        print("Deleter Method")
        del self._age


print("4. PROPERTY METHODS")

person1 = Person()

# Getter
print(person1.age)

# Setter
person1.age = 45

# Getter
print(person1.age)

# Deleter
del person1.age

print()


# ============================================================
# 5. PROPERTY FUNCTION
# Getter, Setter and Deleter using property()
# ============================================================

class Person:

    def __init__(self):
        self._age = None

    # Getter
    def get_age(self):
        print("Get age method")
        return self._age

    # Setter
    def set_age(self, value):
        print("Set age method")

        if value >= 0:
            self._age = value

    # Deleter
    def delete_age(self):
        print("Delete age method")

        if hasattr(self, "_age"):
            del self._age

    # property()
    age = property(
        get_age,
        set_age,
        delete_age
    )


print("5. PROPERTY FUNCTION")

person1 = Person()

# Getter
print(person1.age)

# Setter
person1.age = 45

# Getter
print(person1.age)

# Deleter
del person1.age

print()

# Methods can also be called explicitly
person1.set_age(50)

print(person1.get_age())

person1.delete_age()

print()


# ============================================================
# 6. ATTRIBUTE FUNCTIONS
# getattr(), setattr(), hasattr()
# ============================================================

class Calculator:

    brand = "Casio"

    def __init__(self, a, b):
        self.a = a
        self.b = b


print("6. ATTRIBUTE FUNCTIONS")

calc1 = Calculator(10, 20)

# ------------------------------------------------------------
# getattr()
# Gets the value of an attribute
# ------------------------------------------------------------

print("getattr:")

print(getattr(Calculator, "brand"))
print(getattr(calc1, "a"))
print(getattr(calc1, "brand"))

# ------------------------------------------------------------
# setattr()
# Creates or updates an attribute
# ------------------------------------------------------------

print()
print("setattr:")

setattr(Calculator, "version", 2)

print(getattr(Calculator, "version"))

setattr(Calculator, "version", 3)

print(getattr(Calculator, "version"))

setattr(calc1, "c", 2)

print(getattr(calc1, "c"))

# ------------------------------------------------------------
# hasattr()
# Checks whether an attribute exists
# ------------------------------------------------------------

print()
print("hasattr:")

print(hasattr(Calculator, "version"))
print(hasattr(Calculator, "a"))
print(hasattr(calc1, "a"))
print(hasattr(calc1, "version"))

print()


# ============================================================
# 7. INNER CLASS
# ============================================================

class Car:

    class Engine:

        def sound(self):
            print("Wrooom")


print("7. INNER CLASS")

# Creating Inner Class Object using Class
engine1 = Car.Engine()

engine1.sound()

# Creating Inner Class Object using Outer Class Object
car1 = Car()

engine2 = car1.Engine()

engine2.sound()

print()


# ============================================================
# 8. sys.getrefcount()
# ============================================================

import sys

print("8. REFERENCE COUNT")

# List object
l = [1, 2, 3, 4]

a = l
b = l
c = l

print("List reference count:")
print(sys.getrefcount(l))

# Integer object
i = 1

x = i
y = i
z = i

print("Integer reference count:")
print(sys.getrefcount(i))

print()


# ============================================================
# 9. dir() FUNCTION
# ============================================================

class Calculator:

    brand = "Casio"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


print("9. DIR FUNCTION")

# Module / Current Namespace
print("Module:")
print(dir())

print()

# Class Attributes and Methods
print("Class:")
print(dir(Calculator))

print()

# Object Attributes and Methods
print("Object:")
print(dir(Calculator(10, 20)))

print()




