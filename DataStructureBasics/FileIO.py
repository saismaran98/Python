myfile = open('text.txt')
print(myfile.read())
print(myfile.readline()) #print a list of lines where each element is a line

myfile.close()

#Using with open we dont need to close it.
#We don't need to explicitly call the close() method. It is done internally.
with open("text.txt") as f:
    content=f.read()
    print(content)
