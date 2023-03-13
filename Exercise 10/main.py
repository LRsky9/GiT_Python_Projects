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
        attempt +=