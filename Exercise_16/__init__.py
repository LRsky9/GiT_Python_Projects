class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_address(self):
        return self.address


class Employee(Person):
    def __init__(self, name, age, address, employee_id, job):
        #super() takes the def from superclass (Person) and pulls that into the sub classes of Employee and Customer
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.job = job

    def get_employee_id(self):
        return self.employee_id

    def get_job(self):
        return self.job


class Customer(Person):
    def __init__(self, name, age, address, customer_id, email):
        super().__init__(name, age, address)
        self.customer_id = customer_id
        self.email = email

    def get_customer_id(self):
        return self.customer_id

    def get_email(self):
        return self.email