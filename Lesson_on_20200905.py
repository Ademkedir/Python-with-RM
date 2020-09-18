# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:36:46 2020

@author: adeke
"""

cls = lambda: print("\033[2J\033[;H", end='')

cls()

# =============================================================================
# def sum(array):
#     s = 0 #initialization
#     
#     for x in array:
#         s = s + x
#     return s
# 
# array = [5, 7, 6, 2, 8]
# total = sum(array)
# 
# print("The sum of {}".format(array),total)
# =============================================================================

#20200905

# =============================================================================
# a = [1, 2, 3]
# b=a
# 
# a.append(4)
# b
# print(a)
# print(b)
# b.append(6)
# print(a)
# 
# =============================================================================
#an example of a function
data=[1,2,3]
def append_element (some_list, element,element2):
    some_list.append(element)
    some_list.append(element2)
    x=[1,2,3]
    x.append(4)
    x.append('asd')
    print(x)
    data=['a','b','c']
    print(data)
append_element(data,4,5)


x=12

print(x)
print(data) 
'''
Summary From 9/5
1. Pass by value V Pass by Reference
Python uses Pass by Reference way of assigning values
see example above
2. Scope of a variable: changing a variable inside v outside a function
a. Local Scope: 
b. Function Scope:scope is within a function
c. Parent Scope: Scope is outside the function
3. Variable and Object assignment:
4. the following 2 lines clean up console by removing previous outputs as well as directory
a. cls = lambda: print("\033[2J\033[;H", end='')

b. cls()
    '''
#20200907
'''
Note from 20200907
How does memory work?
1. Bit V bite
2. RAM
3. ASCII V Unicode
4. Dynamic references
5. Exercise on type: how to get the type for an object
example: X=5 
    in this example X is a variable
    5 is a value or object 
Array List: remember that list positions in Python start from 0 (not 1)
   Example 2: write an instance 
   
   NOte to self: create a few samples in order to drill 

def isString(inpt):
    return isinstance(inpt, str)
def isFloat(inpt):
    return isinstance(inpt,float)
    
'''
cls = lambda: print("\033[2J\033[;H", end='')

cls()
# =============================================================================
# 
# x=[1,2,3]
# type(x)
# y=[1,2,('adem')]
# print(type(y))
# y.type
# x=(Adem
# =============================================================================


# =============================================================================
# %run Hello_Python.py
# =============================================================================

#!/usr/bin/python

# Function definition is here
# =============================================================================
# def printinfo( name, age ):
#    "This prints a passed info into this function"
#    print "Name: ", name
#    print "Age ", age
#    return;
# 
# # Now you can call printinfo function
# printinfo( age=50, name="miki" )
# =============================================================================
cls = lambda: print("\033[2J\033[;H", end='')

cls()
#Practice on Functions
# =============================================================================
# def printme( str ):
#    ("This prints a passed string into this function")
#    print (str)
#   
# printme( str = "My string")
# 
# def write_me (str):
#     print (str)



#     
# write_me (str="this is America")
# 
# def write_me_trice(bota):
#     print (bota)



#   
# write_me_trice(bota=" 3 function")
# #more examples
# 
# def printinfo (name, age):
#     print ("Name:" , name)
#     print("age:", age)
#     
# printinfo (age=50, name='Wagaye Legesse')
# 
# 
# def printinfo2 (name, race):
#     print ("name:",name)
#     print ("race:",race)
# 
# printinfo2 (name='adem', race='Tikur') 
# =============================================================================
#?data
# =============================================================================
# a=("this is 123")
# print (a)
# =============================================================================
cls = lambda: print("\033[2J\033[;H", end='')

cls()
def myfunction3(str):
    print (str)
    
myfunction3(str='this is 012')
print (str) 

# =============================================================================
# 
# Objects in Python typically have both attributes (other Python objects stored “inside”
# the object) and methods (functions associated with an object that can have access to
# the object’s internal data). Both of them are accessed via the syntax
# obj.attribute_name:
#   Imports
# In Python a module is simply a file with the .py extension containing Python code.
# Suppose that we had the following module:
# =============================================================================

#Operation

# =============================================================================
# a + b Add a and b
# a - b Subtract b from a
# a * b Multiply a by b
# a / b Divide a by b
# a // b Floor-divide a by b, dropping any fractional remainder
# a ** b Raise a to the b power
# a & b True if both a and b are True; for integers, take the bitwise AND
# a | b True if either a or b is True; for integers, take the bitwise OR
# a ^ b For booleans, True if a or b is True, but not both; for integers, take the bitwise EXCLUSIVE-OR
# a == b True if a equals b
# a != b True if a is not equal to b
# a <= b, a < b True if a is less than (less than or equal) to b
# a > b, a >= b True if a is greater than (greater than or equal) to b
# a is b True if a and b reference the same Python object
# a is not b True if a and b reference different Python objects
# =============================================================================
cls = lambda: print("\033[2J\033[;H", end='')

cls()
# try out some of the attributes of a python object
x="hello world"
print(x)

x=("hello world")
x=x.capitalize()
print(x)

x=x.upper()
print(x)

y=[1,2,3,4]
y=y.append(5)
print(y)

z=[21,34,1,2,3,5,4,78,56]
print (z.count(1))# counts instances of 1
#print (z.pop(4))
print (z.remove(5)) #remove doesn't return a value but changes the list
print (z)
z.sort()
print (z)
#print (z.index(44,5,10)) 

# =============================================================================
# Mutable and immutable objects
# Most objects in Python, such as lists, dicts, NumPy arrays, and most user-defined
# types (classes), are mutable. This means that the object or values that they contain can
# be modified
# =============================================================================
cls = lambda: print("\033[2J\033[;H", end='')

cls()
#09/12/2020
#casting

s=3.12
fval=float(s)
type(fval)

#Import9/12/20
# =============================================================================
# Importing a function: 2 methods 
# a. import some_module 
# b. from some_module import f, g, PI
# =============================================================================

# =============================================================================
# import functions_for_import as ffi
# result=ffi.f(5)
# print (result)
# 
# result2=ffi.g(34,12)
# print(result2)
# result3=ffi.f(PI)
# print (result3)
# 
# Q for MIke
# =============================================================================

#9/14/2020
# =============================================================================
# Mutable and immutable objects
# Most objects in Python, such as lists, dicts, NumPy arrays, and most user-defined
# types (classes), are mutable. This means that the object or values that they contain can
# be modified

# Others, like strings and tuples, are immutable:
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets
# =============================================================================

#x.append(4) #example to demonstrate tuple doesnt allow appending
'''
1. Scalar Types: single value (numerical data, string, boolean(true,false))
* Numeric types: int and float
* Strings
2.bytes and Unicode
3. Booleans (True or False)
4. None: None is the Python null value type. If a function does not explicitly return a value, it
implicitly returns None
5. Date and time:The built-in Python datetime module provides datetime, date, and time type

eg.from datetime import datetime, date, time: page 45 for complete listr of date types

more on bitwise operation: https://www.geeksforgeeks.org/python-bitwise-operators/
Control Flow
'''

cls = lambda: print("\033[2J\033[;H", end='')

cls()

s='python' 

list(s)

print (s[:3]) #slicing
print(s[3:])

q=[1,2, 4,5,6,2,12]

t='Today is Ethiopian New Year, false'
print (list (t))
#The backslash character \ is an escape character,

print (6/1)

z=(1,2, 4,5,6,2,12)
a_tuple = (3, 5, (4, 5))

#20200917

cls = lambda: print("\033[2J\033[;H", end='')

cls()

s='3.14'
t='word'
type(s)

print (type (s))

fval=float(s)

print (fval)

print (type(fval))

print (type(t) )

#fval2=float(t) # as expected:could not convert string to float'

print (bool(fval))
print (bool(1)) # true
print (bool(0)) #False, why?

a = None 
a is None 
x=5

if x<0:
    print ("it's negative")
elif x==0:
    print("x is equal to Zero")
else: 
    print ("x is positive")
    

print (bool(1)) # true
# =============================================================================
# \n newline
# \s
# practice on datetime how to get time zone?
# =============================================================================
cls = lambda: print("\033[2J\033[;H", end='')

cls()

def between(a,b,v):
    return a>=v>=b

def calc_grade(g):
    if g >= 90:
        return "A"
    elif between(90,80,g):
        return "B"
    elif between(80,70,g):
        return "C"
    else:
        return "no grade"

print (calc_grade(75))
print (calc_grade(85))
print (calc_grade(90))
print (calc_grade(76))
    




 