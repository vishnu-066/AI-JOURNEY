"""method overriding  -- here you are overriding the method of parent class in child class (changing the behavior of the method with same name of parent class method)"""
class parent:
  
  def __init__(self,name,age,department):
    self.name = name
    self.age = age 
    self.department = department
  def display(self):
    return self.name,self.age,self.department

class child(parent):
  def __init__(self,name,branch,clg):
    self.name = name
    self.branch = branch
    self.clg = clg
    
  def display(self):
    return self.name,self.branch,self.clg

p1 = parent("vishnu",23,"IT")
c1 = child("vardhan","cse","LPU")

print(p1.display())
print(c1.display())