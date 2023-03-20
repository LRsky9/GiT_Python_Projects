from EX16 import Person
from EX16 import Employee
from EX16 import Customer

subject_1 = Person('Sam', '33', 'Durham')
print(subject_1.get_name())
print(subject_1.get_age())
print(subject_1.get_address())


subject_2 = Employee('Dan', '44', 'York', '8629473', 'Cleaner')
print(subject_2.get_name())
print(subject_2.get_age())
print(subject_2.get_address())
print(subject_2.get_employee_id())
print(subject_2.get_job())


subject_3 = Customer ('Ben', '25', 'Leeds', '87353', 'i@dontknow.com')
print(subject_3.get_name())
print(subject_3.get_age())
print(subject_3.get_address())
print(subject_3.get_customer_id())
print(subject_3.get_email())