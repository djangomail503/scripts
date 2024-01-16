class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")

class Car:
    def __init__(self, make, model, year, color="Black"):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = 0
        self.engine = Engine("Gasoline")

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} ({self.color})")

    def drive(self, miles):
        print(f"Driving {miles} miles.")
        self.mileage += miles

    def get_mileage(self):
        return self.mileage

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()

# Example usage:
car3 = Car("Ford", "Mustang", 2023, "Red")
car3.start_engine()
car3.drive(50)
car3.stop_engine()
print(f"{car3.get_mileage()} miles driven.")
car3.display_info()
