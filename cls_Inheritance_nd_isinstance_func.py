# Demonstrate the use of isinstance() to check if my_tesla is an isinstance of car and ElectricCar.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model  = model
        
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return  "Petrol And Desiel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) 
        self.battery_size = battery_size
        
    def fuel_type(self):
        return  "Eletric Charge"
         
my_tesla = ElectricCar("Tesla", "Model S", "85kwh")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))