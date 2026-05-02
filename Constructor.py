class Student:
    def __init__(self, name):
        self.name = name  # Tnitilize variables
        
    def show(self):
        print("Name", self.name)
        
s1 = Student("Raushan")   #constructor automatically calling
s1.show()