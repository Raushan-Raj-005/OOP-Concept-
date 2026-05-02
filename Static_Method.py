# Add a static method to the class that returns a general description of a car.

class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand
    @staticmethod
    # def general_description(self):
    def general_description():
        return "Cars are means of transport"
    
class ElectricCar(Car):
    def __init__(self, brand, model, bettery_size):
        super().__init__(brand, model)
        self.bettery_size = bettery_size
        
    def fuel_type(self):
        return "Electric Charge" 
    
my_car = Car("Tata", "Thar") 
Car("Tata", "Nexon")

# print(my_car.general_description())        
print(Car.general_description())        