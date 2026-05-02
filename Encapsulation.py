# modify the car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand            # "__brand" is private Which is accessable by 'get_brand()' method.
        self.model = model
        
    def get_brand(self):
        return self.__brand  + "!" 
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    
    
my_car = ElectricCar("Tesla", "Model S", "85kwh")
# print(my_car.__brand)  # No attribute "brand".
# print(my_car.__brand)  # it is not work because of it is private attribute it can usable with 'get_brand()' method.
print(my_car.get_brand())
print(my_car.model)
print(my_car.battery_size)

    
    # Setter & Getter 

class Student:
    def __init__(self):
        self.__marks = 0   # private variable

    # Getter → get value
    def get_marks(self):
        return self.__marks

    # Setter → set value
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks!")

# Create object
s = Student()

# Set value
s.set_marks(90)

# Get value
print("Marks:", s.get_marks())