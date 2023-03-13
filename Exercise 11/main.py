import random

lotto = (1, 51)

random_numbers = random.sample(range(1, 51), 6)
print(random_numbers)



#This code uses the sample method of the random module to generate a list of 6
# unique random numbers between 1 and 50. The range function is used to generate a
# sequence of integers from 1 to 50 (inclusive), and the sample method randomly
# selects 6 numbers from this sequence without replacement.


