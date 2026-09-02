#_________________________[DUNDER METHODS ]_______________________________##

"""
WHAT ARE DUNDER METHODS?
- "Dunder" stands for "Double Underscore" because these methods start and end with two underscores (e.g., __init__, __str__, __add__).
- Also known as "Magic Methods" or "Special Methods".

IN VERY SIMPLE WORDS:
- They are built-in methods that let your objects work with Python's standard operations (like +, -, print(), len()).
- You don't usually call them directly; Python automatically calls them behind the scenes!
  Example: When you write `num1 + num2`, Python automatically calls `num1.__add__(num2)`.
"""

class Animal:
    def __init__(self,name,):
        self.name = name 
    
    def __str__(self):
        return f"name is {self.name}"

obj1 = Animal("lion")
print(obj1)
print(obj1.name)


obj2 = Animal("cat")
print(obj2)
print(obj2.name)


class nums:
    def __init__(self,a):
        self.a = a
    
    def __add__(self,other):
        return self.a + other.a
    
    def __eq__(self, other):
        return self.a == other.a
    
num1 = nums(10)
num2 = nums(20)
print(num1 + num2)
print(f"add using dunder {num1.__add__(num2)}")

num3=nums(20)
print(num3==num2)
print(f"eqaual using dunder {num3.__eq__(num2)}")


####__________[ Decorators]____________#########

def greeting(func):
    def wrapper():
        print("welcome to codeacademy")

        func()

        print("visit again")
    return wrapper

@greeting
def hello():
    print("lets learn to python")

hello()



