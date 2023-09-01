#!/usr/bin/env python
# coding: utf-8

# ### How do you comment code in Python? What are the different types of comments?
# 

# In[9]:


# Any part of code Which we dpn't want to execute or want that part to be ignored by interpreter.
# Any text that follows the hash symbol(#) on the same line is consider as comment.


# This is a single-line comment in Python.

print("Hello, World!") # example

"""
This is multiline comment We use comments to notedown the process we followed.
"""


# ### What are variables in Python? How do you declare and assign values to variables

# In[10]:


# Variables in python works as a container that we use to store some values.
# A variable is essentially a name that represents a value stored in the computer's memory. 

# To declare a variable in Python, you simply choose a name for the variable and use the assignment operator (=) to assign a value to it.

x = 5
name = "John"
age = 25
is_student = True


# There are some certain rules for variable name:
# 1. A Python variable name must start with a letter or the underscore character.
# 2. A Python variable name cannot start with a number.
# 3. A Python variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
# 4. Variable in Python names are case-sensitive (name, Name, and NAME are three different variables).
# 5. The reserved words(keywords) in Python cannot be used to name the variable in Python.


# ### How do you convert one data type to another in Python?
# 

# In[14]:


## In Python,We use type conversion to change the data type of the object.
# Example: 

x = 3
print(type(x))
y = float(x)
print(y)
z = str(x)
h = bool(x)
print(z,h)
print(type(z))
print(type(h))


# ### How do you write and execute a Python script from the command line?
# 

# In[1]:


##Open a text editor (like Notepad on Windows, nano on Linux, or TextEdit on macOS) and write your Python code. Save the file with a .py extension. ##you can create a file named myscript.py and add the following code:

print("Hello, from my Python script!")


###Open a command line terminal on your computer

#On Windows: Press Win + R, type cmd, and press Enter.
#On Linux/macOS: Use the built-in terminal or press Ctrl + Alt + T


# ### Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].
# 

# In[3]:


my_list = [1,2,3,4,5]
print(my_list[1:3])


# ### What is a complex number in mathematics, and how is it represented in Python.

# In[4]:


## In mathematics, a complex number is a number that comprises both a real part and an imaginary part. It is represented in the form a + bi, 
## where a is the real part, b is the imaginary part, 
## and i is the imaginary unit, defined as the square root of -1. The real and imaginary parts are both real numbers.

z1 = 3+4j
z1_real = z1.real
z1_img = z1.imag

print(z1_real, z1_img)


# ### What is the correct way to declare a variable named age and assign the value 25 to it?
# 

# In[5]:


# you can declare a variable named age and assign the value 25 to it.
age = 25
print(age)


# ### Declare a variable named price and assign the value 9.99 to it. What data type does this variable belong to?
# 

# In[6]:


price = 9.99
print(type(price))

# this data type belongs to float variable.


# ### Create a variable named name and assign your full name to it as a string. How would you print the value of this variable?
# 

# In[7]:


name = 'Neha Singh'
print(name)


# ### Given the string "Hello, World!", extract the substring "World".
# 

# In[8]:


a = "Hello, World!"
print(a[7:])


# ### Create a variable named "is_student" and assign it a boolean value indicating whether you are currently a student or not.

# In[9]:


is_student = True
print("Is student:", is_student)


# In[ ]:




