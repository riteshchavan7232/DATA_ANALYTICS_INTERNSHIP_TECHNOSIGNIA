
# CONDITIONAL STATEMENTS

#1 if statement
age = 23
if age >= 18:
    print("Eligible to vote")


#2 if else statement
marks = 35
if marks >= 40:
    print("Pass")
else:
    print("Fail")


#3 if elif else statement
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")


# LOOPS

#1 for loop
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)


#2 Calculate total using for loop
numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total = total + number
print("Total:", total)


#3 while loop
count = 1
while count <= 5:
    print(count)
    count = count + 1


#4 Calculate total using while loop
numbers = [10, 20, 30, 40, 50]
total = 0
count = 0
while count < len(numbers):
    total = total + numbers[count]
    count = count + 1

print("Total:", total)


# COLLECTIONS

#1 List
numbers = [10, 20, 30, 40, 50]
print(numbers)


#2 Tuple
numbers = (10, 20, 30, 40, 50)
print(numbers)


#3 Set
numbers = {10, 20, 30, 40, 50}
print(numbers)


#4 Dictionary
student = {
    "name": "Ritesh",
    "age": 23,
    "city": "Rahuri"
}
print(student)


# FIND MAXIMUM VALUE
numbers = [25, 10, 50, 35, 15]
maximum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
print("Maximum value:", maximum)


# REMOVE DUPLICATE VALUES
numbers = [10, 20, 10, 30, 20, 40, 30]
unique_numbers = set(numbers)
print("Original list:", numbers)
print("Unique values:", unique_numbers)


# COUNT CATEGORIES
departments = [
    "IT",
    "HR",
    "IT",
    "Sales",
    "HR",
    "IT"
]

category_count = {}
for department in departments:
    if department in category_count:
        category_count[department] = category_count[department] + 1
    else:
        category_count[department] = 1
print("Category count:", category_count)


# FUNCTIONS

#1 Simple function
def greet():
    print("Hello Ritesh")

greet()


#2 Calculate total using function
def calculate_total(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


sales = [100, 200, 300, 400, 500]

total_sales = calculate_total(sales)

print("Total sales:", total_sales)


#3 Find maximum value using function
def find_maximum(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


numbers = [25, 10, 50, 35, 15]

maximum = find_maximum(numbers)

print("Maximum value:", maximum)
