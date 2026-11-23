#static and class methids

#create a class company
class company:
  company_name = 'Google'
  hike_per = 5
  #dunder method
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary

  #instance method
  def email(self):
    return f"{self.name.lower()}@{self.company_name.lower()}.com"
  #class method
  @classmethod
  def increment_per(cls,percent):
    cls.hike_per = percent
  @classmethod
  def getter(cls):
    return cls.hike_per

emp1 = company("Vishnu",25000)
emp2 = company("virat",30000)

print(emp1.email())
company.increment_per(10)
print(company.getter())