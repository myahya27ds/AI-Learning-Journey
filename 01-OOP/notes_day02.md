# 📝 Notes: Inheritance in Python OOP

---

## 📌 Definition
**Inheritance** is an OOP concept where a class (child/subclass) can **inherit attributes and methods** from another class (parent/superclass).  
With inheritance, we can create new classes without rewriting the same code.

---

## 🛠️ Basic Concepts
- **Parent Class (Superclass)** → the class being inherited from.  
- **Child Class (Subclass)** → the class that inherits.  
- Subclasses can **add** new methods/attributes or **override** methods from the superclass.  
- The `super()` function is used to call the constructor or methods of the parent class.

---

## 📝 Code Example
```python
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "This animal makes a sound"

# Child Class
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # call parent's __init__
        self.breed = breed

    def make_sound(self):
        return "Meow!"  # override parent method

# Another Child Class
class Dog(Animal):
    def make_sound(self):
        return "Woof Woof!"

# --- Usage ---
c1 = Cat("Milo", "Persian")
d1 = Dog("Doggy")

print(f"{c1.name} makes sound: {c1.make_sound()}")
print(f"{d1.name} makes sound: {d1.make_sound()}")
```

---

### 💡 Important Notes
- Subclasses automatically have all attributes & methods of the parent.
- You can add new methods specific to the subclass.
- You can override methods to change behavior from the parent.
- `super()` → used to call parent methods/attributes.

---

### 🎯 Challenge
1. Create a class Vehicle with attributes brand and year.
   - Add a method info() to display vehicle information.
2. Create a subclass Car that inherits Vehicle with an additional attribute num_doors.
   - Override the info() method to show all details.
3. Create a subclass Motorcycle with an additional attribute type_motor (e.g., cub, sport, matic).
   - Add a special method horn_sound().

```python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"Vehicle: {self.brand} ({self.year})"

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors

    def info(self):
        return f"Car: {self.brand} ({self.year}), Number of Doors: {self.num_doors}"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, type_motor):
        super().__init__(brand, year)
        self.type_motor = type_motor

    def info(self):
        return f"Motorcycle: {self.brand} ({self.year}), Type: {self.type_motor}"

    def horn_sound(self):
        return "Beep beep!"

# Example usage
car1 = Car("Honda", 2020, 4)
motorcycle1 = Motorcycle("Yamaha", 2022, "Matic")

print(car1.info())
print(motorcycle1.info())
print(motorcycle1.horn_sound())
```