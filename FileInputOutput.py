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
from pathlib import Path #<---------- Import Path from pathlib

# Using pathlib i can use the forward slash and it will resolve perfectly fine for Wintel directories. 
# Plus you could if you wanted use a raw string or double //.

path = pathlib.Path('c:/users/ElliotStenning/Documents/python/PythonText.txt')

path = pathlib.Path(r'c:\users\ElliotStenning\Documents\python\PythonText.txt') #<----- Raw string

path = pathlib.Path('c:\\users\\ElliotStenning\\Documents\\python\\PythonText.txt') #<----- Double back slash

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
# A filesystem path that does not start from the top level directory is called a relative file path. There are special 
# names that can be used to reference direcotories. The single (.) will link to the current working directory. The double (..) will identify the parent directory.
# You can establish if the file path is absolute by using .is_absolute(). If you want to lengthen a relative path you can use the / operator.
# ===============================================================
# Example:

absPath = pathlib.Path.home()  #<----------- absolute file path to c:\users\username
print(absPath.is_absolute())

absPathCWD = pathlib.Path.cwd() #<----------- absolute file path to current working directory
print(absPathCWD.is_absolute())

relPath = pathlib.Path('/parent/PythonText.txt') #<--------- relative file path
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
# pathlib provides a function to check directories in the system path using the parent and parents attribute. While The parent attribute will 
# return the first parent directory. which is a shortcut for parents[0]. The parents attriute will return all directories 
# in the filesystem path in a reverse order. When you use the attributes parents and parent you need to pipe them into a list 
# otherwise you will not see the iterable return.   
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
# If the filepath is absolute you can use the anchor attribute to access the top level file system. anchor will return a string rather than
# a path object. If the path is relative it will return an empty string. 
# ===============================================================
# Example:

absPath = pathlib.Path('c:/users/elliotstenning')
print(absPath.anchor)

# ===============================================================
# File names consist of two parts. The name of the file called the stem and the file extention called the suffix. The attribute 
# .name will return both parts of the file including the stem and suffix. The .stem attribute will highlight the file name and the 
# .suffix will return the file extention.  
# ===============================================================
# Example:
#                               stem  suffix
#                                |    |
# C:\   users   \elliotstenning\name.txt 
#  |      |            |          |
#anchor  Parent      parent     Name 

absPath = pathlib.Path('c:/users/elliotstenning/file.txt')
print(absPath.name)
print(absPath.stem)
print(absPath.suffix)

# ===============================================================
# To check if a file exists you can use the .exists() method. The method will return a True of exists or a False if not. 
# You can also check if a filepath refers to a file or directory with the .if_file() method.
# ===============================================================
# Example

absPath = pathlib.Path('c:/users/elliotstenning/file.txt') 
print(absPath.exists())

print(absPath.is_file())

print(absPath.is_dir())

# ===============================================================
# Creating a new directory or file you can use the .mkdir() function and to create a file use the .touch() function.  
# You will need to import Path from pathlib. 
# ===============================================================
# Example

# To create a directory firstly create an absolute path and assign it to a variable. Use the / operator to create your parent directory. 
# If you want to create a nested directory you can add the 'parents=True' key argument inbetween the parentheses of mkdir(). 
# If the directories already exist you will get an error so to silence the error you can add another key argument into the mkdir()
# function 'exist_ok=True' This is an if statement equivelent. 
#                      
#                   if not strPth.exists():
#                            strPath.mkdir()

# [Single directory with file]  

strPath = pathlib.Path.home() / 'parent1'
strPath.mkdir(exist_ok=True) #<----- Will avoid the error file already exists equiv - if not strPath.exists(): strPath.mkdir()
if strPath:
    file = strPath / 'file.txt' #<-------------------------------- join the absolute path to the relative path and assign to variable
    file.touch()        #<------------------------- Create file 
else:
    print(f'{strPath} does not exist')

# [Nested directory with file]

strPath = pathlib.Path.home() / 'parent1' / 'parent2' / 'parent3'
strPath.mkdir(exist_ok=True, parents=True) #<----- Have added extra key argument parents=True to create multiple nested directories
if strPath:
    file = strPath / 'file1.txt' #<-------------------------------- join the absolute path to the relative path and assign to variable
    file.touch()        #<------------------------- Create file 
