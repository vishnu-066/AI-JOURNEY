#to watch everything inside a module we can use dir() function. It will return a list of all the attributes and methods of the module.
import math
print(dir(math))  #prints all the attributes and methods of the math module.

import sys
a = 10.763457337
print(sys.getsizeof(a))
print(sys.getrefcount(a))
print(sys.getrecursionlimit())
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())
print(sys.path)  #prints the list of directories where Python looks for modules. It is a list of strings that specifies the search path for modules. When you import a module, Python searches for the module in the directories listed in sys.path, in order. If the module is not found in any of the directories, Python raises an ImportError. You can modify sys.path to add or remove directories from the search path, or you can use the PYTHONPATH environment variable to specify additional directories to search for modules.

#--------------------------------------------------------------------------------------------

import decimal
a = decimal.Decimal("10.763457337")
print(a)
#decimal is used to store large numbers with high precision. It is used to store numbers that are too large or too small to be represented as a float. It is also used to store numbers that require a high degree of precision, such as financial calculations. The decimal module provides a Decimal data type that can be used to represent decimal numbers with arbitrary precision. The Decimal data type can be used to perform arithmetic operations on decimal numbers with high precision. The Decimal data type can also be used to convert between decimal and other numeric types, such as float and int. The Decimal data type can also be used to format decimal numbers for display, such as rounding and formatting for currency.

print(decimal.getcontext().prec)  #returns the current precision of the decimal module. The precision is the number of significant digits that are used to represent decimal numbers. The default precision is 28, which means that decimal numbers are represented with 28 significant digits. The precision can be changed by setting the prec attribute of the context object. For example, decimal.getcontext().prec = 10 will set the precision to 10 significant digits. The precision can also be changed by using the localcontext() function, which creates a new context object with a different precision. For example, with decimal.localcontext() as ctx: ctx.prec = 10 will create a new context object with a precision of 10 significant digits.


#-----------------------------------------------------------------------------------------------

import math
a =10
b = 5
c = math.hypot(a, b)  # calculates the hypotenuse of a right triangle with sides a and b
print(c)

print(math.sqrt(a**2 + b**2))  # calculates the square root of the sum of the squares of a and b, which is the same as the hypotenuse of a right triangle with sides a and b
print(math.pow(a,b))  # calculates a raised to the power of b, which is the same as a**b
print(math.exp(a))  # calculates e raised to the power of a, where e is the base of the natural logarithm
print(math.log(a))  # calculates the natural logarithm of a, which is the inverse of the exponential function
print(math.log10(a))  # calculates the base-10 logarithm of a, which is the inverse of the power of 10 function
print(math.log2(a))  # calculates the base-2 logarithm of a, which is the inverse of the power of 2 function

#rounding...
print(math.ceil(34.4))  # rounds up to the nearest integer
print(math.floor(34.4))  # rounds down to the nearest integer
print(math.trunc(34.4))  # truncates the decimal part and returns the integer part

#Trigonometry ....
# sin,cos,tan will take radians value as input and return the sin,cos,tan value respectively.
print(math.sin(math.radians(90)))  # calculates the sine of 90 degrees,
# asin,acos,atan will take input as sin,cos,tan value and return the angle in radians.
print(math.degrees(math.asin(1)))  # calculates the arcsine of 1, which is the angle whose sine is 1, and converts it to degrees


# constants

print(math.pi)
print(math.e)
print(math.inf)


# factorial , combinations and permutations.
print(math.factorial(5))  # calculates the factorial of 5
print(math.comb(5, 2))  # calculates the number of ways to choose 2 items from 5 items
print(math.perm(5, 2))  # calculates the number of ways to arrange 2 items from 5 items
print(math.lcm(10,15))  # calculates the least common multiple of 10 and 15
print(math.gcd(10,15))  # calculates the greatest common divisor of 10 and 15


#Not important
import platform
print(platform.python_implementation())  # returns the name of the Python implementation, such as "CPython", "PyPy", or "Jython"
print(platform.python_version())  # returns the version of the Python interpreter, such as "3.9.1" or "2.7.18"

