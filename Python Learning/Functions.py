
#user defined functions...
#we can create used defined functions by using def keyword

"""
Difference between arguments and parameters...
During the function creation inside the paranthesis , we calld this as parameters
during function call.. passes the values inside it call arguments..

There are four types of arguments are there.... No arguments,default arguments,keyword arguments and positional arguments.
"""
#you can write a function with or without return value , incase if you dont write return value then by default its none.

# No arguments...
def call1():
         print("Hello world")
def call2():
         return "Hello world"
         
call1()  # we can call the function directly without print because there is no return value...If you use print here then the return value is none by default.

print(call2()) #here we need to call the function using print, bcoz there is return value..




# Default arguments..

def mutiply(a,b=10):
         return f"Multilly : {a*b}"
print(mutiply(4)) #here if you miss  the value of b then by default value it takes 10 because we assigned the value during function creation

#Keyword arguments = key value pair arguments
#The benifit of using keyword arguments - we dont need to pass the arguments in order...

def intro(Name,age,where):
         return f"Hello, My name is {Name}, {age} old, I am from {where}..."

print(intro(age = 21,Name = "Vishnu", where="Banglore")) 


# Positional arguments 
def summation(a,b):
         return f"sum : {a+b}"
print(summation(3,4)) #we need to pass same number of arguments and parameters in order, other wise it throughs an error..

#mix of position , keyword and default arguments..

def argu_mix(Name,age,branch,department = "CSE"):
         return f"Hello, I am {Name}, {age} years old. I recently joined in {branch}, \"{department}\" department"

print(argu_mix("Vishnu",age = 21, branch = "Btech")) #you cant able to do positional argument after the keyword argument while function calling with arguments ...
print(argu_mix("Vishnu",age = 21, branch = "Btech",department="ECE"))       



#You can pass any datatype to the function as arguments like int,string,float,list,tuple,set etc...  
#passing list to function as argument..

def fruit_call(fruits):
         for fruit in fruits:
                  print(fruit,end= " ")
myfruit = ['apple','banana','pineapple']
fruit_call(myfruit)
print()

#passing set 
def set_pass(cars,target = "BENZ"):
         if target in cars:
                  cars.remove(target)
         
         else:
                  pass
         return cars
cars = {"BMW","BENZ","VOLVO","FERARI"}
print(set_pass(cars))


# we can able to set a function that only accepts positional arguments bu using /

def sumation(a,b,/):
         return a+b
print(sumation(3,5)) #if you try to pass arguments using keyword then it throughs an error


# we can able to set a function that only accepts keyword arguments bu using *
def multiply(*,a,b):
         return a*b
print(multiply(a=3,b=5)) #if you try to pass arguments using positional then it throughs an error


#mix of position and keyword arguments
def sumation(a,b,/,*,c,d):
         return a+b+c+d
print(sumation(10,2,c=5,d=8)) #here positional arguments must be ahead of keyword arguments


# args--------------
""" suppose you have created one function with fixed positional parameters like a,b,c ...Now in futute you dont know how manay parameters you are passing through it...in this case you need to use dynamic positional parametric function - here wee call this as args (positional arbitary arguments) 
*args are stored in tuples...
Real world example : 
Suppose you are implementing a cart page for an e-commerce website - here you need to calculate the cart total, actually you dont know how many product prices you need to calculate, the arguments  changes based on orders, so here you are using *args 
"""

def summation(*values):
  return sum(values)
print(summation(12,34,56,23))


#Kwargs...........
"""kwargs is also same like args , but here you need to pass the arguments through keywords
In kwargs the values are stored like dictonary form(key-value pairs...)
"""

""" Try writing your own function that accepts a required user ID, any number of product names, a required keyword-only payment method, and optional keyword details. That will help you apply these concepts without relying on examples. """

def create_product(**details):
    print(details["name"])
    print(details["price"])
    print(details["brand"])
product = {
    "name": "Laptop",
    "price": 55000,
    "brand": "Dell"
}

create_product(**product) # here ** is used to unpack the dictonary items , you can use * for unpacking the list or tuple in *args concept.

# mixed ....
def details(user_ID,*products,payment_method,coupon_code="SAVE100",**other_details):
  print(f"{user_ID}\t{products}\t{payment_method}\t{coupon_code}\t{other_details}")

details(10237727,"mouse","keyboard","monitor",payment_method="UPI",coupon_code="NEW100",Address = "Banglore",code = 560035)
