#PYTHON VARIABLES
name = "Ritesh"
age = 23
salary = 25000

print(name)
print(age)
print(salary)


#PYTHON DATATYPES
# 1 INTEGER
age = 23
print(age)
print(type(age))

#2 FLOAT
price = 99.50
print(price)
print(type(price))

#3 STRING
city = "Rahuri"
print(city)
print(type(city))

#4 Boolean
is_student = True
print(is_student)
print(type(is_student))

# OPERATORS

#1  Arithmetic operators
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)

#2 Comparison operators
a = 10
b = 5
print(a > b)
print(a < b)
print(a == b)
print(a != b)

#3 Logical operators
age = 23
print(age > 18 and age < 30)
print(age < 18 or age > 20)
print(not age > 18)

# Input and output
name = input("Enter your name: ")
print("Hello", name)

# Calculate percentage
marks = 80
total_marks = 100
percentage = marks / total_marks * 100
print("Percentage:", percentage)

# Calculate sales total
price = 100
quantity = 5
total = price * quantity
print("Total sales:", total)

# Calculate discount
price = 1000
discount = 10
discount_amount = price * discount / 100
final_price = price - discount_amount
print("Discount:", discount_amount)
print("Final price:", final_price)

#  Calculate average
a = 70
b = 80
c = 90
average = (a + b + c) / 3
print("Average:", average)
