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
# You will need to import Path from pathlib. from pathlib import * 'or Path'
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

strPathFileList = [

    strPath / 'file1.jpg',
    strPath / 'file2.txt',
    strPath / 'parent1' / 'parent2' / 'file.py',
    strPath / 'parent1' / 'file.json',
]

print(strPathList)

for dir in strPathList:
    dir.touch()

# create multiple directories from a list

strPathDir = pathlib.Path.home()

strPathDirList = [

    strPathDir / 'DirM',
    strPathDir / 'DirN' / 'DirO',
    strPathDir / 'DirP',

]

for dir in strPathDirList:
    dir.mkdir(exist_ok=True, parents=True)

# ===============================================================
# Iterating over the contents of a (single directory) is possible with pathlib iterdir().
# ===============================================================
# Example

strPath = pathlib.Path.home() / 'parent1' / 'parent2' / 'parent3' #<------------- Create path object 
strPath.mkdir(exist_ok=True, parents=True) #<-------------- create the directories with mkdir()
file = strPath / 'file1.txt' #<-------------------- join the absolute path with the relative path
file.touch()

# iterate over directories from a list
strPath = pathlib.Path.home()

strPathList = [
    strPath / 'parent1',
    strPath / 'parent1' / 'parent2',
    strPath / 'parent1' / 'parent2' / 'parent3',
]

for srchItem in strPathList:
    strList = list(srchItem.iterdir())
    for foundItem in strList:
        print(foundItem)

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
# To delete files the unlink() method is used. To delete directories the rmdir() method is used. The rmdir() method requires the 
# directory to be empty so you must delete the files first. The shutil() module that includes a rmtree() function can be used 
# to delete directories with files. 
# ===============================================================
# Example

# Create nested directories and a file
strPathSource = pathlib.Path.home() / 'dirA' / 'dirB' #<----- Create the path object with two directories
strPathSource.mkdir(exist_ok=True, parents=True) #<------- make the new directories 
file = strPathSource / 'file1.txt' #<---------- create a file object and assign the path to variable file
file.touch() #<----------- create the file

# Move a file 
strPathSource = pathlib.Path.home() / 'dirA' / 'dirB' / 'file1'
strPathDest = pathlib.Path.home() / 'dirA' / 'file1.txt' #<-------- Destination to where we want to move the file
if not strPathDest.exists():   
    strPathSource.replace(strPathDest)  #<--------------------- replace the file from source to destination 
    if strPathDest.exists():
        print(strPathDest)

# Rename a directory
strPathSource = pathlib.Path.home() / 'dirA' #<----------------- Current directory name
strPathDest = pathlib.Path.home() / 'dirC' #<---------------------- New directory name
if not strPathDest.exists():
    strPathSource.replace(strPathDest)
    if strPathDest.exists():
        print(strPathDest)

# Remove a file 
strPathDir = pathlib.Path.home() / 'dirC'
strPathDir.mkdir(exist_ok=True, parents=True)
filePath = strPathDir / 'file.txt'
filePath.touch()

print(f'[+] Locating file in directory [{filePath}]')
if filePath.exists():
    for path in strPathDir.iterdir():
        print(f'[+] file {filePath.name} located')
    print(f'[+] Removing file in directory [{filePath}]')
    filePath.unlink()
    filePath = strPathDir / 'file.txt'
    if filePath.exists():
        print(f'[-] file [{filePath.name}] has failed to be removed.')
    else:
        print(f'[+] file [{filePath.name}] has been removed successfully.')

# Remove empty directory
strPathDir = pathlib.Path.home() / 'dirC'
strPathDir.mkdir(exist_ok=True, parents=True)

print('[+] Locating Directory.')
if strPathDir.exists():
    print(f'[+] Directory [{strPathDir}] located.')
    print(f'[+] Removing directory [{strPathDir}].')
    strPathDir.rmdir()
    if strPathDir.exists():
        print(f'[-] Directory [{strPathDir}] has failed to be removed.')
    else:
        print(f'[+] Directory [{strPathDir}] has been removed successfully.')

# Remove directory with files using shutil 
import shutil

strPathDir = pathlib.Path.home() / 'dirC'
strPathDir.mkdir(exist_ok=True, parents=True)
file = strPathDir / 'file.txt'
file.touch()

