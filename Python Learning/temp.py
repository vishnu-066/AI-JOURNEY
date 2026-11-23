def highest_avg():
  sum = 0
  avg = sum/5  
  max_avg = 0
  for i in student_records:
    sum = 0
    for j in range(1,6,1):
      sum += j
    if(avg > max_avg):
      max_avg = avg
  return max_avg

def lowest_avg():
  sum = 0
  avg = sum/5
  min_avg = 501
  for i in student_records:
    for j in range(1,6,1):
      sum += j
    if(avg < min_avg):
      min_avg = avg
  return min_avg


def failed():
  fail_count = 0
  for i in student_records:
    for j in range(1,6,1):
      if(j < 40):
        fail_count += 1
        break
  return fail_count

def passed():
  pass_count = len(student_records) - failed()
  # for i in student_records:
  #   for j in range(1,6,1):
  #     if((j < 40) ):
  #       break
    
  return pass_count


def avg_greater_80():
  avg_list = []
  for i in avg_marks:
    if(i >= 80):
      avg_list.append(student_records[i][0])
  return avg_list
      
      

student_records = []
no_of_students = int(input("Enter no.of students to enter : "))
for i in range(no_of_students):
  particular_student = []
  student_name = input("Enter your name : ")
  particular_student.append(student_name)
  for i in range(5):
    student_marks = int(input("Enter your marks in 5 sub : "))
    particular_student.append(student_marks)
  
  student_records.append(particular_student)

avg_marks = []
sum = 0
for i in student_records:
  for j in range(1,6,1):
    sum += j
  avg = sum/5
  avg_marks.append(avg)

print(f"[ {highest_avg()}, {lowest_avg()}, {passed()}, {failed()}, {avg_greater_80()}")
    
# print(f"Max avg {highest_avg()}")
# for inner in student_records:
#   print(*student_records)
 
# =======================================================================================

# Online Python compiler (interpreter)
# Write and run Python online using this editor.

# from decimal import Decimal

# price = Decimal("0.1")
# tax = Decimal("0.2")

# total = price + tax
# print(total)      # 0.3
# result = Decimal("0.4") * Decimal("2.8")
# print(Decimal(result))

a = {1,2,4}
b = {1,2,4}
c = a
d = (a,b,c)
e = (a,b,c)
print(a is c)

# a = {2,3,4}
# b = {1}
# print(b + a)

a = "QwertyuiopasdfghjkldfghC thb zxcvbnm"
val = set(a.lower().replace(" ",""))
print(len(val))

f = {"a","A","b"}
print(f)

import math
a = math.inf
b = -(math.inf)
val = int(input("Enter number : "))
if(val>b):
  a = val
print(a)
print(b)
a = [2,67,9]
print(max(a))
print(math.sin(math.degrees(0.8939966636005579)))
print(round(math.cos(math.radians(90)),6))
print(type(round(3.83746834838,7)).__name__)

a="vishnu"
print(list(a))
b = [2,4,6]
print(type(b))

a = [45,67,89]
print("-".join(map(str,a)))
print(len(a))


name = "vishnu vardhan reddy"
print(name[-10:-1:1])

name = name.split()
print(" ".join([name[0],"-".join([name[1],name[2]])]))

def cal(val):
  return val*2

val=list(map(cal,[2,3]))
print(val)


import time

# for i in range(1, 101):
#     # \r resets to start of line; end="" prevents print from automatically adding \n
#     print(f"\rDownloading: [{i}%]", end="", flush=True)
#     time.sleep(0.2)

# print("\nDone!")

# import time

# for remaining in range(5, 0, -1):
#     print(f"\rTime left: {remaining:02d}s", end="", flush=True)
#     time.sleep(1)

# print("\rTime's up!      ")

import time

for ch in ["-", "\\", "|", "/"]:
    print(ch, end="", flush=True)
    time.sleep(0.3)
    print("\b", end="", flush=True)  # rewinds cursor so the next symbol overwrites

print("\nVishnu".casefold())
print("Vishnu".encode())

# ===========================================================================


# #1. Reverse a String

# # Take a string as input and print it in reverse without using [::-1].

# name = input("Enter input : ")
# for i in range(-1,-(len(name)+1),-1):
#   print(name[i],end = "")
# print()


# input_val = input("Enter input : ")
# input_val = input_val.lower()
# count = 0
# for i in input_val:
#   if(i in "aeiou"):
#     count += 1
# print(count)

#palindrome checker 

input_val = input("Enter value : ")
len_val = len(input_val)
start = 0
end = len_val -1

  

while(start < end):
  if(input_val[start] != input_val[end]):
    print('Not a palindrome')
    break
  start += 1
  end -= 1
else:
  print("Palindrome")
    
    
      
      
  