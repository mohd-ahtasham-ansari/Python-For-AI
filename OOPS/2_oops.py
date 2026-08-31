class Bag:
    def __init__(self, material , zips , pocket):
        self.material = material
        self.zips = zips
        self.pocket = pocket

    def order(self):
        return f"order placed"

reebok = Bag("leather", 2 ,3)

print(f"reebok is made of {reebok.material} and has {reebok.zips} zips and {reebok.pocket} pockets")

print(reebok.order())


class Animal:

    a =12   #Class attribute

    def __init__(self,name):  #object /instance attribute  , capture the location os object
        self.name = name

    def hello(self):                             # object /instance method , capture the location os object and cls
        print(f"hello my name is {self.name}")

    def hello2(self):                           # object /instance method , capture the location of object and cls
        print(f"hello my name is {self.a}")

    @classmethod
    def greet(cls):                           # class method , capture the location of cls
        print(f"hello from class method {cls.a}")

    @staticmethod
    def speak():
        print("helllo , i am a static methon") #static method , capture the location of cls but not use it 


obj = Animal("lion")          #object

obj.hello()                 #calling object method
obj.hello2()                  #calling object method
obj.greet()                   #calling class method