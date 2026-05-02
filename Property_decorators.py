# Use a property decorator in the class to make the model attribute read only.


class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand
    @staticmethod
    # def general_description(self):
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, bettery_size):
        super().__init__(brand, model)
        self.bettery_size = bettery_size
        
    def fuel_type(self):
        return "Electric Charge" 
    
my_car = Car("Tata", "Thar") 
# my_car.model = "raj"
Car("Tata", "Nexon")

# print(my_car.general_description())        
# print(Car.general_description())

print(my_car.model)        