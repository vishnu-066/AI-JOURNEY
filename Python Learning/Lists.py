#List topic ................

# You can create a list in Python by using square brackets [] or the list() constructor. Lists can contain elements of different data types, including integers, strings, other lists, tuples, sets, and dictionaries.
a =[]  
b = list()
c= [1,2,"abc",[7,89,0],(1,2,3),{1,2,3},{'a':1,'b':2}]

#Question : How can we access these elements in list?

print(c[2])  # Access the third element (index 2) which is the string "abc"
print(c[3][0])  # Access the fourth element (index 3) which is a list, then access its first element (index 0)
print(c[4][1])  # Access the fifth element (index 4) which is a tuple, then access its second element (index 1)
print(c[5])  # Access the sixth element (index 5) which is a set
print(c[6]['a'])  # Access the seventh element (index 6) which is a dictionary, then access its 'a' key
print(c[-1]['b'])  # Access the last element (index -1) which is a dictionary, then access its 'b' key
print(c[:3])  # Access the first three elements (index 0 to 2) which are [1, 2, "abc"]
print(c[1:4])  # Access elements from index 1 to 3 which are [2, "abc", [7, 89, 0]]
print(c[1:4][2][1])  # Access elements from index 1 to 3 which are [2, "abc", [7, 89, 0]], then access the second element (index 1) which is "abc"


# How can we change the values of the list elements?

c[0] = 100  # Change the first element (index 0) to 100
print(c)  # Print the updated list

# replace multiple elements in a list using slicing
c[2:4] = [100,200]  # Replaces elements at index 2 and 3 with [100, 200]
print(c)

# How can we add elements to a list?  3 options -> append,insert and extend

# using "append" you can able to insert a single element to the list and that too that will add at "end of the list".
# using "insert" you can able to insert a single element to the list and that too that will add at "given index" of the list.
# using "extend" you can able to insert "multiple elements" to the list and that too that will add at "end of the list".


c.append(500)  # Add 500 to the end of the list
print(c)  # Print the updated list

c.insert(1, 200)  # Insert 200 at index 1
print(c)  # Print the updated list

c.extend([7,8,9])  # Add multiple elements [7, 8, 9] to the end of the list
print(c)  # Print the updated list


#What makes difference between append and extend ?

a = [1,2,3]
a.append([4,5])  # Adds [4, 5] as a single element
print(a)  # Output: [1, 2, 3, [4, 5]]

b = [7,2,3]
b.extend([4,5])  # Adds 4 and 5 as separate elements
print(b)  # Output: [7, 2, 3, 4, 5]
print(b.sort())  # Returns none, sorts the list in place
print(b)  # Output: [2, 3, 4, 5, 7]
print(b.reverse())  # Returns none, reverses the list in place
print(b)  # Output: [7, 5, 4, 3, 2]

b[2:4] = [100,200]  # Replaces elements at index 2 and 3 with [100, 200]
print(b)


#unpacking list
a = [1,2,3]
x,y,z = a
print(x)
print(y)
print(z)




#Problems on list

'''Problem   ---  level : 1 star problem

Write a program that:

Takes n numbers from the user.
Store them in a list.
Print:
Complete list
Length
Largest number
Smallest number
Sum
Print every element with its index.'''

user_input = int(input("Enter how many numbers do want enter : "))
user_list = []
i = 0
while i<user_input:
    values = int(input(f"Enter {i+1}th number : "))
    user_list.append(values)
    i +=1
print(user_list)
print(len(user_list))
print(max(user_list))
print(min(user_list))
print(sum(user_list))
for i,val in enumerate(user_list,start = 1):
    print(f"Index : {i} , Value : {val}")
a=list(enumerate(user_list))
print(a)


'''
---  level : 2 star problem

Perform these operations one by one.

Append 60
Insert 25 after 20
Extend with
[70,80]
Remove 40
Pop the last element
Delete first element
Check whether 50 exists.
Count occurrence of 20
Find index of 70'''

from collections import Counter
list_values = [10,20,30,40]
list_values.append(60)
print(list_values)
list_values.insert(2,25)
print(list_values)
list_values.extend([70,80])
print(list_values)
list_values.remove(40)
print(list_values)
list_values.pop()
print(list_values)
list_values.pop(1)
print(list_values)
del list_values[3]
# del 3 in list_values
print(list_values)
print(25 in list_values)
print(list_values.index(25))
print(list_values.count(25))
count = Counter(list_values)
for i,val in count.items():
    print(f"{i} -> {val}")
print(Counter(list_values))
print(list(Counter(list_values)))



'''Problem   ---  level : 3 star problem

Input marks of 10 students.

Print

Highest marks
Lowest marks
Average
Passed students (>=35)
Failed students (<35)
Sorted marks
Reverse sorted marks

Create another list using

copy()

Add bonus marks only to copied list.

Verify original list is unchanged.'''

list_marks = []
i=0
while(i<5):
    input_marks = int(input("Enter your marks : "))
    list_marks.append(input_marks)
    i+=1
print(max(list_marks))
print(min(list_marks))
print(sum(list_marks)/10)
print("Passed : ")
for i in list_marks:
    if(i>=35):
        
        print(i)
print("Failed") 
for i in list_marks:
    if(i<35):
        
        print(i)
list_marks.sort()

print(list_marks)
list_marks.sort(reverse = True)
print(list_marks)

update_list = list_marks.copy()
print(update_list)

for i in range(len(update_list)):
    update_list[i]+=5
    
print(update_list)
    


'''
problem ---  level : 4 star problem


'''



def add_products(product_name = "NA",price = 0,quantity = 0):
    product_name = input("Enter name of product : ")
    price = int(input("Enter price of product in rupee without coma separation : "))
    quantity = int(input("Enter quantity without separation : "))
    product_records.append([product_name,price,quantity])
    print('"Product successfully added"')
    return product_records
    
def remove_products():
    product_name = input("Enter name of product : ")
    price = int(input("Enter price of product in rupee without coma separation : "))
    quantity = int(input("Enter quantity without separation : "))
    product_records.remove([product_name,price,quantity])
    print('"Product successfully removed"')
    return product_records
    
def update_Quantity():
    product_name = input("Enter product name : ")
    for row in range(len(product_records)):
        for col in range(len(product_records[row])):
            if product_records[row][col] == product_name:
                print("Type 'price' for price update or 'quantity' for Quantity update : ")
                inner_operation = input("Enter inner operation : ")
                if(inner_operation == "price"):
                    product_records[row][1] = int(input( "enter updating price : "))
                    print('Price updated')
                if(inner_operation == "quantity"):
                    product_records[row][2] = int(input("Enter updated quantity : "))
                    print('Quantity updated')
                    
def search_product():
    product_name = input("Enter product name : ")
    for row in range(len(product_records)):
        for col in range(len(product_records[row])):
            if(product_records[row][col] == product_name):
                print("Here your searched product\n")
                print(product_records[row])
                
def display_inventory():
    for i in range(len(product_records)):
        print(*product_records[i])

product_records = []
while(True):
    Op_input = input("Enter your operation : ")
    Op_input = Op_input.lower()
    if(Op_input == "exit"):
        print('"Exited successfully"')
        break
    elif(Op_input == "add"):
        add_products()
    elif(Op_input == "remove"):
        remove_products()
    elif(Op_input == "update"):
        update_Quantity()
    elif(Op_input == "search"):
        search_product()
    elif(Op_input == "display"):
        display_inventory()
    else:
        print("Enter correct input ......")




