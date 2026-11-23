

team_A_total = 0
team_B_total = 0
import random
def operators():
  print("Both team total values are '0' now, so choose the operator wisely")
  print("typr '+' addition")
  print("typr '-' subtraction")
  print("typr '*' multiplication")
  print("typr '/' division, if numerator is less than denominator then total resets to 0")
  print("typr 'p' base to power of 2")

def operations_team_A():
  team_A = random.randint(1,100)
  print(f"Team A : {team_A}")
  operation_count_A = []
  while True:
    team_A_input = input("Enter your operation A: ")
    
    if(operation_count_A.count(team_A_input) >=2):
      print("Operation limit exceeded, select another operator")
      
    else:
      operation_count_A.append(team_A_input)
      global team_A_total
    team_A_total = team_A_total + team_A if team_A_input == "+" else team_A_total - team_A if team_A_input == "-" else team_A_total * team_A if team_A_input == "*" else team_A_total // team_A if team_A_input == "/" else team_A_total + pow(team_A,2) if team_A_input == "p" else "Enter correct input."
    
    break

def operations_team_B():
  team_B = random.randint(1,100)
  print(f"Team B : {team_B}")
  operation_count_B = []
  while True:
    team_B_input = input("Enter your operation B : ")
    
    if(operation_count_B.count(team_B_input) >=2):
      print("Operation limit exceeded, select another operator")
      
    else:
      operation_count_B.append(team_B_input)
      global team_B_total
  
    team_B_total = team_B_total + team_B if team_B_input == "+" else team_B_total - team_B if team_B_input == "-" else team_B_total * team_B if team_B_input == "*" else team_B_total // team_B if team_B_input == "/" else team_B_total + pow(team_B,2) if team_B_input == "p" else "Enter correct input."
    
    break
  
def operation_call():
  i = 0
  while i < 3:
    operations_team_A()
    operations_team_B()
    i += 1
  print(f"{team_A_total=}")
  print(f"{team_B_total=}")
  print(f"{var_name(max(team_A_total,team_B_total))} is the winner...")

def var_name(target_val):
  return [name for name, value in globals().items() if value is target_val]

operators()
operation_call()

#error 1 : operation counting bug
#error 2 :  

    
    
    
    
    
  