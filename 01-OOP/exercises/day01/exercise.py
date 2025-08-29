# Student Class
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def introduce(self):
        return f"Hi, my name is {self.name} and I study {self.major}."

# --- Testing ---
s1 = Student("Yahya", "Economics Education")
print(s1.introduce())