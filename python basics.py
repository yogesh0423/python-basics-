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

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")
print(fruits)
fruits.remove("banana")
print(fruits)       
print(fruits[0])
print(fruits[-1])
