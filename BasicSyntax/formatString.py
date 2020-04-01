#   .format() use to insert multiple strings in a string position.

# Online Best Resourse for Print formatting "https://pyformat.info/"
string = "Original String {} {}"
string = string.format("Insert1","Insert2")     #Prints Original String Insert1 Insert2 as index not specified it assignes default values accoring to insert
print(string)


string = "Original String {1} {0}"
string = string.format("Insert1","Insert2")        #Prints Original String Insert2 Insert1 as the index mentioned.


string = "Original String {insert2} {insert1}"
string = string.format(insert1="Insert1",insert2="Insert2")  #Prints Original String Insert2 Insert1 as the index mentioned.
print(string+"\n")

result = 100/777

print("Original Value :{}".format(result))
print("Formatted result is {r:1.3f}".format(r=result))  #Float formatting follows "{value:width.precision f}"

#new feature in python 3.3 allows formatting literals

name = "saismaran"
age = 21
print(f"My name is {name} and my age is {age}") #Prints My name is saismaran and my age is 21 here we do not write i.e it is a format string
                            # .format({name}) insted mention f before hand and pass variable directly
