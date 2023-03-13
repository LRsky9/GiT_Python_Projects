pelican = open("pelican.txt", 'w')

pelican.write("A wonderful bird is the pelican, \n")

pelican.write("His bill holds more than his belican,\n")

line = ["He can take in his beak, \n", "Enough food for a week, \n", "I'm damned if i see how the helican, \n"]

##\n used to create line breaks/new lines so data is not all stored in one continuous line.

pelican.writelines(line)

pelican.close()

pelican = open("pelican.txt", "r")

print(pelican.read())

pelican.close()
