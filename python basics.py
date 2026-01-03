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
print()
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
print()

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

print()

# looping through a list
for fruit in fruits:
    print(fruit)       

for fruit in fruits:
    print(fruit , len(fruits))