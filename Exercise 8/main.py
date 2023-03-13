#if statement

#number=int(input("Enter number:"))
#distance=int(input("Enter distance:"))

#if 0 < number < 42 < distance:
 #   print("number and distance are in range")
#else:
 #   print("number and distance are out of range")

#while loop

#line = None
#while line != 'done':
 #   line = input('Type "done" to complete')
  #  print ('<', line, '>')


mylist = ['arm', 'leg', 'head']
if 'arm' in mylist:
    print("arm is here")

print(mylist)

if mylist:
    print(True)
else:
    print(False)


for index, value in enumerate(mylist, start=1):
    print(index, value)

import sys

x = 'hello'
print(x)
sys.exit("goodbye")

