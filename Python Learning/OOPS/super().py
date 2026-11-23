"""If you wanna change the behavior of the parent method in child method then you can do it this process called method overriding
suppose you want parent method excution in child class with some add-on then here super() comes into the picture...
"""
class parent:
  
  def __init__(self,name,age,department):
    self.name = name
    self.age = age 
    self.department = department
  def display(self,year):
    return self.name,self.age,self.department,year

class child(parent):
  def __init__(self,name,age,department,branch,clg):
    super().__init__(name,age,department)
    self.branch = branch
    self.clg = clg
    
  def display(self,year,sems):
    parent_info = super().display(year)
    
    return parent_info + (self.branch,self.clg,sems)

p1 = parent("vishnu",23,"IT")
c1 = child("vishnu",23,"IT","cse","LPU")

print(p1.display(4))
print(c1.display(4,8))