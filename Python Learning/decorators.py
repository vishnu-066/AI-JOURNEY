#Decorator - It is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it. In Python, decorators are implemented as functions (or classes) that return a new function that adds some kind of functionality to the original function. Decorators are often used in web frameworks, logging, authentication, and other scenarios where you want to add common functionality to multiple functions or methods.
"""decorator
1.normal decorator
2.multiple decorateds
3.decorated with arguments
4.decorated with args and kwars
5.multiple decorators
6.decorator with arguments
7.keep metedata of original function same."""

#Normal decorator :
#using closure.... (holding the value weather its a variable or return value of a function even though the function excution was completed..)

def decorator(func):
  def wrapper():
    return func().upper()
  return wrapper
    

def function():
  return "vishnu"

function = decorator(function)
print(function())

#Normal decorator using decorator ..
def decorator(func):
  def wrapper():
    return func().upper()
  return wrapper
    
@decorator    #function = decorator(function) <- closure..
def function():
  return "vishnu"

print(function())


#multiple decorateds...(one decorator acts on multiple function..)
def decorator(func):
  def wrapper():
    return func().upper()
  return wrapper
    
@decorator    #function = decorator(function) <- closure..
def function():
  return "vishnu"
@decorator    #function = decorator(function) <- closure..
def function():
  return "vardhan"

print(function())


#decorated with arguments...
def decorator(func):
  def wrapper(name,age):  #if you are applying the decorator on single function(decorated) then you can you directly variable names... else you need to use args and kwargs)
    return func(name,age)
  return wrapper
      
@decorator
def details(name,age):
  return f"Hello I am {name} , and i am {age} years old"

name = input('Enter name : ')
age = int(input("Enter age : "))
print(details(name,age))
 

#decorated with args and kwargs..

"""Problem statement
You are building an application and want to track when functions start and finish. Instead of writing the same print statements inside every function, create a decorator called track_execution and apply it to multiple functions.
Requirements
1. Create a decorator named track_execution.
2. It must print "Execution started" before the decorated function runs.
3. It must print "Execution completed" after the function finishes.
4. It must support functions with different arguments using *args and **kwargs.
5. It must return the decorated function's result correctly.
6. Apply it to all three functions below."""

def track_excution(func):
  def wrapper(*args,**kwargs):
    print("Execution started")
    print(func(*args,**kwargs))
    return 'Excution finished'
    
  return wrapper

@track_excution
def func1(name,age):
  return f"Hello i am {name} , i am {age} years old"
@track_excution
def func2(branch,clg):
  return f"I am currently persuing {branch} in {clg} university"
@track_excution
def func3(cgpa):
  return f"My overall CGPS is {cgpa}.."

print(func1("Vishnu",23))
print(func2("CSE","LPU"))
print(func3(7.58))




#decorator with parameter/argument..
# The parameter decorator is used , when the decorator needs to act based on this parameter..
#Eg : Supose u are creation a permission check decorator for accessing something ...
def decorator(role):
  def inner(func):
    def wrapper(user_role):
      if role == user_role:
        return func(user_role)
      return "Access denaied"
    return wrapper
  return inner


@decorator("admin")
def logs(user_role):   #Now this logs details have permission for admin only...
  a = """325 mem ordered mouse
  total sales 34256
  total new users = 453"""
  return a
print(logs("admin1"))




#multiple decorators... multiple decorators acts on single decorated function...
#it was mainly useful for logging,time check etc...
from time import perf_counter
def deco_A(func):
  def logging(*args,**kwargs):
    print('Excution strarted..')
    
    print(func(*args,**kwargs))
    return "Excution done..."
  return logging

def deco_B(func):
  def time_check(*args,**kwargs):
    start = perf_counter()
    try:
      return func(*args,**kwargs)
    finally:
      print(f"{(perf_counter() - start):.6f}")
  return time_check
@deco_A
@deco_B
def function(a,b):
  return a*b

print(function(10,20))




# wraps...

#suppose you are applying a decorator on a function... you are trying to access the metadata of original function..its not possible to access without wraps..because now that original function name points to the wrapper function matadata inside the decorator...
#To over come this...we use functools.wraps...it binds the original function metadata 

#without @wraps

def decorator(func):  
  def wrapper(*args):
    '''This is wrapper docstring'''
    print('Function started..')
    print(func(*args))
    return "Function Excuted"
  return wrapper
@decorator
def summation(*args):
  """This is summation doc string"""
  return sum(args)

print(summation(2,3,4,5))
print(summation.__name__)  #return name of function - wrapper because here function points to wrapper
print(summation.__doc__)   #returns docstring of the wrapper function , if docstring not found returns none..



from functools import wraps
def decorator(func):
  @wraps(func)
  def wrapper(*args):
    print('Function started..')
    print(func(*args))
    return "Function Excuted"
  return wrapper
@decorator
def summation(*args):
  """This function is all about summation"""
  return sum(args)

print(summation(2,3,4,5))
print(summation.__name__)  #return name of original function
print(summation.__doc__)   #returns docstring of the original function , if docstring not found returns none..