######################################################## Questions ########################################################


# ## 🟢 Question 1: Basic Class & Object

# Create a class **Student** that has:

# * `name`
# * `roll_number`

# Use `__init__` to initialize the values.

# 👉 Create one object and print:

# ```
# Student Name: <name>
# Roll Number: <roll_number>
# ```

# ---

# ## 🟡 Question 2: Multiple Objects

# Create a class **Car** with:

# * `brand`
# * `model`
# * `year`

# Use `__init__`.

# 👉 Create **two car objects**
# 👉 Print details of both cars in this format:

# ```
# Brand: Toyota, Model: Fortuner, Year: 2022
# Brand: Honda, Model: City, Year: 2021
# ```

# ---

# ## 🔵 Question 3: Class with a Method

# Create a class **Person** with:

# * `name`
# * `age`

# Use `__init__`.

# Add a method `greet()` that prints:

# ```
# Hello, my name is <name> and I am <age> years old.
# ```

# 👉 Create an object and call the `greet()` method.

# ---
######################################################## Solutions ########################################################

# class Student:
#     def __init__(self,name,roll_number):
#         self.name = name
#         self.roll_number = roll_number
        
# p1 = Student("Shlok",2)
# print(f"Student Name: {p1.name}")

# class Car:
#     def __init__ (self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
        
# car1 = Car("Toyota","Fortuner",2022)
# car2 = Car("Honda","City",2021)

# print(f"Brand: {car1.brand}, Model: {car1.model}, Year: {car1.year}")
# print(f"Brand: {car2.brand}, Model: {car2.model}, Year: {car2.year}")

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."
        
# person1 = Person("Shlok",23)
# print(person1.greet())

######################################################## Questions  ########################################################

# ## 🟢 Question 1: Class Variable + Instance Variable

# Create a class **Company** with:

# * Class property: `company_name = "TechCorp"`
# * Instance properties: `employee_name`, `employee_id` (using `__init__`)

# 👉 Create **2 employee objects** and print:

# ```
# TechCorp - <employee_name> (<employee_id>)
# ```

# ---

# ## 🟡 Question 2: Class Method to Update Class Property

# Create a class **Student** with:

# * Class property: `school_name = "ABC School"`
# * Instance property: `name`

# Add a **class method** `change_school(cls, new_name)`
# that updates the school name.

# 👉 Change the school name and print it using **two different objects**.

# ---

# ## 🟡 Question 3: Counter Using Class Property

# Create a class **User** with:

# * Class property: `total_users = 0`
# * Instance property: `username`

# Each time a new object is created:

# * Increase `total_users` by 1

# 👉 Create 3 users and print:

# ```
# Total users: 3
# ```

# ---

# ## 🔵 Question 4: Mix of Instance Method & Class Method

# Create a class **BankAccount** with:

# * Class property: `bank_name = "Python Bank"`
# * Instance properties: `account_holder`, `balance`

# Add:

# * Instance method `deposit(amount)`
# * Class method `change_bank_name(new_name)`

# 👉 Deposit money into one account
# 👉 Change bank name
# 👉 Print details of two accounts

# ---

# ## 🔴 Question 5 (Real OOP Thinking)

# Create a class **Product** with:

# * Class property: `tax_rate = 0.18`
# * Instance properties: `name`, `price`

# Add:

# * Instance method `final_price()` → returns price + tax
# * Class method `update_tax_rate(new_rate)`

# 👉 Create two products
# 👉 Update tax rate
# 👉 Print final price for both

# ---

# ## Rules for practice 🧠

# * Use `self` correctly
# * Use `cls` for class methods
# * Don’t hardcode values inside methods
# * Run the code

# ---




######################################################## Solutions #########################################################
# class Company:
#     company_name = "TechCorp"
    
#     def __init__(self,employee_name, employee_id):
#         self.employee_name = employee_name
#         self.employee_id = employee_id
        
# employee1 = Company("Shlok",22)
# employee2 = Company("Rohit",12)

# print(f"{Company.company_name} - {employee1.employee_name} ({employee1.employee_id})")
# print(f"{Company.company_name} - {employee2.employee_name} ({employee2.employee_id})")


# class Student:
#     school_name = "ABC School"
    
#     def __init__(self,name):
#         self.name = name
        
#     @classmethod   
#     def change_school(cls,new_name):
#         cls.school_name = new_name
        
# s1 = Student("Shlok")
# s2 = Student("Rohit")

# print(s1.school_name)
# print(s2.school_name)

# Student.change_school("XYZ School")

# print(s1.school_name)
# print(s2.school_name)

# class User:
#     total_users = 0
    
#     def __init__(self,username):
#         self.username = username
#         User.total_users += 1
        
# u1 = User("Shlok")
# u2 = User("Rohit")

# print(f"Total users: {User.total_users}")

# class BankAccount:
#     bank_name = "Python Bank"
    
#     def __init__(self,account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance
    
#     def deposite(self, amount):
#         self.balance += amount
        
#     @classmethod
#     def change_bank_name(cls,new_name):
#         cls.bank_name = new_name
        
# p1 = BankAccount("Shlok",500)
# p2 = BankAccount("Rohit",5000)

# print(p1.bank_name)

# BankAccount.change_bank_name("JS Bank")

# print(p1.bank_name)

# print(p1.balance)
# p1.deposite(100)
# print(p1.balance)

class Product:
    tax_rate = 0.18
    
    def __init__(self,name, price):
        self.name = name
        self.price = price
        
    def finalprice(self):
        return self.price + (self.price * Product.tax_rate)
    
    @classmethod
    def update_tax_rate(cls,new_rate):
        cls.tax_rate = new_rate

p1 = Product("Milk",20)

print(p1.tax_rate)
Product.update_tax_rate(0.20)
print(p1.tax_rate)

print(p1.finalprice())
