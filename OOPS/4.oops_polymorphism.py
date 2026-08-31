#___________________[polymorphism]________________#

# polymorphism means having many forms in different conditions 

class Animal:
    def speak(self):
        print("animal cannot speak")

class Human:
    def speak(self):
        print("we are human we can speak")

obj = Animal()
obj2=Human()

obj.speak()
obj2.speak()

##_________[method  overriding]________________##
class Animal:
    def walk(self):
        print("animal cannot walk")

class Dog(Animal):
    def walk(self):
        print("dog can walk")

obj=Animal()
obj2=Dog()

obj.walk()
obj2.walk()