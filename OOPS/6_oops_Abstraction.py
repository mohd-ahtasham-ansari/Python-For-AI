##______________________________[ ABSTRACTION ]_________________________________##

""" abtraction does not exist in python but we can achieve it using a library  ,, abstraction is used to simpify the 
complex system by focusing on essential  features and hiding  unnecessary detail

Abstract classes and methods:
- Abstract classes are classes that contains one or more abstract methods.
- Abstract method: A method that is defined but not implemented in the abstract class. subclasses must provide the implementation.
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")
    
    def stop(self):
        print("Car stopped")

car = Car()
car.start()
car.stop()
 

from abc import ABC, abstractmethod

class Enforce(ABC):
    @abstractmethod
    def start(self):
        pass

class Truck(Enforce):
    def start(self):
        print ("truck started")


class Car(Enforce):
    def start(self):
        print ("car started")
    
   
obj=Car()
obj.start()

obj2 = Truck()
obj2.start()

