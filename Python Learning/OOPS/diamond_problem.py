
class Employee:
    def __init__(self, name, salary, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        # Your implementation here
        
        super().__init__(**kwargs)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")


class Manager(Employee):
    def __init__(self, team_size, **kwargs):
        # Your implementation here
        super().__init__(**kwargs)
        self.team_size = team_size

    def display(self):
        super().display()
        print(f"Team Size: {self.team_size}")


class TechnicalLead(Developer, Manager):
    def __init__(self, project_name, **kwargs):
        # Your implementation here
        super().__init__(**kwargs)
        self.project_name = project_name

    def display(self):
        super().display()
        print(f"Project Name: {self.project_name}")


tc = TechnicalLead(
    name="Vishnu",
    salary=90000,
    programming_language="Python",
    team_size=12,
    project_name="Vistra",
    
    
)

tc.display()
