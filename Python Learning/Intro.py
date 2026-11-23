# print("Hello")
a = input("A = ")
b = input("B = ") 
print("Result = ",int(a)-int(b))


#variables 
""" 3 types of varible names in python
camel case - myVariable
pascal case - MyVariable
snake case - my_variable"""

""" global and local variables 
global is defined outside the function and it can be accesseble anywhere in program
local variable is defined inside the function and it can be accessable only inside the function"""

"""suppose you have both local and global variables with same name the how can we call a global variable inside the function here it is : """
x = "vishnu"
def myfunc():
    x= "vardhan"
    print(f"Global : {globals()['x']}")  #globals() is a built-in function that returns a dictionary of the current global symbol table. The global symbol table is a data structure that contains all the information about the global variables and functions in the current module. The globals() function can be used to access global variables from within a function, even if there is a local variable with the same name. In this case, globals()['x'] will return the value of the global variable x, which is "vishnu".
    print(f"Local : {x}")  #prints the value of local variable x which is "vardhan"
myfunc()  #calling the function myfunc()


"""suppose i want to modify the global variable from inside the function , here it is :"""
x = "vishnu"
def myfunc():
    global x  #declares that we want to use the global variable x
    x = "vardhan"
    print(f"Modified Global : {x}")
myfunc()
print(f"Global after function call : {x}")

"""you can also able to declare a global variable inside the function using global keyword, here it is :"""
def myfunc2():
    global y
    y = "new_global_variable"
    print(f"New Global : {y}")
myfunc2()
print(f"Global after function call : {y}")