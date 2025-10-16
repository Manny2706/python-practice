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