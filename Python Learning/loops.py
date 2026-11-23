#while loop...
#basically while loop is used when we dont know how many steps we need to perform..
#lets take an example with a game ...i have 5 boxes i want to pick box by box if i found a key then i need to stop the loop..
#we can use while loop here because we dont know in which box the key is present so we will keep on checking until we find the key or we check all boxes and if we dont find the key then we will print key was not found in boxes
#we can also use else statement with while loop which will be executed when the while loop is not terminated by break statement.
box = ["Not Found","Not Found","Not Found","Found","Not Found"]
i = 0
while i<len(box):
         if box[i] == "Found":
                  print(box[i], "in", i+1, "th box")
                  break
         i += 1
else:
         print("Key was not found in boxes")



# take the inputs from user continuosly until user enters a specific value to stop the loop. return the max value whithout using extra space or list to store the values.

#method 1

max_val = None

while True:
         input_val = int(input('Enter value : '))

         if input_val == 0:
                  break
         if max_val is None or input_val > max_val:
                  max_val = input_val

if max_val is None:
         print("Nothing entered")
else:
         print(max_val)


#method 2


max_value = float("-inf")
while True:
         user_input = input("Enter a number (or 'stop' to finish): ")
         if user_input.lower() == "stop":
                  break
         try:
                  num = float(user_input)
                  if num > max_value:
                           max_value = num
         except ValueError:
                  print("Please enter a valid number or 'stop' to finish.")
print("The maximum value entered is:", max_value)



#Fizzbuzz program using while loop and list to store the values and print the list at the end of the program.
print("enter stop when you want to stop the program..\n")

list_val = []

while True:
    user_input = input("Enter value (type stop to finish): ")

    if user_input.lower() == "stop":
        break

    num = int(user_input)

    if num % 3 == 0 and num % 5 == 0:
        list_val.append("FizzBuzz")
    elif num % 3 == 0:
        list_val.append("Fizz")
    elif num % 5 == 0:
        list_val.append("Buzz")
    else:
        list_val.append(num)

print(list_val)


