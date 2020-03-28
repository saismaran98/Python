
#Find the length of a given string

s = "Hello World"

print("OneLineIndex"[0] +"\n"+ "OneLineIndex"[0:3:])    #returns 'O' and One

print(len(s))       #Prints the length of the string "Hello World"

#Getting values from differnet index of a string

print(s[1] +'\n'+ s[-3])    #s1[1] return the index at 1 and s[-1] returns r i.e 3rd index from reverse string

#Slicing the string

print(  s[2:])
#[startIndex: upToIndex: Steps(intervals)]

print(s[2:7:2])

print(s[::2])   #jump 2 steps and print the string

#reversing s uing jump
print(s[::-1])

#String Concardination using '*' and '+' operator

testString = "sai "
print("Using Add: "+testString+testString+testString + "\n"+"Using *: "+testString*5)

#Split a string based on a character
print(s.split())    #split based on white spaces by default and give output as ['Hello', 'World']

print(s.split('l')) #split based on character 'l' and give output as ['He', '', 'o Wor', 'd']