print('[+] Locating Directory.')
if strPathDir.exists():
    print(f'[+] Directory [{strPathDir}] located.')
    for path in strPathDir.iterdir():
        print(f'[+] Removing files [{path.name}] ')
    print(f'[+] Removing directory [{strPathDir}].')
    shutil.rmtree(strPathDir)
    strPathDir = pathlib.Path.home() / 'dirC'
    if strPathDir.exists():
        print(f'[-] Directory [{strPathDir}] has failed to be removed.')
    else:
        print(f'[+] Directory [{strPathDir}] has been removed successfully.')

# ===============================================================
# When reading and writing data types using python file objects you can read and write entire files or just one line or even just a character. 
# Python file objects will do all the encoding and decoding. files are made up of bits that make bytes. There is 8 bits to a byte. 
# Unlike networks where throughput speeds are measured in bits.
# data types such as files etc are measured in bytes. When Data types are written to a storage medium. They are written in 
# a sequence of bytes. Some use two bytes. As the computer processes the data type it can only work with binary bits 1's and 0's.
# The processor uses an encoding scheme to decode from binary into a human readable format based upon the encoding scheme. 
# When a line of text is written to a file it will end with a line ending. There are two character flags that mark the line as ended, 
# known as a carrige return \r and a line feed \n. They are interpreted slightly differntly to each operating system but Python will 
# resolve line ending automatically. 

########################################################
#   Mode   |              Description
#   'r'    | Creates a file object for reading
#   'w'    | Creates a file object for writing
#   'a'    | Creates a file object for appending
#   'rb'   | Creates a binary file object for reading
#   'wb'   | Creates a binary file object for writing
#   'ab'   | Creates a binary file object for appending
#########################################################

######################################
#  String          Encoding          #
######################################
# 'ascii'           ASCII
# 'utf-8'           UTF-8
# 'utf-16'          UTF-16
# 'utf-32'          UTF-32
######################################

# To create a file object you can use the built-in open() function or the Path.open() method. 
# ===============================================================
# Example

# The built-in open() function uses three parameters. Create a variable and assign the path to the file. 

strPath = pathlib.Path.home() / 'text1.txt'
strPath.touch()
fileObject = open(strPath, mode = 'r', encoding='utf-8')
print(fileObject.read())
fileObject.close()

# Path.open() method uses the Path class. You will need to create a path object in order to open a file. There are two keyword 
# parameters. mode and the encoding parameter. When you open a file you need to explicitly tell python to close the file.

from pathlib import *

strPath = pathlib.Path.home() / 'text1.txt'
strPath.touch()
fileObject = strPath.open(mode = 'r', encoding='utf-8')
print(fileObject.read())
fileObject.close()

# ===============================================================
# Using the with statement the close() method is not required and python will close the file automatically.
# This is best practice allowing Python to close the file rather than you explicitly writing the close statement which 
# could potenetionaly leave you working with a closed file when you did not intend to close it or your program crashes
# and leaves the file open which could lead to data coruption. 
# ===============================================================
# Example

from pathlib import *
strPath = pathlib.Path.home() / 'text1.txt'
strPath.touch()

with strPath.open(mode='r', encoding='utf-8') as fileObject:
    ReadFile = fileObject.read()
print(ReadFile)

# ===============================================================
# Reading data from a file with the read() method reads the contents and will return the content as a string.
# Each line of text in the file is seperated with a newline character \n. If you assign the string into a list you will see 
# the newline character. 
# ===============================================================
# Example Setup

strPath = pathlib.Path.home() / 'text1.txt'
if not strPath.exists():
    strPath.touch()
with strPath.open(mode='w', encoding='utf-8') as fileObject:
	newList = (fileObject.write('hello world\nhellow World'))

# ===============================================================
# Example 

with strPath.open(mode='r', encoding='utf-8') as fileObject:
	newList = (fileObject.read())

print(newList) #<--- 'hello world\nhello world'

# ===============================================================
# To remove the newline character you can use .rstrip() 
# ===============================================================
# Example 

with strPath.open(mode='r', encoding='utf-8') as fileObject:
	newList = (fileObject.read().rstrip())

