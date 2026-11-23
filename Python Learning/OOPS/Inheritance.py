#Inheritance means acquiring the properties of a class into another class. The class which inherits the properties of another class is called a subclass (or derived class, child class), and the class whose properties are inherited is called a superclass (or base class, parent class).
"""
Some basic questions...
Why we need inheritance?
When we use this, why cant we simply implement all the things in a single class?
Whats the difference between multiple objects in a single class and multiple classes?
Types of inheritance..
"""

#Lets take an example :
"""Suppose i am running a startup company...i have 3 different teams...each team has different responsibilities right....but the common thing all they have is their details(Attributes) like name, salary, emails etc and methods like display etc...so lets implement this.."""
#Wthout inheritance
class employees:
    def __init__(self,name,age,salary,experience):
        self.name = name
        self.age = age
        self.salary = salary
        self.experience = experience

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Experience: {self.experience}")

class Manager:
    def __init__(self,name,age,salary,experience):
        self.name = name
        self.age = age
        self.salary = salary
        self.experience = experience

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Experience: {self.experience}")

    def Manager_specific_method(self):
        print("This is a manager-specific method.")


class HR:
    def __init__(self,name,age,salary,experience):
        self.name = name
        self.age = age
        self.salary = salary
        self.experience = experience

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Experience: {self.experience}")

    def HR_specific_method(self):
        print("This is an HR-specific method.")

class Developer:
    def __init__(self,name,age,salary,experience):
        self.name = name
        self.age = age
        self.salary = salary
        self.experience = experience

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Experience: {self.experience}")

    def Developer_specific_method(self):
        print("This is a developer-specific method.")


Man = Manager("Vishnu", 30, 50000, 5)
HR = HR("Virat", 28, 40000, 3)
Dev = Developer("Emil", 25, 60000, 2)

Man.display()
Man.Manager_specific_method()
print("--------------------")
HR.display()
HR.HR_specific_method()
print("--------------------")
Dev.display()
Dev.Developer_specific_method()


"""Here the above code problem is that we are repeating the same attributes and methods through all classes manually...what if we have 10+ teams do we sit and write the same code throught out the day...it takes lot of time and effort to implement this..
Suppose we want to add one more attribute to all employees like "email" then we have to go through all the classes and add this attribute manually...so to avoid this we can use inheritance..."""



#Lets implement this with inheritance...

class Employee:
    def __init__(self,name,age,salary,experience):
        self.name = name
        self.age = age
        self.salary = salary
        self.experience = experience

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Experience: {self.experience}")

class Manager(Employee):
    def Manager_specific_method(self):
        print("This is a manager-specific method.")

class HR(Employee):
    def HR_specific_method(self):
        print("This is an HR-specific method.")

class Developer(Employee):
    def Developer_specific_method(self):
        print("This is a developer-specific method.")



Man = Manager("Vishnu", 30, 50000, 5)
HR = HR("Virat", 28, 40000, 3)
Dev = Developer("Emil", 25, 60000, 2)

Man.display()
Man.Manager_specific_method()
print("--------------------")
HR.display()
HR.HR_specific_method()
print("--------------------")
Dev.display()
Dev.Developer_specific_method()

"""Here we can see that we have implemented the same functionality as before but with less code and more efficiency...internally python will 
inherit the properties of the parent class(Employee) into the child classes(Manager, HR, Developer) and we can access the methods and attributes of 
the parent class in the child classes without having to write them again..."""
"""In the above we code we called the display method in Manager, HR and Developer clsses but these classes doesn't contain this method then how python displayed the message without throwing an error...
Here the main picture MRO(Method resolution order) ... Here python will check first in child class if the method or attribute present in that class then it will return , if its not present in child class then it loopup
 into the parent class , if its present in parent thyen it will excute other wise it will throw an error..."""




# ==============================================================



