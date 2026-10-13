#Polymorphism:
#1. Method Overriding
class Vehicle:
    def drive(s):
        print('Vehicle is driving')
class Bike(Vehicle):
    def drive(s):                 #child class with same method name as in parent class
        print('Bike is driving')
Vehicle().drive()   #calling through parent 
Bike().drive()      #calling through child

#2. Method Overloading (Python does not support)
def add(a, b):
    print(a+b) 
def add(a, b, c):
    print(a+b+c)
def add(a, b, c, d):   #last defined function only considered
    print(a+b+c+d)
# add(1, 2)
# add(1,2,3)
add(1,2,3,4)

#2.1 But can be achieved using default or vararg parameters
#var-arg parameter
def add(*a):
    print(sum(a))
add(1)
add(2, 3)
add(3,4,23,4,23,42,34,2,34,2,3423,4)
print()
#default parameters
def add(a, b=10, c=20):
    print(a+b+c)
add(1)
add(1,2)
add(1,2,3)

#2.2. Python supports operator overloading 
#Same operator doing different operations based on oparands
# + : 1. addition between non-sequences. 2. concatenation between same sequences
print(23+34)
print('rak'+'esh')
print([1,2,3]+[4,5,6])
print((1,2,3)+(4,5,6))
print()
# * : 1. multiplication between non-sequences. 2. repetition between sequence and an integer
#     3. unpacking before a sequence
print(45*34)
print([1,2,3]*4)
print('rak'*3)
print([1,2,3])  #prints list
print(*[1,3,4]) #unpacks and prints each element separately



#Abstraction:
from abc import ABC, abstractmethod
class Vehicle(ABC):
  def drive(s):
    print('Vehicle is driving')
  @abstractmethod
  def engine(s):
    pass
v = Vehicle()      #cannot create object if there are abstract methods
class Bike(Vehicle):
  pass   
b = Bike()         #cannot create object if abstract methods are not implemented
class Bike(Vehicle):
  def engine(s):     #implemented the abstract method engine()
    print('200CC')
b = Bike()          
