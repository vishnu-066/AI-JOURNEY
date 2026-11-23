"""1. Employee class
- Initialize name and salary.
- Create a display() method to display both.
2. Developer class
- Inherit from Employee.
- Initialize programming_language.
- Override display() and use super().
3. Manager class
- Inherit from Employee.
- Initialize team_size.
- Override display() and use super().
4. TechnicalLead class
- Inherit from both Developer and Manager.
- Initialize project_name.
- Use cooperative constructor chaining with **kwargs.
- Override display() and use super()."""

class Employee:
  def __init__(self,name,salary,**kwargs):
    super().__init__(**kwargs)
    self.name = name
    self.salary = salary

  def display(self):
    print(f"Name : {self.name}")
    print(f"salary : {self.salary}")

class Developer(Employee):
  def __init__(self,programming_language,**kwargs):
    super().__init__(**kwargs)
    self.programming_language = programming_language
    
  def display(self):
    super().display()
    print(f"programming_language : {self.programming_language}")
    
  
class Manager(Employee):
  def __init__(self,team_size,**kwargs):
    super().__init__(**kwargs)
    self.team_size = team_size

  def display(self):
    super().display()
    print(f"Team_size = {self.team_size}")

class TechnicalLead(Developer,Manager):
  def __init__(self,project_name,**kwargs):
    super().__init__(**kwargs)
    self.project_name = project_name

  def display(self):
    super().display()
    print(f"Project_Name : {self.project_name}")

TL = TechnicalLead(
  name = "Vishnu",
  salary = 90000,
  programming_language = "Python",
  team_size = 12,
  project_name = "AI Assistant",
)

TL.display()
  
  


"""You have three employee types:
- Developer
- Manager
- Designer
Each employee has a different salary calculation.

Your requirements:
1. Create a parent class Employee.
2. Create three child classes.
3. Override calculate_salary() in each child class.
4. Use polymorphism to calculate everyone's salary.
5. Store all employees in one list and iterate through it."""

class Employee:
  
  def __init__(self,salary,leaves):
    self.leaves = leaves
    self.salary = salary
    
  def calculate_salary(self):
    self.leaves_deduction =  (self.salary//30) * self.leaves
    print(f"Deducted amount as a leave : {self.leaves_deduction}")

class Developer(Employee):
  night_alloances = 700
  def __init__(self,Night_shifts_days,**kwargs):
    super().__init__(**kwargs)
    self.Night_shifts_days = Night_shifts_days

  def calculate_salary(self):
    super().calculate_salary()
    self.Total_salary = (self.salary - self.leaves_deduction) + (self.Night_shifts_days * Developer.night_alloances)
    return f"Total Salary : {self.Total_salary}/-"


class Manager(Employee):
  allowance_per_project = 3000
  def __init__(self,No_of_projects,**kwargs):
    super().__init__(**kwargs)
    self.No_of_projects = No_of_projects

  def calculate_salary(self):
    super().calculate_salary()
    self.Total_salary = (self.salary - self.leaves_deduction) + (self.No_of_projects * Manager.allowance_per_project)
    return f"Total Salary : {self.Total_salary}/-" 
    
    
  
class Designer(Employee):
  allowance_per_design = 900
  def __init__(self,UI_designs,**kwargs):
    super().__init__(**kwargs)
    self.UI_designs = UI_designs

  def calculate_salary(self):
    super().calculate_salary()
    self.Total_salary = (self.salary - self.leaves_deduction) + (self.UI_designs * Designer.allowance_per_design)
    return f"Total Salary : {self.Total_salary}/-" 


def employee_call(self):   #duck typing concept
  print(f"Employee type : {type(self).__name__}")
  print(self.calculate_salary())
 
employees = [Developer(salary = 50000,leaves = 3, Night_shifts_days = 23), Manager(salary = 60000, leaves = 2, No_of_projects = 6), Designer(salary = 45000, leaves = 3, UI_designs = 4)]
for employee in employees:
  employee_call(employee)