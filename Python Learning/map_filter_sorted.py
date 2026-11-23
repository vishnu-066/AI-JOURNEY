# Reference : https://www.w3schools.com/python/python_lambda.asp

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



#Filter... basically filter is used  - functions applies to the iterables and returns the values which are true for the condition.
#Raw syntax : filter(function,iterable) you can keep only one iterable..
a = [2,3,4,5,6,7]
b = [4,6,7,8]
new = filter(lambda x: x%2 == 0,a) #here trying to filter even numbers. (note : you cant able to pass multiple iterables like map)
print(list(new))

new1 = [x for x in a if x%2==0] #same with list comprehension
print(new1)


#sorted --- it is used to sort the collections , it will creates the new collection object as result...
# Raw syntax : sorted(iterable,key,reverse) by default reverse = False and key is optional... you can pass functions as well for key value..

a = [3,68,65,892,3]
print(sorted(a))
print(sorted(a,reverse=True))
b = ["abc","vishnu","vard"]
print(sorted(b,key = lambda x :len(x),reverse= True )) #sorted through key


a = [("a",24),("b",12),("c",26)]
print(sorted(a,key = lambda x : x[1])) #sorted through key value of tuple index 1