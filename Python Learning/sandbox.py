# import time
# import sys

# pin_number = 1234
# money = 10000

# def login():
#   wrong_count = 1
#   while True:
#     pin = int(input("Enter 4 digit pin number : "))
#     if pin != pin_number:
#       print("Pin is incorrect, Please try again")
#       if wrong_count < 3:
#         wrong_count += 1
#       else:
#         for i in range(59,-1,-1):
#           print(f"\rAccount Freezed for  {i} sec", end="")
#           time.sleep(1)
#         print("\nAccount Unfreezed, Please try again")
#         wrong_count = 0
#     else:
#       menu()
      
#   print()
    


# def menu():
#   while True:
#     print("1. Check Balance ")
#     print("2. Withdrawl Balance ")
#     print("3. Deposit Money ")
#     print("4. Change pin ")
#     print("5. Exit ")
#     print()
#     operation = input("Chose an operation : ")
#     match operation:
#       case "1":
#         check_balance()
#       case "2":
#         with_draw = int(input("Enter withdrawl money : "))
#         withdrawl(with_draw)
#       case "3":
#         deposit_money = int(input("Enter deposit money : "))
#         money_deposit(deposit_money)
#       case "4":
#         old_pin = int(input("Enter old pin number : "))
#         change_pin(old_pin)
#       case "5":
#         end_session()
#       case _:
#         print("Enter correct input")

      
     

# def check_balance():
  
#   print(f"Current balance : {money}")  
#   print()
  


# def withdrawl(with_drawl_money):
#   global money
#   if money >= with_drawl_money and with_drawl_money > 0:
#     if with_drawl_money % 100 == 0:
#       money -= with_drawl_money
#       print("With_draw successfull....")
#       print(f"Current balance : {money}")
      
#     else:
#       print("Withdraw failed...Please enter money in hundreds...")
#   else:
#     print("Unsufficient balance...")
#   print()
 


# def money_deposit(deposit_money):
#   if deposit_money > 0 and deposit_money % 100 == 0:
#     global money
#     money += deposit_money
#     print("Money deposited successfully...!!")
#     print(f"Current Balance : {money}")
#   else:
#     print("Invalid input")
#   print()
  

# def change_pin(old_pin):
#   wrong_count = 1
  
#   while True:
#         if(wrong_count < 3):
#           global pin_number
#           if(old_pin == pin_number):
#               New_pin = input("Enter 4 digit new pin number that differ from old pin : ")
#               if(len(New_pin) == 4):
#                   New_pin = int(New_pin)
#                   if(pin_number != New_pin):
#                       pin_number = New_pin
#                       print("Pin changed successfully..!!")
#                       break
#                   else:
#                       print("Make sure New pin is differnt from old pin")
#                       continue
#               else:
#                   print("Pin length not matched...")
#                   continue
#           else:
#               print("Pin is not matched...!!")
#               wrong_count += 1
              
#               old_pin = int(input("Enter old pin number : "))
#         else:
#           for i in range(20,-1,-1):
#               print(f"\rLimit exceeded....Account freezed for {i} secs...", end="")
#               time.sleep(1)
#           break
#   print()
  

# def end_session():
#   print("Your session was ended..!!")
#   sys.exit()
  
# login()












#Created products,ids and values....based on ids user can add products to cart and getting the final price after applied discount.


#products and their values
def products_value():
  products_value = {
    "Mouse" : 800,
    "Keyboard" : 1100,
  "Wire" : 200,
  "plug" : 150,
  "bolts" : 250,
  'stand' : 750
  }
  return products_value

#products and their ids
def products_items():
   product_items = {101 : "Mouse",
      102 : "Keyboard" ,
    103 : "Wire",
    104 : "plug" ,
    105 : "bolts" ,
     106 : 'stand' }
   return product_items

#Created a decorator to check the login credentials and then access the cart function to add products to cart and get the final price after applied discount.
def login_page(func):
  def login():
      
      while True:
        login_id = int(input("Please enter your login id : "))
        password = input("Enter password : ")
        if login_id == 9110752349 and password == "Vishnu@2004":
          product_items = products_items()
          print("Item ID's...............")
          for val in product_items.items():
            print(*val)
          result = func()
          return result
        else:
           print("Enter correct Id or password")
           continue

  return login

@login_page
def cart():
  cart_items = {}
  cart_value = []
  Product_id = None
  product_items = products_items()
  product_value = products_value()
  while True:
      product_id = int(input("Enter Product Id : "))
      if product_id == 0:
         break
      else:
        
        if product_id in product_items:
            item_name = product_items[product_id]
            item_price = product_value[item_name]
            if item_name in cart_items:
                cart_items[item_name] += 1
            else:
                cart_items[item_name] = 1
            cart_value.append(item_price)
            print(f"Added {item_name} to cart.")
        else:
            print("Choose appropriate 'ID'")
  print("\n ....Your cart....")
  for item, quantity in cart_items.items():
      print(f"{item}: {quantity} = {product_value[item]} * {quantity} = {product_value[item] * quantity}/-")
  return cart_items,cart_value


#Function (closure) to calculate discount based on the rate provided
def discount_calculation(rate):
   def shopping_price(price):
      return (rate/100)*price
   return shopping_price


#Function to calculate the final price after applied discount based on the total price of the products in cart.
def calculations():
  items,value = cart()
  if(sum(value) > 2000):
    discount_percentage = 5
    premium_customer = discount_calculation(discount_percentage)
    discount_value = premium_customer(sum(value))
    print(f"Discounted_percentage = {discount_percentage}%")
    print(f"Discounted_price = {discount_value}/-")
    print(f"Total_price : {sum(value)} - {discount_value} = {sum(value) - discount_value}/-")

  else:
      discount_percentage = 3
      regular_customer = discount_calculation(discount_percentage)
      discount_value = regular_customer(sum(value))
      print(f"Discounted_percentage = {discount_percentage}%")
      print(f"Discounted_price = {discount_value}/-")
      print(f"Total_price : {sum(value)} - {discount_value} = {sum(value) - discount_value}/-")

  print("\n'Thank you.....Visit again...!!'")

calculations()

   

        
        






