#Tuples are ordered, immutable and allow duplicates.
#creating a tuple.
a = ("a",3,[1,2,34],(1,2,3),{1,2,3},{'a':1,'b':2})  #tuple can contain different data types like list, set, dictionary, tuple and string.
b = 1,2,3,4,5 #tuple can be created without using parenthesis.
c = ("a") #this is not a tuple, this is a string because it has only one element and no comma.
d = ("a",) #this is a tuple because it has only one element and a comma.
e = () #this is an empty tuple.

# we can also able to create a tuple using tuple constructor tuple() like same as list constructor list().
f = tuple((1,2,3,4)) #this is a tuple with elements 1, 2, 3, 4.
g = tuple()  #this is an empty tuple.


#======Accessing tuple values=========
print(a[0]) #accessing first element of tuple a.
print(a[2][2]) #accessing third element of list which is present in tuple a.
a[2][2] = 100 #we can able to change the value of list which is present in tuple a because list is mutable.
print(a[2][2]) #accessing third element of list which is present in tuple a.
print(a[1:3]) #accessing second and third element of tuple a.
print(a[-1]) #accessing last element of tuple a using negative indexing.


#=================update tuple values (add,delete and update values)========================
# we can able to update the tuple values by converting the tuple to list and then updating the list and then converting the list back to tuple.
h = list(a) #converting tuple a to list h.
h[1] = 100 #updating the third element of the list which is present in tuple a.
a = tuple(h) #converting the list h back to tuple a.

#We can able to add two tuples using + operator and we can able to multiply the tuple using * operator.
i = a + b #adding two tuples a and b.
j = a * 2 #multiplying tuple a by 2.
print(i) #printing the tuple i.
print(j) #printing the tuple j.

del b #deleting the tuple b from memory.



#=============unpacking of tuple values========================
a = ("a",2,"vishnu")
x,y,z = a #unpacking the tuple a into variables x, y and z.
print(x) #printing the variable x.
print(y) #printing the variable y.
print(z) #printing the variable z.


#suppuse if you have more values than the variables you have to unpack then you can use * operator to unpack the remaining values into a list.
a = ("a",2,"vishnu","reddy","python")
x,y,*z = a #unpacking the tuple a into variables x, y and z.
print(x) #printing the variable x.
print(y) #printing the variable y.
print(z) #printing the variable z.