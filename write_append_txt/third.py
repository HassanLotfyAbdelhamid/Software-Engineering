# write append

import os

# make sure working directory is in project folder (desired directory)
print(os.getcwd())

myFile = open("hassoona.txt", "w")

# writing lines
myFile.write("This is line 1\n")
myFile.write("This is ")
myFile.write("line 2\n")
myFile.write("This is three times duplicated line\n" *3)

# append
myFile = open("hassoona.txt", "a")
myFile.write("This is appended line\n") # appended at the end of lines

# adding list after append
myList = [ "hassan\n", "amr\n", "basma\n"] # if \n removed, names will be same line no spaces
myFile.writelines(myList) #write takes str, writelines takes list

myFile.close()


