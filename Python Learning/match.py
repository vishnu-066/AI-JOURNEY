#matching the values using match case statement

a = 7
month = 5
match a:
         case 1:
                  print("1")
         case 2:
                  print("2")
         case 4 if month == 6:
                  print("3")
         case 4 | 5 if month == 5:
                  print("4")
         case _:
                  print("_")