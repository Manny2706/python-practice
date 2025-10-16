#  Class, Object, Constructor (init)

# class Car:#class
#     def __init__(self, make, model, year):#constructor
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         return f"{self.year} {self.make} {self.model}"
    
# obj1 = Car("Toyota", "Camry", 2020)#object

# print(obj1.display_info())

# INSTANCE VARIABLE, CLASS VARIABLE, CLASS METHOD, STATIC METHOD

# class Car:#class
#     total_cars = 0 #class variable
#     def __init__(self, make, model, year):#constructor
#         self.make = make
#         self.model = model
#         self.year = year
#         Car.total_cars += 1 #can access class variable inside constructor using class name
    
#     @classmethod# class method can only access class variable
#     def get_wheels_needed(cls):#cls is a convention for class method cls refers to class as self refers to object
#         return cls.total_cars * 4
    # @staticmethod
    # def total_cars_count():# no need to pass self or cls
    #     return Car.total_cars
    # @staticmethod
    # def printmessage():
    #     print("Cars are cool!")  

    

#     def display_info(self):# instance method can access both instance and class variable
#         return f"{self.year} {self.make} {self.model} {Car.total_cars}"
    
# obj1 = Car("Toyota", "Camry", 2020)#object

# print(obj1.display_info())
# obj2 = Car("Honda", "Civic", 2021)#object
# print(obj2.display_info())

# obj3 = Car("Ford", "Mustang", 2022)#object
# print(obj3.display_info())

# print(Car.get_wheels_needed())#accsessing class method
# print(obj1.get_wheels_needed())#accsessing class method
# print(Car.total_cars_count())#accsessing static method
# print(obj1.total_cars_count())#accsessing static method
# print(obj2.total_cars_count())

# print(Car.total_cars)#accsessing class variable

#  INHERITENCE

# class Car:#class
#     def __init__(self, make, model, year):#constructor
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         return f"{self.year} {self.make} {self.model}"
    
# class ElectricCar(Car):#child class
#     def __init__(self, make, model, year, battery_size):#constructor
#         super().__init__(make, model, year)#calling parent class constructor
#         self.battery_size = battery_size
#     def display_battery_info(self):# acess parent class method
#         return f"{self.display_info()} with a {self.battery_size}-kWh battery"

# obj1 = ElectricCar("Tesla", "Model S", 2020, 100)#object    
# print(obj1.display_battery_info())
#POLYMORPHISM

# class Car:#class
#     def __init__(self, make, model, year):#constructor
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def display_info(self):
#         return f"{self.year} {self.make} {self.model}"
#     def start_engine(self):
#         return "The car's engine is starting."
    
# class ElectricCar(Car):#child class
#     def __init__(self, make, model, year, battery_size):#constructor
#         super().__init__(make, model, year)#calling parent class constructor
#         self.battery_size = battery_size
#     def display_battery_info(self):# acess parent class method
#         return f"{self.display_info()} with a {self.battery_size}-kWh battery"
#     def start_engine(self):
#         return "The electric car is starting silently."
    
# class IgnitionCar(Car):#child class#method overriding
#     def start_engine(self):#method overriding
#         return "The ignition car's engine is starting with a roar."

# obj1 = ElectricCar("Tesla", "Model S", 2020, 100)#object 
# obj2 = IgnitionCar("Ford", "Mustang", 2021)#object
# print(obj1.start_engine())
# print(obj2.start_engine())   

# ENCAPSULATION
class Car:#class
    def __init__(self, make, model, year):#constructor
        self.__make = make#private variable
        self.__model = model#private variable
        self.__year = year#private variable

    def display_info(self):
        return f"{self.__year} {self.__make} {self.__model}"
    
    def get_make(self):#getter method
        return self.__make
    
    def set_make(self, make):#setter method
        self.__make = make
    
class ElectricCar(Car):#child class
    def __init__(self, make, model, year, battery_size):#constructor
        super().__init__(make, model, year)#calling parent class constructor
        self.__battery_size = battery_size#private variable

    def display_battery_info(self):# acess parent class method
        return f"{self.display_info()} with a {self.__battery_size}-kWh battery"
    
    def get_battery_size(self):# BASIC getter method
        return self.__battery_size
    
    def set_battery_size(self, battery_size):# BASIC setter method
        self.__battery_size = battery_size
    
    @property# property decorator
    def battery_size(self):# ADVANCED getter method
        return self.__battery_size
    @battery_size.setter# property decorator
    def battery_size(self, battery_size):# ADVANCED setter method
        self.__battery_size = battery_size

obj1 = ElectricCar("Tesla", "Model S", 2020, 100)#object    
print(obj1.display_battery_info())
print(obj1.get_battery_size())# accessing BASIC getter method
obj1.set_battery_size(120)# accessing BASIC setter method
print(obj1.get_battery_size())# accessing BASIC getter method
print(obj1.battery_size)# accessing ADVANCED getter method
obj1.battery_size = 150# accessing ADVANCED setter method
print(obj1.battery_size)# accessing ADVANCED getter method
# difference between BASIC and ADVANCED getter and setter method is that in BASIC we 
# have to call the method using () but in ADVANCED we can access it like a variable without ().
# and also in ADVANCED we can use property decorator to create getter and setter method with same name as variable.
# ADVANCED getter and setter method is more python way 

