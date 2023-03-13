## ORIGINAL SOLUTION
## UNDERSTOOD IT NEEDED A WHILE LOOP OR IF STATEMENT FOR NUM OF ATTEMPTS, HAD TO RESEARCH HOW AFTER SOME FAILED ATTEMPTS
##SOLUTION BELOW USED WHILE LOOP AND F STRING, WORKS WELL##
##import getpass - WHEN USIMG THIS, COULD NOT ENTER NUMBERS IN RUN BOX
import getpass



pin = '1234'
attempt = 1


while attempt <= 3:
    supplied_pin = getpass.getpass('Enter You PIN:')
    if pin == supplied_pin:
        print('PIN Successful')

        break

    else:
        print('Incorrect PIN')
        attempt += 1

##SOLUTION WITH HELP

pin = '1234'
max_attempts = 3
attempt = 1

while attempt <= max_attempts:
    supplied_pin = input(f'Enter your PIN (attempt {attempt} of {max_attempts}): ')

    if supplied_pin == pin:
        print('PIN Successful')
        break
    else:
        print(f'Incorrect PIN. You have {max_attempts - attempt} attempts remaining.')
        attempt += 1






