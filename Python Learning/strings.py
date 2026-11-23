'''Strings are stored in indexed arrays called "strings"
Strings are immutable, meaning that once a string is created, it cannot be changed.
There are two types of indexing in Python: positive indexing and negative indexing. 
Positive indexing starts from 0 and goes up to n-1, where n is the length of the string. 
Negative indexing starts from -1 and goes down to -n, where n is the length of the string.'''

name = "Vishnu vardhan reddy".title()
print(name)
print(name[1])  # Positive indexing
print(name[-1])  # Negative indexing
print(name[1:-1])  # Slicing the string from index 1 to -1
print(name[:-1])  # Slicing the string from index 0 to -1
print(name[0:])  # Slicing the string from index 0 to end
print(name[1:9:2])  # Slicing the string from index 1 to 9 with step 2
print(name[::-1])  # Reversing the string using slicing
print(name[-1:-10:-1])  # Slicing the string from index -1 to -10 with step -1
print(name[0:30])  # Slicing the string from index 0 to 30 (out of range, but it will not throw an error)
print(len(name))
print(name[19:-1])   #wont print anything because the starting index and ending index are same -- let convert negative index to positive and see.. len + (-1) = 19, so the starting index is 19 and ending index is -1, which is 19. So, it will not print anything. condition internally checks if the starting index is less than the ending index, if not it will not print anything. because step by default is +1 , it move left to right.
print(name[::])  # Slicing the string from index 0 to end with step 1
print(name[:])   # Slicing the string from index 0 to end with step 1


name = "vishnu vardhan reddy"
print(name[-10:-1:1])

print(len("vishnu vardhan".split())) # The string will split where there is space and it stores that splitted strings in list and then len() will return the length of that list. In this case, it will return 2 because there are 2 words in the string "vishnu vardhan".

print(len("vishnu vardhan".replace(" ",""))) # The string will replace the space with nothing and then len() will return the length of that string. In this case, it will return 13 because there are 13 characters in the string "vishnuvardhan".

for i, ch in enumerate(name): # This is out of syllabus for this strings file..you can learn this thing in enumarations concept.
    print(i, repr(ch))



peru = "vishnu"
vis = peru
print(peru.replace("v","V"))
print(vis)


name = name.split()
print(" ".join([name[0],"-".join([name[1],name[2]])]))
a = list("name")
print(a)
print(" ".join(a))

val = "My name is Vishnu vardhAn reddy"
val = val.lower().replace(" ","")
count_val = 0

length = len(val)
for i in range (length):    # It checks the charecter through index
    if(val[i]=="a"):
        count_val += 1
print(f"Total 'a' {count_val}")
del count_val, length, val     #deletes all the variables from memory. This is useful when you want to free up memory or when you want to avoid using the same variable name in different parts of your code.


a ="Vishnuvardhan"
a= a.lower()
count_val = 0
for i in a:             # It directly picks the charecter and checks it without using index
    if(i == "a"):
        count_val += 1
print(count_val)

print(a.count("v"))     #inbuilt method to count the number of occurrences of a substring in a string. In this case, it will return 2 because there is 2 occurrence of "v" in the string "vishnuvardhan".


#str.startswith() -  actual method - str.startswith(prefix, start, end)
#str.endswith() -  actual method - str.endswith(suffix, start, end)
print(a.startswith("S."))   #inbuilt method to check if the string starts with a substring. In this case, it will return False because the string "vishnuvardhan" does not start with "S".
print(a.endswith("n"))   #inbuilt method to check if the string ends with a substring. In this case, it will return True because the string "vishnuvardhan" ends with "n".


# str.find() -  actual method - str.find(prefix, start, end)  - returns the lowest index of the substring if it is found in given string. If it is not found then it returns -1. It checks from left to right.
print(a.find("v"))   #it checks from left to right , inbuilt method to find the index of the first occurrence of a substring in a string. In this case, it will return 0 because the first occurrence of "v" in the string "vishnuvardhan" is at index 0. 
print(a.find("v",1))   #it checks from left to right , inbuilt method to find the index of the first occurrence of a substring in a string starting from index 1. In this case, it will return 6 because the first occurrence of "v" in the string "vishnuvardhan" starting from index 1 is at index 6.
print(a.find("w")) #returns -1 because the substring "w" is not found in the string "vishnuvardhan".
print(a.rfind("v")) # it checks from right to left , inbuilt method to find the index of the last occurrence of a substring in a string. In this case, it will return 6 because the last occurrence of "v" in the string "vishnuvardhan" is at index 6.


#Index  - str.index() -  actual method - str.index(prefix, start, end)  - same like find but if val not found it will throw an error instead of returning -1
print(a.index("v"))   #it checks from left to right , inbuilt method to find the index of the first occurrence of a substring in a string. In this case, it will return 0 because the first occurrence of "v" in the string "vishnuvardhan" is at index 0.
print(a.index("v",1))   #it checks from left to right , inbuilt method to find the index of the first occurrence of a substring in a string starting from index 1. In this case, it will return 6 because the first occurrence of "v" in the string "vishnuvardhan" starting from index 1 is at index 6.
#print(a.index("w")) #throws an error because the substring "w" is not found in the string "vishnuvardhan".
print(a.rindex("v")) # it checks from right to left , inbuilt method to find the index of the last occurrence of a substring in a string. In this case, it will return 6 because the last occurrence of "v" in the string "vishnuvardhan" is at index 6.




#====================Problems ==================

name = input('Enter name : ')
name = name.lower()
count1 = 0
for i in name:                      #length = len(name)
    if(i in "aeiou"):               #for in in range(length):  if(name[i] in "aeiou"):
        count1 += 1                 #   count1 += 1

print(count1)



#convert a string to integer.
val = int("vishnu",36)
print(val)

#string can also be stored in multiline using triple quotes. It can be used to store a string in multiple lines. It can also be used to store a string in a single line with line breaks. It can also be used to store a string in a single line with line breaks and indentation. It can also be used to store a string in a single line with line breaks and indentation and special characters. It can also be used to store a string in a single line with line breaks and indentation and special characters and escape sequences. It can also be used to store a string in a single line with line breaks and indentation and special characters and escape sequences and unicode characters. It can also be used to store a string in a single line with line breaks and indentation and special characters and escape sequences and unicode characters and raw strings. It can also be used to store a string in a single line with line breaks and indentation and special characters and escape sequences and unicode characters and raw strings and formatted strings. It can also be used to store a string in a single line with line breaks and indentation and special characters and escape sequences and unicode characters and raw strings and formatted strings and f-strings. It can also be used to store a string in a single line with line breaks and indentation and special characters and escape sequences and unicode characters and raw strings and formatted strings and f-strings.
val = """This is a multiline string.
It can be used to store a string in multiple lines.
It can also be used to store a string \n in a single line with line breaks."""
print(val)
