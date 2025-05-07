class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

class Car:
    def drive(self):
        print("The car is driving")

    def stop(self):
        print("The car has stopped")

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


circle = Circle(5)
print("Circle area:", circle.area())

class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def introduce(self):
        print(f"My name is {self.name}, I study {self.subject} and my grade is {self.grade}.")

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")