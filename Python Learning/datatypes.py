#Numerical datatypes............... (int, float, complex)
a = 10
print(a)  #results value of a
print(type(a))  #results type of a

b = 10.5
print(b)  #results value of b
print(type(b))  #results type of b

c = 3 + 4j
print(c)  #results value of c
print(type(c))  #results type of c



#String datatypes............... (str)
a = "Hello"
print(a)  #results value of a
print(type(a))  #results type of a



#Boolean datatypes............... (bool)
a = True
print(a)  #results value of a
print(type(a))  #results type of a

b = False
print(b)  #results value of b
print(type(b))  #results type of b



#Sequence datatypes............... (list, tuple, range)
#List
a = [1,2,3,4,5]  # List is a collection which is ordered and changeable(Mutable). Allows duplicate members.
print(a)  #results value of a
print(type(a))  #results type of a

#Tuple
b = (1,2,3,4,5)  # Tuple is a collection which is ordered and unchangeable(Immutable). Allows duplicate members.
print(b)  #results value of b
print(type(b))  #results type of b

#Range
c = range(5)  # Range is a collection which is ordered and unchangeable(Immutable). Does not allow duplicate members.
print(c) 
b = list(c)  # Convert range to list
print(b)
b[2]=10 # Change the value of the 3rd element in the list
print(b)



#Set datatypes............... (set, frozenset)
#Set
a = {1,2,3,4,5}  # Set is a collection which is unordered and unindexed. No duplicate members.Mutable.
print(a)  #results value of a
print(type(a))  #results type of a 


#Frozenset
b = frozenset([1,2,3,4,5])  # Frozenset is a collection which is unordered and unindexed. No duplicate members. It is immutable.
print(b)  #results value of b
print(type(b))  #results type of b



#Mapping datatypes............... (dict)
a = {"name": "John", "age": 30, "city": "New York"}  # Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
print(a)  #results value of a
print(type(a))  #results type of a



#None datatypes............... (NoneType)
a = None  # None is a special data type that represents the absence of a value or a null value.
print(a)  #results value of a
print(type(a))  #results type of a



#Binary datatypes............... (bytes, bytearray, memoryview)
#Bytes  
a = b"Hello, World!"  # Bytes is a collection of bytes. It is immutable.
print(a)  #results value of a
print(type(a))  #results type of a

#Bytearray
b = bytearray([1,2,3,4,5])  # Bytearray is a collection of bytes. It is mutable.
print(b)  #results value of b
print(type(b))  #results type of b

#Memoryview
c = memoryview(a)  # Memoryview is a buffer protocol that allows you to access the internal data of an object that supports the buffer protocol.
print(c)  #results value of c
print(type(c))  #results type of c

#=====================================================================================

a ="a"
a=ord(a)  # Convert string to ASCII value
print(a)  #results value of a
print(type(a))  #results type of a
#Throws an error because the string "a" cannot be converted to an integer.Only integer strings can be converted to integers.  
# For example, "10" can be converted to 10, but "a" cannot be converted to an integer.
#If you need to convert that character string to ASCII value, you can use the ord() function. For example, ord("a") will return 97, which is the ASCII value of "a".
#If you want to convert a integer number to character, you can use the chr() function. For example, chr(97) will return "a", which is the character representation of the ASCII value 97.
#If you need to convert that string to a number, you can use the int() function with base 36. For example, int("a", 36) will return 10, which is the base 36 representation of "a".

from os import name  
import sys

z = 3 + 4j
k = [1,2,3,4]
print(type(z))
print(len(k))
print(sys.getsizeof(k))
print(sys.getsizeof(z))
print(sys.getsizeof(3))

print(sys.getsizeof(""))  #empty str size is 49
print(sys.getsizeof("abc"))  #here str has 3 characters so size is 52  (49 + 3 = 52)

m = ("app", "ban", "cat")
n = ("app", "ban", "cat")
print(m is n)
print(sys.getrefcount(m))


f = open("file_command.txt", "w")
print("file_command", file=f)
f.close()


#swapping of two numbers using bitwise XOR operator
a = 10
b = 20
a = a^b
b = a^b
a = a^b
print(a, b)  #results value of a and b



import sys

lst = []

for i in range(10):
    lst.append(i)
    print(f"Length = {len(lst):2}, Size = {sys.getsizeof(lst)} bytes")


import sys
print(sys.getsizeof(name))   #returns the size of the object in bytes. The size of an object is the amount of memory that it occupies in the computer's memory. The size of an object can vary depending on the type of object and the data that it contains. For example, a string object will typically be larger than an integer object because it contains more data. The size of an object can also vary depending on the implementation of Python that you are using. For example, the size of an object may be different in CPython than it is in PyPy.
print(sys.version) #returns the version of the Python interpreter that is currently running. The version of Python is important because it determines which features and libraries are available to you. For example, some features may only be available in Python 3.6 or later, while others may only be available in Python 2.7 or earlier. The version of Python can also affect the performance of your code, as newer versions of Python may have optimizations that make your code run faster.