else:
    print(f'{strPath} does not exist')

# Creating multiple files from a list.

strPath = pathlib.Path.home()

strPathList = [

    strPath / 'file1.jpg',
    strPath / 'file2.txt',
    strPath / 'parent1' / 'parent2' / 'file.py',
    strPath / 'parent1' / 'file.json',
]

print(strPathList)

for dir in strPathList:
    dir.touch()

# ===============================================================
# Iterating over the contents of a single absolute path is possible with pathlib iterdir().
# ===============================================================
# Example

strPath = pathlib.Path.home() / 'parent1' / 'parent2' / 'parent3' #<------------- Create path object 
strPath.mkdir(exist_ok=True, parents=True) #<-------------- create the directories with mkdir()
file = strPath / 'file1.txt' #<-------------------- join the absolute path with the relative path
file.touch()

for path in strPath.iterdir():
    print(path)

# ===============================================================
# Locating files in directories can be achieved utilising the Path.glob() method. To search for a file you pass the 
# a wildcard character * and glob() will return any paths that signifies a pattern match to the argument passed.
# You can pass multiple search wildcards on the current directory. You can pass *2* to locate files that start with a 2. 
# name? wildcard will idenitfy anything beginning with name. combining wildcards *name.?? will bring back anything starting with name
# and followed by a dot and two more characters. The bracket [5] wilcard will only match what is in the brackets. 
# ===============================================================
# Example

strPath = pathlib.Path.home() / 'parent1' / 'parent2' / 'parent3' #<------------- Create path object 
strPath.mkdir(exist_ok=True, parents=True) #<-------------- create the directories with mkdir()
file = strPath / 'file1.txt' #<-------------------- join the absolute path with the relative path
file.touch()

for path in strPath.glob('*.txt'): #<-------------------This will bring back any file in this absolute path that matches *.txt
    print(path)

for path in strPath.glob('*.py'): #<-------------------This will bring back any file in this absolute path that matches *.txt
    print(path)

# ===============================================================
# With glob() and iterdir() they only identify the paths local to the directory that is called. Subdirectories are not identified.
# Using the ** wildcard character makes the pattern recusrive. Using '**/' tells glob() to match the current directory and subdirectories.
# rglob() is a shorthand method for recusrive matching. You do not need the wildcards.  
# ===============================================================
# Example

strPath = pathlib.Path('C:/')

for path in strPath.glob('**/*PythonText.txt'):
    print(path)

for path in strPath.rglob('PythonText.txt'):
    print(path)

# ===============================================================
# Moving directories or files use the replace() method to move directories and files. This is also can rename directories. 
# If the destination directory already exists the replace() method will over write the destination. Ensure to check that the 
# destination does not already exist.
# To delete files the uplink() method is used. To delete directories the rmdir() method is used. 
# ===============================================================
# Example

# Create the directories and a file
strPathSource = pathlib.Path.home() / 'dirA' / 'dirB' #<----- Create the path object with two directories
strPathSource.mkdir(exist_ok=True, parents=True) #<------- make the new directories 
file = strPathSource / 'file1.txt' #<---------- create a file object and assign the path to variable file
file.touch() #<----------- create the file
print(strPathSource)
strPathSource = pathlib.Path.home() / 'dirA' / 'dirB' / 'file.txt'
print(strPathSource)
strPathDestination = pathlib.Path.home() / 'dirA' / 'file.txt'
print(strPathDestination)
if not strPathDestination.exists():
    strPathSource.replace(strPathDestination)






# But this 99% of the time does not return the absolute path unless you are working local to the directory. 
# There is another method that pathlib provides that allows you to iterate through a filesystem to locate a file called rglob. 


















for path in absPath.rglob('PythonText.txt'):
    print(path)




#import os

#def find(name, path):
#    for root, dirs, files in os.walk(path):
#        if name in files:
#            return os.path.join(root, name)

#print(find('PythonText.txt', 'c:\\'))