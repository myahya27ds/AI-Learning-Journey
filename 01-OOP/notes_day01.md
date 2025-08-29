# 📝 Notes: OOP Python

---

## 📌 Definition of OOP
**Object Oriented Programming (OOP)** is a programming paradigm focused on the concept of **objects**, which have **attributes (data)** and **methods (behavior/functions)**.  
The goal is to make code more structured, maintainable, and reusable.

---

## 🛠️ Basic Concepts

### 1. Class
- Blueprint for creating objects.
- Contains attributes and methods.

```python
class Student:
    name = "None"
    major = "None"
```

---

### 2. Object
- The instance (realization) of a class.
```python
s1 = Student()
print(s1.name)      # Output: None
```

---

### 3. Attribute
- Variables owned by a class/object.
```python
s1.name = "Andy"
s1.major = "Informatics"
print(s1.name, s1.major)
```

---

### 4. Method
- Functions defined inside a class.
```python
class Student:
    def greet(self):
        return f"Hello, my name is {self.name}"

s1 = Student()
s1.name = "Budi"
print(s1.greet())   # Output: Hello, my name is Budi
```

---

### 5. Constructor (`__init__`)
- Special method called automatically when an object is created.
```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

s2 = Student("Citra", "Information Systems")
print(s2.name, s2.major)
```

---

### 6. Encapsulation
- Restricts direct access to object attributes.
- Done using prefix `_` (protected) or `__` (private).
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade   # private attribute

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade!")

s3 = Student("Dina", 85)
print(s3.get_grade())  # 85
s3.set_grade(110)      # Invalid grade!
```

---

### 💡 Important Notes
- Class is the blueprint, object is the instance.
- Attribute = data, Method = behavior.
- `__init__` is used for object initialization.
- Encapsulation protects data (access is restricted).

---

### 🎯 Challenge
1. Create a class BankAccount with attributes: name, balance.
   - Add methods check_balance(), deposit(amount), and withdraw(amount).
   - Use encapsulation to protect balance from unauthorized access.
2. Create an object from BankAccount and simulate transactions.

```python
class BankAccount:
    def __init__(self, name, balance):
        self.name = name              # public
        self.__balance = balance      # private

    # Getter
    def check_balance(self):
        return f"{self.name}'s balance: ${self.__balance}"

    # Setter - deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. Current balance: ${self.__balance}"
        return "Deposit amount must be positive!"

    # Setter - withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. Current balance: ${self.__balance}"
        return "Insufficient balance or invalid amount!"

account1 = BankAccount("Yahya", 100000)

print(account1.check_balance())
print(account1.deposit(50000))
print(account1.withdraw(30000))

# Direct access attempt (will error)
# print(account1.__balance)
```