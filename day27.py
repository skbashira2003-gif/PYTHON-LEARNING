
# Polymorphism

# 1. Method Overriding

class Vehicle:
    def drive(self):
        print("Vehicle is driving")

class Bike(Vehicle):
    def drive(self):
        print("Bike is driving")

Vehicle().drive()
Bike().drive()


# 2. Method Overloading
# Python does not support traditional method overloading

def add(a, b):
    print(a + b)

def add(a, b, c):
    print(a + b + c)

def add(a, b, c, d):
    print(a + b + c + d)

add(1, 2, 3, 4)


# 2.1 Variable Arguments (*args)

def add(*a):
    print(sum(a))

add(1)
add(2, 3)
add(1, 2, 3, 4)


# 2.2 Default Parameters

def add(a, b=10, c=20):
    print(a + b + c)

add(1)
add(1, 2)
add(1, 2, 3)


# 3. Operator Overloading

# Using + operator

print(23 + 34)
print("rak" + "esh")
print([1, 2, 3] + [4, 5, 6])
print((1, 2, 3) + (4, 5, 6))

# Using * operator

print(45 * 34)
print([1, 2, 3] * 4)
print("rak" * 3)

# Unpacking using *

print([1, 2, 3])
print(*[1, 3, 4])


# Abstraction

from abc import ABC, abstractmethod

# 1. Abstract Class and Abstract Method

class Vehicle(ABC):
    def drive(self):
        print("Vehicle is driving")

    @abstractmethod
    def engine(self):
        pass

# 2. Implementing Abstract Method

class Bike(Vehicle):
    def engine(self):
        print("200CC")

# 3. Creating Object

b = Bike()
b.drive()
b.engine()
