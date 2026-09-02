#_____________________________[ ENCAPSULATION ]_________________________________#

#encapsulation is the process of binding data and the function that operate on the data together as a single unit 

class Car:
    def __init__(self , brand , model , price):
        self.brand = brand           #public attribute
        self.__model = model         #private attribute
        self.__price = price         #private attribute

    def display(self):
        print(f"brand :{self.brand}")
        print(f"model :{self.__model}")
        print(f"price :{self.__price}")

    def get_model(self):
        return self.__model

    def set_model(self , model):
        self.__model = model

    def get_price(self):
        return self.__price

    def set_price(self , price):
        self.__price = price

    def __secret(self):
        print("this is a private method")

obj = Car("audi","A4",5000000)
obj.display()
print(obj.get_model())
obj.set_model("A6")
print(obj.get_model())
print(obj.get_price())
obj.set_price(6000000)
print(obj.get_price())
obj._Car__secret()      #accessing private method


class Factory:
    name = "MG"  #public class attribute
    _old = 15 # protected class attribute
    __fuel = "petrol" #private class attribute
    
    def __init__(self, type , tyre , color): 
        self.type = type
        self.__tyre = tyre # private object attribute
        self.color = color
     
    def __detail(self):
        pass


obj = Factory("Sedan","mrf","white")

obj.name ="kia"
obj.old =18
print(obj.name)
print(obj._old)
print(obj._Factory__fuel) # acess private attribute


class hello(Factory):
    print(Factory._Factory__fuel)
    print(Factory._old)
    print(Factory.name)
    print(Factory.__init__)


