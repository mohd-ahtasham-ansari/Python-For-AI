class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print("woof woof")

class cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def meow(self):
        print("meow")


dog1 = Dog("spiky","german shepard")
cat1 = cat("whiskers", "persian")
print(f"The {dog1.name} is a {dog1.breed} ")
dog1.bark()
print(f"The {cat1.name} is a {cat1.breed}")
cat1.meow()