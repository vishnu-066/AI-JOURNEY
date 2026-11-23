"""
Dictionaries are used to store data in key-value pairs. Each key is unique and is used to access the corresponding value. Dictionaries are mutable, meaning you can change their content without changing their identity.
Ordered, don't allow duplicate keys.
"""

#Creating dictionary 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

#Accessing values in a dictionary
print(car["model"])
print(car.get("model")) #is used to access the value of a specific key.
print(car.keys())  #is used to get all the keys in a dictionary.
print(car.values())  #is used to get all the values in a dictionary.
print(car.items())  #is used to get all the key-value pairs in a dictionary.
#Note : If you try to access a key that does not exist in the dictionary, it will raise a KeyError. To avoid this, you can use the get() method, which returns None if the key does not exist.


#Note : when you try to update or add an item , if an item already present in the dictionary then it will update the value of that item, if the item is not present in the dictionary then it will add that item to the dictionary.
#Updating values in a dictionary
car["year"] = 2020  #is used to update the value of a specific key.
car.update({"year": 2021})  #is used to update the value of a specific key.


#you can also add multiple items using update() method.
car.update({"color": "red", "price": 20000})  #is used to add multiple key-value pairs in a dictionary.
dupl = {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "red", "price": 20000}
car.update(dupl)  #is used to add multiple key-value pairs in a dictionary.

#Removing items from a dictionary
car.pop("model")  #is used to remove a specific key-value pair from a dictionary
car.popitem()  #is used to remove the last inserted key-value pair from a dictionary.
del car["year"]  #is used to remove a specific key-value pair from a dictionary
car.clear()  #is used to remove all key-value pairs from a dictionary.
del car  #is used to delete the dictionary from memory.


# accessed using for loop

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

for x in car:
    print(x)  #prints all keys
    print(car[x])  #prints all values

for x in car.keys():
    print(x)  #prints all keys

for x in car.values():
    print(x)  #prints all values

for x, y in car.items():
    print(x, y)  #prints all key-value pairs


# copying a dictionary
car2 = car.copy()  #is used to create a copy of a dictionary.
car3 = dict(car)  #is used to create a copy of a dictionary.


#creating a dictionary and getting all ids from data......
user_1 = {"ID" : "vr_06",
         "Name" : "Vishnuvardhan",
         "DOB" : "4th April"}
user_2 = {"ID" : "vk_18",
         "Name" : "Virat kohli",
         "DOB" : "4th November"}
user_3 = {"ID" : "AA_06",
         "Name" : "Allu_Arjun",
         "DOB" : "8th April"}

Instagram_users = {
  "User_1" : user_1,
  "User_2" : user_2,
  "User_3" : user_3
}

print(Instagram_users)
print(Instagram_users.values())

for x in Instagram_users.values():
  print(x["ID"])
print(Instagram_users["User_2"])

#i want to print all ids from data
for x, obj in Instagram_users.items():
         for y,obj1 in obj.items():
                  if(y == "ID"):
                           print(f"{x} : {obj[y]}")