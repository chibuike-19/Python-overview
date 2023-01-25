import math

print("Hello World")
students_count = 1000
rating = 4.99
is_published = True
course_name = "Python \Programming"
department = "Computer Engineering"
message = """
HI, my name is john from bloomberg i got the invite"""
print(len(course_name))
print(course_name[0:4])

# Built in primitive types in python
# strings
# numbers
# boolean


# formatted string
full = f"{course_name} {department}"
print(full)

# String Methods
print(course_name.upper()) 
print(course_name.lower())
print(course_name.title())
print(course_name.strip())
print(course_name.find("ro"))
print("go" not in course_name)

# Type conversions
# bool()
# int()
# float()

x = input("Enter a number: ")
y = int(x) + 1

# Falsy values in python
# ""
# 0
# None