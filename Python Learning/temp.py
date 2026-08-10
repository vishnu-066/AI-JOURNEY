#binary search

list_values = list(range(2,100,3))

target = int(input("Enter the number you want to search : "))
low = 0
high = (len(list_values))-1

while low <= high:
    mid = low + ((high-low)//2)
    if(target < list_values[0] or target > list_values[(len(list_values)-1)]):
         print("Element not in list")
         break
    if(target == list_values[0]):

        print("0th index")
        break
    if(target == list_values[(len(list_values))-1]):
        print(f"{len(list_values)-1}th index")
        break

    if(target == list_values[mid]):
         print(f"{mid} th index")
         break

    elif(target > list_values[mid]):
         low = mid + 1
         

    elif(target < list_values[mid]):
         high = mid - 1

    
else:
     print("Element not in list")  
    
