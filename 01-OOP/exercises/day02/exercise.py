# Base Class
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