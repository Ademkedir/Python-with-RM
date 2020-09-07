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
    '''

    
