Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print(Belgium)

##task 1

print("-" * len(Belgium)) # len function times by belgium string (easier than interating through and counting num of chars)

##task 2

Belgium_list = Belgium.split(",") #created new variable to split existing string

print(Belgium_list)

Belgium_colon = ":".join(Belgium_list) #created second variable to swap comma with colon

print(Belgium_colon)

##task 2 - alternative

Belgium = Belgium.replace(",", ":") #replace function as an alternative to split and join

##task 3

print(Belgium_list) #kept string as list to extract info

population = int(Belgium_list[1]) + int(Belgium_list[3]) #used function 'int' to confirm numvalues and use addtion and extracted info from list using []

print(population)

