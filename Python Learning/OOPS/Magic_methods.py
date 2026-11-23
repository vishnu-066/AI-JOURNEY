#Dunder methods...(magic methods) these are spcl type of methods that we can able to costomize these methods and python syntax will automatically call these...

class abc:
  
  def __init__(self,name,age):
    self.name = name
    self.age = age
    self.names = ["latha","Vishnu","Emil"]
  def __str__(self):
    return f'Name : {self.name}'
  def __repr__(self):
    return f"Name : ({self.name})"
  def __len__(self):
    return len(self.name)
  def __add__(self,other):
    return abc("Total",self.age + other.age)
  def __sub__(self,other):
    return self.age - other.age
  def __eq__(self,other):
    return self.age == other.age
  def __contains__(self,name):
    return name in self.names
  def __lt__(self,other):
    return self.age<other.age
  

q1 = abc("vishnu",21)
q2 = abc("Vardhan",22)
q3 = abc("sbdh",34)
print(q1)
print(len(q1))
print((q1+q2+q3).age)
print(q1-q2)
print(q1==q2)
print("Vishnu" in q1)
x = sorted([q1,q2,q3])
print(x[0].name)
print(q1.__dict__)