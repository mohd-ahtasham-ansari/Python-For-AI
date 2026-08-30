class Animal:
    def __init__(self , name , breed):
        self.name =name
        self.breed = breed
    
    def sleep(self):
        return f"{self.name} is sleeping "
    
    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):
    def bark(self):
        return f"{self.name} is barking "
    
    def fetch(self):
        return f"{self.name} is fetching"

dog1 = Dog("spiky", "german shepard")
print(dog1.sleep())
print(dog1.fetch())

class Cat(Animal):
    def meow(self):
        return f"{self.name} is meowing"

cat1=Cat("whiskers","Persian")
print(cat1.eat())
print(cat1.meow())