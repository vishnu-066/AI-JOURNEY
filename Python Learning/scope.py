# Reference link : https://www.w3schools.com/python/python_scope.asp

"""
In python mainly 4 types of scopes are there, they are : LEGB rule - Local, Enclosing, Global and Built-in scopes.

1. Local scope - variables defined inside the function are local to that function and can be accessed only inside that function.
2. Enclosing scope - variables defined in the enclosing function can be accessed inside the nested function.
3. Global scope - variables defined at the top level of the module are global and can be accessed from anywhere in the module.
4. Built-in scope - variables defined in the built-in namespace are available in all modules.
"""
def sample():
    x = 10
    print(x)  #prints the value of local variable x which is 10
sample()


def sample():
    x = 10
    def inner():
        nonlocal x  #declares that we want to use the enclosing variable x 
        x = 20
        print(x)  #prints the value of enclosing variable x which is 10
    inner()
sample()

x = 100
def sample():
    global x  #declares that we want to use the global variable x
    x = 200; y= 300
    print(x)  #prints the value of global variable x which is 200
    print(y)  #prints the value of local variable y which is 300
sample()