def returnName(name):
    '''
    DOCSTRING: Information about the function for furture refrence
    INPUT: String that is your name
    OUTPUT: Greet with the input String
    '''

    print("Inside returnName")
    return ("Hello "+name)

greet = returnName(input("Enter Name: "))
print(greet)
print(help(returnName))