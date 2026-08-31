### INHERITENCE   (inherite or access the properties of one class to another class)

class Animal:                  #parent class / base class
    def __init__(self, name):
        self.name = name

    a= 12

    def details(self):
        print(f"hello , my name is {self.name}")

class Human(Animal):                  #child class / derived class
    pass

obj1 = Animal("wiskers")              #object of parent class
obj2 = Human("rohan")                 #object of child class

obj1.details()
obj2.details()
print(obj2.a)

 
class Car:                        #parent class / base class
    def __init__(self,name,mileage):    #object /instance attribute
        self.name = name
        self.mileage = mileage

    def maxspeed(self):            #object /instance method
        print(f"max speed of {self.name} is {self.mileage*10}")

class ElectriCar(Car):                #child class / derived class
    pass

obj1 = Car("swift",10)              #object of parent class
obj2 = ElectriCar("Tesla",20)         #object of child class

obj1.maxspeed()
obj2.maxspeed()


####_______________________Multi - levels of inheritance________________________________________###

# when one inheritence leads to another inheritence then it is called as multi-level inheritance 


class BagFactory:
    def __init__(self,material , pockets,zips):
        self.material = material
        self.pockets = pockets
        self.zips = zips
    
    def details(self):
        print(f"material is {self.material}\nand pockets are {self.pockets}\nand zips are {self.zips}")

class Reebok(BagFactory):
    def __init__(self,material , pockets,zips,color):
        super().__init__(material , pockets,zips)
        self.color = color
    
    def details(self):
        super().details()
        print(f"color is {self.color}")


class Puma(Reebok):
    def __init__(self,material , pockets,zips,color,size):
        super().__init__(material , pockets,zips,color)
        self.size = size
    
    def details(self):              #overriding /modifying a method 
        super().details()
        print(f"size is {self.size}")


obj = Puma("leather", 2 ,3 , "black",10)       
obj.details()

    


################_________________  Multiple inheritance _____________________________________############

# when a child class inherit multiple parent class is called as multiple inheritance .abs

class collage:
    def __init__(self, clg_name ):
        self.clg_name = clg_name

    def details(self):
        print(f"collage name is {self.clg_name}")

class Department:
    def __init__(self , dept_name):
        self.dept_name = dept_name
    
    def dept_details(self):
        print(f"department name is {self.dept_name}")

class student(collage,Department):
    def __init__(self , name,id,clg_name , dept_name):
        collage.__init__(self , clg_name)
        Department.__init__(self , dept_name)
        self.name=name
        self.id=id
    def details(self):
        super().details()
        super().dept_details()
        print(f"name :{self.name}")
        print(f"id :{self.id}")

student1 = student("abc","csaiml12334","Gl bajaj institute of technology and management", "aiml")
student1.details()

#____________hierarchial inheritance___________________####################

class Father:
    def __init__(self,height):
        self.height=height


class Son(Father):
    def __init__(self,height,weight):
        super().__init__(height)
        self.weight=weight

class Daughter(Father):
    def __init__(self,height,weight):
        super().__init__(height)
        self.weight=weight