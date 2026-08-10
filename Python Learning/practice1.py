# Take radius input from the user and print the area of circle.   ( Doubts file in chatgpt about decimal and float conversion)
from math import pi
from decimal import Decimal
radius = float(input("Enter radius value: "))
area = (pi) * radius**2
print(f"Area of circle: {area}")  
# print(type(area))
print(f"Area of circle: {Decimal(area)}")
print(f"Area of circle: {Decimal(str(area))}")  # Convert float to string and then to Decimal
# print(type(Decimal(str(area))))


#------------------------------------------------------

val = Decimal(input("Enter a float value: "))
print(f"Value entered: {val}")


price = 0.1
tax = 0.2
total = price + tax
print(Decimal(str(total)))



price = 60.789
# price = float(input("Enter price : "))
gst = 0.18
total = price + (price * gst)

#print(total)
print(Decimal(str(total)))  # Convert float to string and then to Decimal


print(4+2.7)
a = 0.7
b = 1.6
print(a+b)

print(Decimal(str(a)) + Decimal(str(b)))


# ----------Quadratic roots finding------------------

import math

a,b,c = 1,-3,2
descrim = math.sqrt(math.pow(b,2) - 4*a*c)
root_1 = (-b + descrim)/2*a
root_2 = (-b - descrim)/2*a
print(f"Roots : ({root_1},{root_2})")


#Converting temparature units from Celsius to Fahrenheit and kelvin
# Foreign heat value = (C * 9/5) + 32
# Kelvin value = C + 273
from decimal import Decimal
celcius_val = Decimal(input("Enter value : "))
v = 9/5
F = celcius_val*Decimal(str(v))+Decimal("32")
K = celcius_val + Decimal("273")
print(f"Foreigh_heat_value : {F}\nKelvin_value : {K}")
print(f"{'Foreigh_heat_value':<20}: {F:>3}\n{'Kelvin_value':<20}: {K:>3}")



#Currency converter usd to euro
from decimal import Decimal
usd_amount = Decimal(input("Enter amount in USD: "))
euro_amount = usd_amount * Decimal("0.85")  # Assuming 1 USD = 0.85 EUR
print(f"{'Equivalent amount in EUR':<25}:{euro_amount:>5.1f}")   #.1f for 1 decimal place formatting , >5 is for right alignment with 5 spaces



# counting vowels from input string

name = input('Enter name : ')
name = name.lower()
count1 = 0
for i in name:                      #length = len(name)
    if(i in "aeiou"):               #for in in range(length):  if(name[i] in "aeiou"):
        count1 += 1                 #   count1 += 1

print(count1)



# palindrome

# Method 1

value = input("Enter value : ")
value = value.lower()

reverse_val = value[::-1]
if(value == reverse_val):
    print("True")
else:
    print("False")
    
    
# method 2

value1 = input("Enter value : ")
value1 = value1.lower()
length = len(value1)
new_val = ""
for i in range(length-1,-1,-1):
    new_val += value1[i]
    
if(value1 == new_val):
    print("True")
else:
    print("False")


# method 3
value1 = input("Enter value : ")
value1 = value1.lower().replace(" ", "")

left = 0
right = len(value1) - 1

while left < right:
    if value1[left] != value1[right]:
        print("Not a Palindrome")
        break

    left += 1
    right -= 1
else:
    print("Palindrome")


#largest number
#method 1

a = int(input("Enter num 1 : "))
b = int(input("Enter num 2 : "))
c = int(input("Enter num 3 : "))

print(max(a,b,c))

#method 2
if(a>=b):
    
    if(a>=c):
        print(a)
elif(b>=c):
    print(b)
else:
    print(c)
    
#method 3 - finding max and min
max_val = float('-inf')
min_val = float('inf')
while True:
    num = input("Enter value / type \"done\"  : ")
    if num == "done":
        break
    try:
        num = float(num)
    except ValueError:
        print("Invalid number, try again")
        continue

    if num > int(max_val):
        max_val = num
    if num < int(min_val):
        min_val = num

if max_val == float('-inf') and min_val == float('inf'):
    print("No numbers entered")
else:
    print(f"max : {max_val}")
    print(f"min : {min_val}")




#leap year 

year = int(input("Enter year : "))
if(year>0):
    if(year%4 == 0):
        if(year % 100 == 0 and year % 400 != 0):
            print(f"{year} is not a leap year")
            
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
        
else:
  print("Enter correct year") 



# Question : take a input from user..print the numbers from 1 to n...now if a number diivisible by 3 print fizz, divisible by 5 print buzz , both 3 and 5 print fizzbuzz , if its not divisible by both 3 and 5 print the number.
input_val = int(input("Enter how many numbers you want to enter : "))
list_val = []
for i in range(input_val):
    list_val.append(i+1)
print(list_val)   
for i in range(input_val):
    if(list_val[i]%3 == 0 and list_val[i]%5 == 0):
        list_val[i] = "Fizzbuzz"
    elif(list_val[i]%3 == 0):
        list_val[i] = "Fizz"
    elif(list_val[i]%5 == 0):
        list_val[i] = "Buzz"
    else:
        list_val[i] = list_val[i]

print(*list_val)            # * is used to unpack the list here




'''practice problem :
move all the zeros to the end of the list while maintaining the order of non-zero elements.'''

list_values = [4,0,4,6,0,1,76,0,65,89,0,65,45,9,87,0,0]
left = 0
right = 0
while(right < len(list_values)):
    if(list_values[left] != 0):
        left += 1
        right = max(right,left)
        
    elif(list_values[right] == 0):
        right += 1
        
    else:
        temp = list_values[left]
        list_values[left] = list_values[right]
        list_values[right] = temp
        left += 1
        right += 1
        
print(list_values)