# # #Variables
# student_name = "Ali"
# student_age = 20
# cgpa = 3.5
# is_active = True
# print(student_name)
# print(student_age)
# print(cgpa)
# #Type conversion
# age = "20"
# age = int(age)
# print(age + 5)
#  #create class
# class StudentRecord:

#     def __init__(self, id, name, age):
#         self.id = id
#         self.name = name
#         self.age = age

#     def display(self):
#         print(self.id, self.name, self.age)


# s1 = StudentRecord(1, "Ali", 20)
# s1.display()


# # # Inheritance part
# class Person:

#     def __init__(self, name):
#         self.name = name


# class Student(Person):

#     def __init__(self, name, roll_no):
#         super().__init__(name)
#         self.roll_no = roll_no

#     def show(self):
#         print(self.name, self.roll_no)


# s = Student("Ahmed", 101)
# s.show()
# # List
# students = ["Ali", "Akbar","Hussein","Hassan"]
# print(students)
# # Tuple
# subjects = ("Python", "AI", "CV")
# print(subjects)
# #Dictionary
# student = {
#     "id": 1,
#     "name": "Ali",
#     "age":"20"
# }
# print(student)
# #Functions
# def add(a, b):
#     return a + b

# result = add(5, 3)

# print(result)
# students = []

# while True:

#     print("\n1 Add Student")
#     print("2 View Students")
#     print("3 Exit")

#     choice = input("Enter Choice: ")

#     if choice == "1":

#         name = input("Enter Name: ")
#         age = int(input("Enter Age: "))

#         student = {
#             "name": name,
#             "age": age
#         }

#         students.append(student)

#     elif choice == "2":

#         for s in students:
#             print(s)

#     elif choice == "3":
#         break

#     else:
#         print("Invalid Choice")
# # Excepion Handling
# try:

#     age = int(input("Enter Age: "))

# except ValueError:

#     print("Age must be number")
# # File write
# file = open("students.txt", "w")

# file.write("Ali")

# file.close()
# # File read
# file = open("students.txt", "r")

# data = file.read()

# print(data)

# file.close()

# csv write file
#import csv
# with open("students.csv", "w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Name", "Age"])
#         writer.writerow(["Ali", 20])
#         writer.writerow(["Ahmed", 22])

# csv read file
#import csv
# with open("students.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
#json file write
import json
student = {
    "name": "Ali",
    "age": 20,
    "cgpa": 3.5
}
with open("student.json", "w") as file:

    json.dump(student, file)
#json file read
import json

with open("student.json", "r") as file:

    data = json.load(file)

print(data)


