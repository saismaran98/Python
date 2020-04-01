def checkSubstring(substring, givenString):
    return substring in givenString.lower()

TrueString = 'This contains substring'
FalseString = 'This do not contain'

TrueResult = checkSubstring('substring',TrueString)
FalseResult = checkSubstring('substrign',FalseString)

print(TrueResult)       #Prints True
print(FalseResult)      #Prints False