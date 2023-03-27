from account import Account
from account import PersonalAccount


main = Account('9999999999', 2000, 100)
main.deposit(100)
main.withdraw(30)

personal = PersonalAccount('1234567890', 1000, 100)
personal.deposit(500)
personal.withdraw(200)


print(f"Account number: {main.account_number}| Main Account Balance: {main.get_balance()}")
print(f"Account number: {personal.account_number}| Personal Account Balance: {personal.get_balance()}")


