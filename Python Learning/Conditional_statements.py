# Conditional Statements in Python

# if statement
x = 10
if x > 5:
    print("x is greater than 5")

# if-else statement
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

# if-elif-else statement
z = 7
if z < 5:
    print("z is less than 5")
elif z == 5:
    print("z is equal to 5")
else:
    print("z is greater than 5")



# Nested if statement
a = 10
if a > 5:
    if a < 15:
        print("a is between 5 and 15")
    else:
        print("a is greater than or equal to 15")


# # Logical operators in conditional statements
# and operator
x = 10
y = 20
if x > 5 and y < 25:
    print("Both conditions are true")

# or operator
if x > 15 or y < 25:
    print("At least one condition is true")

# not operator
if not (x < 5):
    print("x is not less than 5")


## Ternary operator (conditional expression)
age = 18
status = "Adult" if age >= 18 else "Not an adult"
print(f"Status: {status}")


#============================================ """PROJECTS""" =========================================================

# small project ---   Grade calculator based on marks obtained in 5 subjects (Telugu, Hindi, English, Maths, Science) and percentage calculation

# Need to update the code 
# to include validation for marks (0-100) and handle exceptions for invalid inputs. Also, consider adding functionality to save the results to a file for future reference.
# use while loop to keep asking for valid input until the user provides it. Also, consider adding a feature to calculate the highest and lowest marks among the subjects.
# use try-except block to handle exceptions for invalid inputs.
# use functions to modularize the code and make it more readable.
Name = input("Enter name : ")
Roll_No = input("Enter Roll_No : ")
marks = []
if(Name.replace(" ","").isalpha() and len(Roll_No) == 8 and Roll_No.isdigit()):
    print(f"Vallidating your credentials......\n\n'Done....! Enter your marks below'\n\n")
    Telugu = int(input("Telugu marks : "))
    marks.append(Telugu)
    Hindi = int(input("Hindi marks : "))
    marks.append(Hindi)
    English = int(input("English marks : "))
    marks.append(English)
    Maths = int(input("Maths marks : "))
    marks.append(Maths)
    Science = int(input("Science marks : "))
    marks.append(Science)
    
    Total = marks[0]+marks[1]+marks[2]+marks[3]+marks[4]
    Average = Total/5
    percentage = (Total / 500)*100
    Grade = " "
    # Grading .....
    print("\n'Here Your Results'\n")
    if(percentage <= 100 and percentage >= 90):
        Grade = "Congratulations you got 'A' grade"
        
    elif(percentage < 90 and percentage >= 80):
        Grade = "Congratulations you got 'B' grade"
        
    elif(percentage < 80 and percentage >= 70):
        Grade = "Congratulations you got 'C' grade"
        
    elif(percentage < 70 and percentage >= 60):
        Grade = "Congratulations you got 'D' grade"
        
    else : 
       
        Grade = "Sorry to say this you 'Failed'"
        
else : 
    print("Enter correct credentials..........")

print(f"{'Name':<10} : {Name}")
print(f"{'Roll_No':<10} : {Roll_No}")
print(f"{'Total':<10} : {Total}")
print(f"{'Average on each subject'} : {Average}")
print(f"{'Percentage':<10} : {percentage}")
print(f"{'Grade':<10} : {Grade}")
