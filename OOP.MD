# **Object-Oriented Programming (OOP) Concepts in Python**

This repository provides an in-depth exploration of Object-Oriented Programming (OOP) principles in Python, including encapsulation, inheritance, polymorphism, and more. It is designed to help developers understand and implement OOP concepts effectively.

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [Encapsulation](#encapsulation)
   - [Encapsulation Example](#encapsulation-example)
3. [Inheritance](#inheritance)
   - [Inheritance Example](#inheritance-example)
4. [Polymorphism](#polymorphism)
   - [Polymorphism Example](#polymorphism-example)
5. [Static and Instance Methods](#static-and-instance-methods)
   - [Static Method Example](#static-method-example)
6. [Magic Methods (Dunder Methods)](#magic-methods-dunder-methods)
   - [Magic Methods Example](#magic-methods-example)
7. [Recap](#recap)

---

## **Introduction**

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design and structure software. These objects encapsulate data and methods, enabling code reuse, scalability, and better organization.

Key OOP principles:
- **Encapsulation:** Hiding implementation details.
- **Inheritance:** Reusing and extending existing code.
- **Polymorphism:** Using a unified interface for different object types.

---

## **Encapsulation**

Encapsulation restricts access to certain parts of an object’s state and behavior. It ensures that an object’s internal state can only be changed through its methods.

### **Encapsulation Example**

```python
class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None  # Protected attribute
        self.__bugs_solved = 0  # Private attribute

    def code(self):
        self.__bugs_solved += 1

    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)

    def get_salary(self):
        return self._salary

    def _calculate_salary(self, base_value):
        if self.__bugs_solved < 10:
            return base_value
        elif self.__bugs_solved < 100:
            return base_value * 2
        return base_value * 3
```
### **Encapsulation Example**
```python
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")

class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def work(self):
        print(f"{self.name} is coding...")

class Designer(Employee):
    def work(self):
        print(f"{self.name} is designing...")
```
#### Example usage:
```python
Copy code
se = SoftwareEngineer("Max", 25, 5000, "Junior")
d = Designer("Philipp", 27, 7000)

se.work()  # Output: Max is coding...
d.work()   # Output: Philipp is designing...
Polymorphism
Polymorphism allows different classes to use the same interface.
```
### Polymorphism Example
```python
Copy code
employees = [
    SoftwareEngineer("Max", 25, 5000, "Junior"),
    Designer("Philipp", 27, 7000)
]

def motivate_employee(employees):
    for employee in employees:
        employee.work()

motivate_employee(employees)
```
#### Output:
```csharp
Copy code
Max is coding...
Philipp is designing...
Static and Instance Methods
Static methods can be accessed without creating an object, whereas instance methods require an object.
```
### Static Method Example
```python
Copy code
class SoftwareEngineer:
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        return 7000
```
#### Example Usage:
```python
Copy code
print(SoftwareEngineer.entry_salary(24))  # Output: 5000
Magic Methods (Dunder Methods)
Magic methods (also called dunder methods) are special methods in Python used for operator overloading and other custom behavior.
```

### Magic Methods Example
```python
Copy code
class SoftwareEngineer:
    def __init__(self, name, age, level):
        self.name = name
        self.age = age
        self.level = level

    def __str__(self):
        return f"{self.name}, {self.age}, {self.level}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
```

#### Example Usage:
```python

Copy code
se1 = SoftwareEngineer("Max", 25, "Junior")
se2 = SoftwareEngineer("Max", 25, "Junior")
print(se1 == se2)  # Output: True
```
### Recap
--A class is a blueprint for creating objects.
    --An object is an instance of a class.
    --Attributes can be class attributes or instance attributes.
#### Core OOP principles include Encapsulation, Inheritance, and Polymorphism.
##### Magic methods and decorators like `@staticmethod` and `@property `enhance class functionality.

---Feel free to fork, star, and contribute to this repository!









