class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def email(self):
        return self.first + '.' + self.last + '@gmail.com'

    def fullname(self):
        return self.first + ' ' + self.last

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_str_1 = 'mike-girma-8000'

emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Doe', 60000)

new_emp_1 = Employee.from_string(emp_str_1)


print(new_emp_1.email())
