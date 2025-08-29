# Base Class
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"Vehicle: {self.brand} ({self.year})"

# Child Class
class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors

    def info(self):
        return f"Car: {self.brand} ({self.year}), Number of Doors: {self.num_doors}"

# Another Child Class
class Motorcycle(Vehicle):
    def __init__(self, brand, year, type_motor):
        super().__init__(brand, year)
        self.type_motor = type_motor

    def info(self):
        return f"Motorcycle: {self.brand} ({self.year}), Type: {self.type_motor}"

    def horn_sound(self):
        return "Beep beep!"

# --- Usage ---
car1 = Car("Honda", 2020, 4)
motorcycle1 = Motorcycle("Yamaha", 2022, "Matic")

print(car1.info())
print(motorcycle1.info())
print(motorcycle1.horn_sound())