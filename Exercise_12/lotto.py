##solution 1

import random

lotto_num = random.sample(range(1, 51), 6) #sample instead of randint, concatenating range and sample nums
print(lotto_num)


##solution 2

import random

lotto_num = [] #empty list for lotto num to append into

for i in range(6): #range 6, randint will iterate through and find 6 random numbers
    lotto_num.append(random.randint(1, 50)) #randint is random integer function

print(lotto_num)


