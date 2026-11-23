#Reference link : https://www.w3schools.com/python/python_lambda.asp

#Lambda is a ananymous function in Python. It is a small, unnamed function defined using the lambda keyword. Lambda functions can take any number of arguments but can only have one expression. The expression is evaluated and returned when the function is called.

#basic lambda function..

x = lambda a,b,c : a+b*c  #you can take multiple arguments here but only one expression..
print(x(2,3,4))

x = lambda x : lambda y : x+y #This is nested lambda and process of taking the arguments one by one in chain process called function curring..
#here lambda y : x+y is the expression for lambda x..
print(x(4)(5))

#you can also able to call the lambda function inside a function through return 
def mul(n):
  return lambda a:a*n
x = mul(3)  #calling the function and assigned that to a variable....here x store the return value that is lambda a : a*3
print(x(10)) #now we called the lambda function with passing an arguments(value of a)
print(mul(3)(10)) #you can also able to pass the both arguments at once...


def calculate(x):
    return (lambda y:
              lambda z: 
                  x + y * z)

print(calculate(2)(3)(4))

a = lambda c = 10 : 4*c  #keeping adefault value....
print(a())




#lambda with built-in function...

#Map... basically map is used  - functions applies to the iterables
#Raw syntax : map(function,iterable1,iterable2 etc) you can keep as many iterables..

#without lambda...
def squares(n):
  return n*n
a = [2,3,4,5]
print(list(map(squares,a)))

#with lambda function
a = [2,3,4,5]
squares = list(map(lambda x : x**2,a))
print(squares)

# with multiple iterables...
a = (1,2,3,4)
b = (6,7,5,9)
print(list(map(lambda a,b : a+b , a,b)))

#what if the the lengths of collections(lists,tuples,sets) are with different lengths...
#ans : it will excute the min lenght of the collection...map checks wheather the both collections are same or not ..if not same then run the map function until the small collection reaches...
m = [2,3,4,5,6,7,9]
n = (6,4,3)
print(list(map(lambda m,n : m*n,m,n)))