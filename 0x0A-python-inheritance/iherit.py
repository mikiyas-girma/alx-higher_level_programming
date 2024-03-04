
class Person:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name, self.id)


class Emp(Person):

    def Print(self):
        print("Emp class called")


Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()


emp = Person('mikiyas', 2193)
emp.display()
