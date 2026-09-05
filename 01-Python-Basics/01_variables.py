
# Python Variables

# 1. What is a Variable?

# A variable is a name or container used to store a value or data in a program.
# Variables allow us to store data and use it later in our program.

# Example:

name = "Nimra"
age = 20

print(name)
print(age)

""" 
In this program, we declared two variables: name and age. 
We assigned the value "Nimra" to the variable name and the value 20 to the variable age. 
We then printed the values of both variables using the print() function.
"""


# 2. Variable Declaration and Initialization

# Declaration means defining a variable name.
# Initialization means assigning an initial value to a variable.

# In Python, declaration and initialization usually happen at the same time.

student_name = "Nimra"
student_age = 20
student_marks = 85.5

print(student_name)
print(student_age)
print(student_marks)

""" 
In this program, we declared  and initialized three variables: 
student_name, student_age, and student_marks.
"""


# 3. Why Variables?
#
# Variables are used to:
# - Store data
# - Reuse data
# - Make programs easier to understand
# - Perform operations on stored values

# Example:

price = 100
quantity = 3

total = price * quantity  # this is for understanding purpose only : how to create variables and use it.

print(total)


# 4. Variable Naming Rules

# Rule 1:
# A variable name can contain letters, numbers, and underscores.

student_name = "Ali"
student1 = "Ahmed"
total_marks = 450


# Rule 2:
# A variable name cannot start with a number.

# 1student = "Ali"       # Invalid


# Rule 3:
# Spaces are not allowed in variable names.

# student name = "Ali"   # Invalid


# Rule 4:
# Variable names are case-sensitive.

name = "Nimra"
Name = "Ali"

print(name)
print(Name)


# Rule 5:
# Python keywords cannot be used as variable names.

# class = "Python"       # Invalid
# if = 10                # Invalid


# 5. Examples

# Example 1: String variable

first_name = "Nimra"

print(first_name)

# we store string values in variables using quotes (single or double).


# Example 2: Integer variable

age = 20

print(age)


# Example 3: Float variable

percentage = 85.5

print(percentage)


# Example 4: Boolean variable

is_student = True

print(is_student)


# Example 5: Multiple variables

name = "Nimra"
age = 20
city = "Sargodha"

print(name)
print(age)
print(city)


# Example 6: Multiple assignment

name, age, city = "Nimra", 20, "Sargodha"

print(name)
print(age)
print(city)


# Example 7: Updating a variable

score = 50

print(score)

score = 80

print(score)


# 6. Practice Questions

# Practice Question 1:
# Create variables for your name, age, city, and favorite language.
# Print all four values.


# Practice Question 2:
# Create two variables containing numbers.
# Add them and store the result in a third variable.
# Print the result.


# Practice Question 3:
# Create variables for:
# student_name
# student_age
# student_marks
# is_student
# Print all four values.


# Practice Question 4:
# Create variables for the length and width of a rectangle.
# Calculate and print its area.(for formula: area = length * width)


# Practice Question 5:
# Create two variables:
# first_name
# last_name
# Combine them into a full_name variable and print it.