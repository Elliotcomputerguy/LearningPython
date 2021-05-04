#!/usr/bin/env python

# When reading or writing to a file with python you will need to tell python the path to the file. You can either pass the 
# absolute path which is from the root or you can use a relative path if the file is stored in the same directory as the python 
# program. There are more than one way to create path objects. You can use a string, use classes or use operator /. 
# Python has a module called pathlib that was created to be the main interface for working with file paths. pathlib was first 
# proposed (and accepted) in PEP 428. It has been around since Python 3.4. If you're still using Python 2.7, 
# a package is available on PyPI with a backport, known as pathlib2pathlib Pathlib. Pathlib enables cross compatability between different
# operating systems.
# ===============================================================
# Example:

import pathlib #<---------- Import pathlib to use the module 

# Using pathlib i can use the forward slash and it will resolve perfectly fine for Wintel directories. 
# Plus you could if you wanted use a raw string or double //.

path = pathlib.path('c:/users/ElliotStenning/Documents/python/pythontext.txt')

path = pathlib.path(r'c:\users\ElliotStenning\Documents\python\pythontext.txt') #<----- Raw string

path = pathlib.path('c:\\users\\ElliotStenning\\Documents\\python\\pythontext.txt') #<----- Double back slash

# ===============================================================
# as well as allowing you to create path objects pathlib allows you to use pathlib.Path.home() to obtain the
# users home directory. 
# ===============================================================
# Example:

print(pathlib.Path.home())

# ===============================================================
# To get the current working directory you can use the pathlib.Path.cwd() class method. 
# ===============================================================
# Example:

print(pathlib.Path.cwd())

# ===============================================================
# A filesystem path that begins at the top level directory of the file system is known as the absolute file path. 
# A filesystem path that does not start from the top level directory is called a relative file path. A relative file path
# is used when the files the application is working with are stored in the same directory as the program and ony references the local file.
# You can establish if the file path is absolute by using .is_absolute(). If you want to lengthen a relative path you can use the / operator
# ===============================================================
# Example:

absPath = pathlib.Path.home()  #<----------- absolute file path to c:\users\username
print(absPath.is_absolute())

absPathCWD = pathlib.Path.cwd() #<----------- absolute file path to current working directory
print(absPathCWD.is_absolute())

relPath = pathlib.Path('PythonText.txt') #<--------- relative file path
print(relPath.is_absolute())

print(absPath / relPath) #<--- You can lengthen the path from a relative path to an absolute path. 
                         
# ===============================================================
# When you do not know the absolute path you can use the resolve() method to create the absolute path. It will attempt to return the 
# absolute path. It is not guarenteed that it will return the absolute path.
# ===============================================================
# Example:

absPath = pathlib.Path('c:/')
relPath = pathlib.Path('/users/')
absPath = relPath.resolve()
print(absPath)

# ===============================================================
# pathlib provides a function to check all directories in the path using the parents attribute. The parent attribute will just return the 
# first parent directory. When the parents attriute is used all directories are returned in a reverse order. The parents attribute is a
# parent is a shortcut for .parents[0]. 
# ===============================================================
# Example:

absPath = pathlib.Path('c:/users/elliotstenning')
print(absPath)
parentList = list(absPath.parents)
print(parentList) #<-------- [WindowsPath('c:/users'), WindowsPath('c:/')]
for directory in parentList:
    print(directory) #<------- C:\users\
                     #<------- C:\ 
for directory in absPath.parents:
    print(directory) #<------- C:\users\
                     #<------- C:\ 
absPath.parents[0] #<--------- C:\users\
absPath.parents[1] #<--------- C:\

# ===============================================================
# 
# ===============================================================
# Example:

# But this 99% of the time does not return the absolute path unless you are working local to the directory. 
# There is another method that pathlib provides that allows you to iterate through a filesystem to locate a file called rglob. 























import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

print(find('PythonText.txt', 'c:\\'))