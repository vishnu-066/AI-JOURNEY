import sys

objects = [
    True,
    10,
    3.14,
    3+4j,
    "",
    "A",
    "Hello",
    [],
    [1,2,3,4],
    (),
    (1,2,3,4),
    {},
    set(),
    frozenset(),
    b"",
    bytearray(),
    range(10),
    None
]

for obj in objects:
    print(f"{type(obj).__name__ :12} {repr(obj):20} {sys.getsizeof(obj)} bytes")


#--------------------------------------------------------

list_m = [1,9.8,(7,9,6),{},set()," "]
for i in list_m:
    print(type(i).__name__)
    # print(f"{repr(i)}")
    print(i,end=" ") ; print(repr(i))


import platform
print(platform.python_implementation())    
print(platform.python_version())


a = [12,4,56]
b = a
print(sys.getrefcount(a))


# print(dir(sys))  # checks which functions are available in sys directory using dir() function.
# print(help(sys.maxsize))   #knowing about particular function in a module 


# math functions 
import math
print(math.ceil(3.5))
print(math.floor(3.5))

print(round(3.145,2))
print(f"{3.145:.2f}") #formatting the float number to 2 decimal places 
#differcnce between decimal(xf) and round function is the output for .xf is in srt format and for round function is float format.
print(f"{3.145:.3g}")  #formatting the float number to 3 significant digits
print(f"{0.04516:.3g}")  #formatting the float number to 3 significant digits
print(f"{3.14565657657:.3e}")  #formatting the float number to scientific notation with 2 decimal places



a = [1,2,3,4]
print(sys.getrefcount(a))
print(sys.getrefcount([4,4,5]))


import sys

x = ("vishnu","vardhan","reddy")
y = ("vishnu","vardhan","reddy")

print(x is y)
print(sys.getrefcount(x))

print(math.sin(math.radians(90)))
print(math.sin(90))

a = round(3.14) #by default int
b = round(3.14,2) #float
print(a)
print(type(a))
print(b)
print(type(b))

import time

for ch in ["-", "\\", "|", "/"]:
    print(ch, end="", flush=True)
    time.sleep(2)
    print("\b", end="", flush=True)  # rewinds cursor so the next symbol overwrites

    