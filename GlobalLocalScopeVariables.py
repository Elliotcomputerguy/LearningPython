#!/bin/usr/env python

# #Variables in the global and local scope
# Every time a function is called, a local scope is created. Variables created during a function call exist in the local scope.
# Parameters always exist in a local scope. When a function returns, the local scope is destroyed and all variables are forgotten. 
# A variable in the local scope is still a sperate variable from a global scope variable even if the two variables have the same name.
# Variables created outside of every function exist in a global scope. When the program exits, the global scope is destroyed and all
# variables in the program are forgotten. 

# #Global Statement
# If you want a variable that is inside of a function to be a global variable you use the global statement with the variable name as the
# first line after the def statement. 

# Rules

# 1) Variables outside of all functions are always global variables.
# 2) If a variable in a function is never used in an assigment statement, it is a global variable.
# 3) If a variable in a function is not used in a global statement; but is used in an assigment statement, it is a local variable
# 4) If a variable in a function is used in a global statement, it is a global variable when used in that function.

# ===============================================================
# Example:

var = 42 # global variable

def func():
    var = 99 # var in this function is local
    print('In func():', var)

def func1():
    print('In func1():', var) # var in this function is global

def func2():
    global var # var in this function is global
    print('In func2():', var)

param = 54

def func3(var):
    var = 0
    print('In func3():', param, + var) # param is global and var in this function is local

print(var)    
func()
print('----------')
print(var)
func1()
print('----------')
print(var)
func2()
print('----------')
print(var)
func3(param)
print('----------')