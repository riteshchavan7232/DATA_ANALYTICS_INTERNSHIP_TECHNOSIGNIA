
# FILE HANDLING

#1 Write text file
with open("data.txt", "w") as file:
    file.write("Hello Ritesh\n")
    file.write("Python File Handling")

print("File written successfully")


#2 Read text file
with open("data.txt", "r") as file:
    content = file.read()

print("File content:")
print(content)


#3 Append text file
with open("data.txt", "a") as file:
    file.write("\nLearning Python")

print("Data added successfully")


# CSV FILES

#1 Write CSV file
import csv

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["employee_name", "salary"])

    writer.writerow(["Ritesh", 25000])
    writer.writerow(["Rahul", 30000])
    writer.writerow(["Amit", 35000])

print("CSV file created successfully")


#2 Read CSV file
import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# ERROR HANDLING

#1 try and except
try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Please enter a valid number")


#2 Handle division error
try:
    a = 10
    b = 0

    result = a / b

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")


#3 try except finally
try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Invalid input")

finally:
    print("Program completed")


# IMPORTING MODULES

#1 Math module
import math

number = 25

result = math.sqrt(number)

print("Square root:", result)


#2 OS module
import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File does not exist")


# CSV FILE PROCESSING

# Read CSV file and handle errors
import csv
import os

filename = "employees.csv"

try:
    if os.path.exists(filename):

        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            total_salary = 0
            count = 0

            for row in reader:
                try:
                    name = row["employee_name"]
                    salary = float(row["salary"])

                    if name == "":
                        print("Invalid employee name")
                        continue

                    if salary < 0:
                        print("Invalid salary for", name)
                        continue

                    total_salary = total_salary + salary
                    count = count + 1

                    print("Employee:", name)
                    print("Salary:", salary)

                except ValueError:
                    print("Invalid salary data")

                except KeyError:
                    print("Missing column in CSV file")
                    break

            print("Total salary:", total_salary)
            print("Total employees:", count)

    else:
        print("CSV file does not exist")

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")

except OSError:
    print("File error")

finally:
    print("CSV processing completed")
