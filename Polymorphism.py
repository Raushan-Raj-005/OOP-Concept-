# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

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
        
my_car = Car("Tata", "Thar")  
my_ecar = ElectricCar("Tesla", "Model S", "85kwh")

print(my_car.fuel_type())
print(my_ecar.fuel_type())
         