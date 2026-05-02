# Add a class variable to car that keeps track of the number of cars created.

class Car:
    total_car = 0    # variables
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1    # count cars created
        
    def get_brand(self):
        return self.__brand
    # object created
A = Car("Tata", "Thar")
B = Car("Tata", "Beloro")
             # OR
# Car("Tata", "Thar")
# Car("Tata", "Beloro")

# print(A.total_car)
        # OR
print(Car.total_car)
print(A.get_brand())