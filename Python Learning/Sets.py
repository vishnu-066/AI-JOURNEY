sets = {1, 2, 3, 4, 5}  
sets1 = {True,1,0,False,"Vishnu",1.2,1+2j} #set can contain different data types like int, float, complex, string and boolean.But here True and 1 are treat as same and False and 0 are treats as same because True is equal to 1 and False is equal to 0.
# sets2 = {1,2,(1,2),{1,2},[1,2,3],{"a":1,"b":2}} #set can contain different data types like int, float, complex, string, boolean, tuple and dictionary. But set cannot contain list, dictionary and set because they are mutable.
# print(sets2)

#If you want to access the set elements - need to use for loop
for i in sets1:
    print(i)

#or you need to convert the set into list and then access the elements using indexing.
sets1_list = list(sets1)    
print(sets1_list[:])

#using while loop after set converted into list
i =0
while i<len(sets1_list):
    print(sets1_list[i])
    i+=1

#=======updating set(add,update)========
sets.add(6) #adding single element to the set.
sets.update(sets1) #adding multiple elements to the set.
sets.update([7,8,9]) #adding multiple elements to the set using list.

#========removing elements from set========
sets.remove(1) #removing single element from the set. If the element is not present in the set then it will raise a KeyError.
sets.discard(2) #removing single element from the set. If the element is not present in the set then it will not raise any error.
sets.pop() #removing random element from the set. If the set is empty then it will raise a KeyError.
sets.clear() #removing all elements from the set. If the set is empty then it will not raise any error.
del sets1 #deleting the set from memory. If the set is not present in the memory then it will raise a NameError.



# Union operation - union operation resulted set will remove all the common elements and returns only distinct elements from sets
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}
set_3 = {'vishnu', 'reddy', 'python'}
list_1 = [1, 2, 32, 4, 54]
tuple_1= (11,23,3,67)
dict_1 = {'a': 1, 'b': 2, 'c': 3}

print(set_1.union(set_2)) #union operation between two sets. You can also use the | operator to perform union operation between sets.
print(set_1 | set_2) #union operation between two sets using | operator.
print(set_1.union(set_2,set_3)) #union operation between three sets.
print(set_1 | set_2 | set_3) #union operation between three sets using | operator.

print(set_1.union(list_1)) #union operation between set and list. but the result is in set.
print(set_1.union(tuple_1)) #union operation between set and tuple. but the result is in set.
print(set_1.union(dict_1)) #union operation between set and dictionary. but the result is in set.

print(set_1 | set_2 | set_3 | set(list_1) | set(tuple_1) | set(dict_1)) #union operation between multiple sets, list, tuple and dictionary. but the result is in set.

#====intersection operation--- it wiill return only common elements among the sets. You can also use the & operator to perform intersection operation between sets.
print(set_1.intersection(set_2)) #intersection operation between two sets. You can also use the & operator to perform intersection operation between sets.
print(set_1 & set_2 & set_3) #intersection operation between two sets using & operator.
print(set_1.intersection(set_2,set_3)) #intersection operation between three sets.
print(set_1 & set_2 & set_3) #intersection operation between three sets using & operator.
print(set_1 & set(list_1)) #intersection operation between set and list. but the result is in set.
print(set_1 & set(tuple_1)) #intersection operation between set and tuple. but the result is in set.
print(set_1 & set(dict_1)) #intersection operation between set and dictionary. but the result is in set.
print(set_1.intersection(set_2, set_3, set(list_1), set(tuple_1), set(dict_1))) #intersection operation between multiple sets, list, tuple and dictionary. but the result is in set.

# ==== intersection_update operation - intersection_update operation will update the original set with the intersection of sets. You can also use the &= operator to perform intersection_update operation between sets.
# same like intersection but it wont create new set , it updates the existing set.
set_1.intersection_update(set_2) #intersection operation between two sets using intersection_update() method. It will update the set_1 with the intersection of set_1 and set_2.
print(set_1)
set_1 &= set_2 #intersection operation between two sets using &= operator. It will update the set_1 with the intersection of set_1 and set_2.
print(set_1)

