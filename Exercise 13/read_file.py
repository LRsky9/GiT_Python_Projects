pelican = open("pelican.txt")

print(pelican.read())

##type of data returned is a string

with open("pelican.txt") as pelican:
    con_list = pelican.readlines()


print(con_list, len(con_list))

##data now converted to a list via .readlines()
##counted the number of lines in the list

with open("pelican.txt") as pelican:
    for line in pelican:
        print(line.strip())