print(newList) #<---- 'hello world hello world'

# ===============================================================
# You can also read the line by line rather than the whole file using a for loop. It will store each line of the text
# file into a list and print out exactly how it is input into the file. Again the newline characters are present and have to be striped. 
# ===============================================================
# Example

with strPath.open(mode='r', encoding='utf-8') as fileObject:
    print(fileObject.readlines()) #<--- ['hello world\n', 'hello world']

    for file in fileObject.readlines(): #<----------------------- Due to the newline character it will create unwanted white space that
        print(file) #<------------------- hello world             can be removed with the rstrip() or use the end paramater in print. 
                            
                                        # hello world

    for file in fileObject.readlines():
        print(file.rstrip())

    for file in fileObject.readlines():
        print(file, end='')

# ===============================================================
# To write data to a file you use the write() method and set the mode to write. When you use the write method 
# it will overwrite any contents already existing in the file. If you want to add to a file use the mode append. 
# You can only write strings to text files. If you want to write integer values you will have to convert them to a string data type.
# ===============================================================
# Example

strPath = pathlib.Path.home() / 'text1.txt'

with strPath.open(mode='w', encoding='utf-8') as fileObject:
	newList = (fileObject.write('hello world\nhellow World'))

with strPath.open(mode='a', encoding='utf-8') as fileObject:
	newList = (fileObject.write('hello world\nhellow World'))

# ===============================================================
# writing lines from a list to a file, reading the file and replacing words from the file with a list of words.
# ===============================================================
# Example

from pathlib import *
strPath = pathlib.Path.home() / 'text1.txt'
if not strPath.exists():
    strPath.touch()

someText = [
    'hello world\n',
    'hello world\n',
    'hello world\n',
]

with strPath.open(mode='w', encoding='utf-8') as fileObject:
    fileObject.writelines(someText)
with strPath.open(mode='r', encoding='utf-8') as fileObject:
    print(fileObject.read())

words = ['hello', 'world',]
changeWords = ['hey', 'good bye']
newString=''
counter = 0
with strPath.open(mode='r', encoding='utf-8') as fileObject:
    for file in fileObject.readlines():
        newString += file.replace(words[counter], changeWords[counter])
        counter += 1
        if counter > 1:
            counter = 0
print(newString)
with strPath.open(mode='w', encoding='utf-8') as fileObj:
    fileObj.write(newString)
with strPath.open(mode='r', encoding='utf-8') as fileObj:
    print(fileObj.read())

# ===============================================================
# Counting words in a file can be done with the split method where we put all the words into alist.
# ===============================================================
# Example

def countWords(file, drive):
    ''' count words in file'''
    import pathlib
    from pathlib import Path
    rootPath = pathlib.Path(drive)
    if not rootPath.exists():
        driveNotFound = f'[-] {drive} does not exist. Cannot locate {file}'
        return driveNotFound
    else:
        for searchPath in rootPath.rglob(file):
            absPath = searchPath
            if absPath.exists():
                print(f'[+] located absolute path {absPath.parents[0]}')
                print(f'[+] located file {file}')
                print(f'[+] Counting words in {file}')
                with absPath.open(mode='r', encoding='utf-8') as fileObj:
                    countWords = fileObj.read().split()
                    counted = f'[+] in {file} there is {len(countWords)} words'
                    return counted
        
        fileNotFound = f'[-] {file} does not exist. Cannot locate {file} in {drive}'
        return fileNotFound

def callCountWords():
    DRIVE_LETTERS = ['a','b','c','d',',e',
        'f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t',
        'u','v','w','x','y','z',
        ]

    userInputfile = ''
    userInputDrive = ''

    while not userInputfile and not userInputDrive:
        userInputfile = input('Enter file name including suffix:>')
        userInputDrive = input('Enter single drive letter the file can be located at:>').lower().strip()
    while userInputDrive not in DRIVE_LETTERS:
        userInputDrive = input('You have not entered a letter :>')
    userInputDrive += ':/'
    print(countWords(userInputfile, userInputDrive))


callCountWords()

#import os

#def find(name, path):
#    for root, dirs, files in os.walk(path):
#        if name in files:
#            return os.path.join(root, name)

#print(find('PythonText.txt', 'c:\\'))