# ====== difference operation - difference operation will return the elements which are present in the first set but not in the second set. You can also use the - operator to perform difference operation between sets.
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}
print(set_1.difference(set_2)) #difference operation between two sets. You can also use the - operator to perform difference operation between sets.
print(set_1 - set_2) #difference operation between two sets using - operator.
set_3 = {67,4,2,3,5}
print(set_1.difference(set_2,set_3)) #difference operation between three sets.
print(set_1 - set_2 - set_3) #difference operation between three sets using - operator.

#===similarly we have difference_update operation - difference_update operation will update the original set with the difference of sets. You can also use the -= operator to perform difference_update operation between sets.
set_1.difference_update(set_2) #difference operation between two sets using difference_update() method. It will update the set_1 with the difference of set_1 and set_2.
print(set_1)


# =====Syemmetric difference operation - symmetric difference operation will return the elements which are present in either of the sets but not in both sets. You can also use the ^ operator to perform symmetric difference operation between sets.
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}
print(set_1.symmetric_difference(set_2)) #symmetric difference operation between two sets. You can also use the ^ operator to perform symmetric difference operation between sets.
print(set_1 ^ set_2) #symmetric difference operation between two sets using ^ operator.

#similarly we have symmetric_difference_update operation - symmetric_difference_update operation will update the original set with the symmetric difference of sets. You can also use the ^= operator to perform symmetric_difference_update operation between sets.
set_1.symmetric_difference_update(set_2) #symmetric difference operation between two sets using symmetric_difference_update() method. It will update the set_1 with the symmetric difference of set_1 and set_2.
print(set_1)

fs = set_1.copy()  #shallow copy...
print(fs) #copying the set_1 to fs using copy() method. It will create a new set fs with the same elements as set_1.
fs.add(100) #adding an element to the copied set fs. It will not affect the original set set_1.
print(fs)

import copy
ds = copy.deepcopy(set_1) #deep copy...
print(ds)

print(set_1.isdisjoint(set_2)) #checking if two sets are disjoint or not. It will return True if the sets are disjoint and False if they are not disjoint.
print(set_1.issubset(set_2)) #checking if set_1 is a subset of set_2 or not. It will return True if set_1 is a subset of set_2 and False if it is not a subset.
print(set_1.issuperset(set_2)) #checking if set_1 is a superset of set_2 or not. It will return True if set_1 is a superset of set_2 and False if it is not a superset.


#========== problems =============
# remove duplicates from a list without using set() method.
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
numbers.sort()

low = 0
high = 1

while high < len(numbers):
  if(numbers[low] == numbers[high]):
    numbers.pop(high)
  else:
    low += 1
    high += 1

print(numbers)

#remove duplicates from a list using set() method.
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
numbers = list(set(numbers))
print(numbers)


"""
Students present in both classes
Students present only in Class A
Students present only in Class B
Students present in either class but not both
"""
class_A = {"Vishnu", "Rahul", "Anil", "Priya", "Sneha"}
class_B = {"Rahul", "Priya", "Arjun", "Kiran", "Sneha"}

print(*(class_A & class_B))  #here star operator is used to unpack the set and print the elements of the set.
print(*(class_A - class_B))
print(*(class_B - class_A))
print(*(class_A ^ class_B))


"""
Write a program to find:
1. Users who have both developer and admin access
2. Users who have developer or tester access but NOT both
3. Users who have all three types of access
4. Users who have exactly one type of access
5. Users who have no access to any of the three groups
6. Create a final set containing every unique user
"""


all_users = {"A", "B", "C", "D", "E", "F", "G", "H", "I"}

developers = {"A", "B", "C", "D", "E"}
admins = {"C", "D", "F"}
testers = {"B", "E", "F", "G"}

print(developers & admins)
print(developers ^ testers)
print(developers & admins & testers)
print(developers ^ testers ^ admins)
print(all_users - (developers | testers | admins))
print(developers | testers | admins)


