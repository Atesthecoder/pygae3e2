class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        return self.model + "" + self.make + "" + self.year
    def get_info(self):
        print("working on it...")
Car("Toyota", "Camry", 2020)
Car.get_info()
    