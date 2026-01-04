# revising basic Python concepts

# variables and data types
name = "Yogesh"
age = 20
val = 3.14
s = True
print(name)
print(age)
print(type(name))
print(type(age))
print(type(val))
print(type(s))
print('----------------------')


# string functions

text = "Hello, world!"

print(len(text)) 
print(text.lower())
print(text.upper())
print(text.title())  
print(text.count("o"))   
print(text.find("lo"))   
print(text.replace("world", "Python"))
print(text.split(", "))
print('----------------------')


# list operations

fruits = ["apple", "banana", "cherry", "grape", "mango"]

fruits.append("orange")           # adding an item
print(fruits)
fruits.remove("banana")           # removing an item
print(fruits)       
print(fruits[0])                  # accessing an item
print(fruits[1:3])                # slicing the list
fruits.sort()                     # sorting the list
print(fruits)
fruits.reverse()                  # reversing the list
print(fruits)
print(len(fruits))                  # length of the list

print('----------------------')

# looping through a list
for fruit in fruits:
    print(fruit)       

for fruit in fruits:
    print(fruit , len(fruits))

print('----------------------')

# tuple operations

courses = ("Ba", "Bcom", "Bsc", "Btech", "Bca")
print(courses)
print(type(courses))

print(courses[1])               # accessing an item

print(len(courses))              # length of the tuple
print(courses.count("Bsc"))     # counting occurrences
print(courses.index("Btech"))   # finding index of an item

for course in courses:        # looping through a tuple
    print(course)

for id, course in enumerate(courses):
    print(id, course)

print('----------------------')


# dictionary operations
student = {
    "name": "Yogesh",
    "age": 20,
    "student_id": "12345",
    "subjects": ["Math", "Science", "History"]
}
print(student)
print(type(student))

print(student["name"])               # accessing a value
print(student.get("age"))           # accessing a value using get()
print(len(student))     # length of the dictionary

student["age"] = 21                 # updating a value
print(student)

student.pop("student_id")            # removing a key-value pair
print(student)                       #del also can be used
# clear() can be used to empty the dictionary

for item in student:          # looping through keys
    print(item)

for key, value in student.items():   # looping through key-value pairs
    print(key, value)

print('----------------------')


# set operations
colors = {"red", "green", "blue"}
print(colors)
print(type(colors))

colors.add("yellow")            # adding an item
print(colors)
colors.remove("green")         # removing an item
print(colors)
print(len(colors))               # length of the set

for color in colors:          # looping through a set
    print(color)

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(setA.union(setB))          # union
print(setA.intersection(setB))   # intersection
print(setA.difference(setB))     # difference
print(setA.symmetric_difference(setB))  # symmetric difference

print('----------------------')


# Functions
def hello(name):
    return f"Hello, {name}!"
print(hello("Yogesh"))
print(hello(18))
print(type(hello))

def add(a, b):
    return a + b
A = add(5, 10)
print(A)

print('----------------------')


# Conditional statements

# if statement
num = 10
if num > 0:
    print(f"{num} is positive")
print()

# if-else statement
a = 5
b = 10
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")

print()

# if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

print('----------------------')


# loops
# for loop - iterating over a range of numbers 
for i in range(5):
    print(i)

# it can also iterate over a string, list, tuple, dictionary, or set as shown above in previous examples
print('--------')
# break and continue
for i in range(10):
    if i == 5:
        break               # exit the loop when i is 5
    print(i)

print('--------')

for i in range(10):
    if i % 2 == 0:
        continue                # skip the current iteration and move to the next according to the condition
    print(i) 

print('----------------------')

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

i = 0  
str1 = 'Beautiful'  
  
while i < len(str1):   
    if str1[i] == 't':   
        i += 1  
        break  
    print('Current Letter :', str1[i])   
    i += 1 

print('----------------------')


# Class and Objects
class Student:                                         # defining a class
    def __init__(self, name, age):
        self.name = name                               # initializing attributes
        self.age = age

    def display_info(self):                                # method to display student info
        return f"Name: {self.name}, Age: {self.age}"
    
student1 = Student("Yogesh", 20)                       # creating an object
print(student1.display_info())                         # calling a method


print('----------------------')



