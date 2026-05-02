# Create two classes battery and Enginr, and let the EletricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    def battery_info(self):
        return "This is Battery."

class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCar(Battery, Engine):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_tesla = ElectricCar("Tesla", "Model S")

print(my_tesla.engine_info())
print(my_tesla.battery_info())