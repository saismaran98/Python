#LESSER OF TWO EVENS: Write a function that returns the lesser of two given
#numbers if both numbers are even, but returns the greater if one or both numbers are odd

def func(number1, number2):
    if number1%2==0 and number2%2==0:
        if(number1>number2):
            return number2
        else:
            return number1
    else:
        if(number1>number2):
            return number1
        else:
            return number2

print(func(5,2))

#ANIMAL CRACKERS: Write a function takes a two-word string and
#returns True if both words begin with same lette

def animal(string1):

    string1 = string1.split(" ")
    return string1[0][0].lower() == string1[1][0].lower()

print(animal("This shreater"))


#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one
#of the integers is 20. If not, return False

def isTwenty(n1,n2):
    if n1==20 or n2==20:
        return True
    elif n1+n2==20:
        return True
    else:
        return False

print(isTwenty(10,10))


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

def capitalize(name):
    if len(name)==0:
        return ""
    elif len(name)<4:
        return ""+name[0].upper()+name[1:]
    elif len(name)==4:
        return ""+name[0].upper()+name[1:3]+name[3].upper()
    else:
        return ""+name[0].upper()+name[1:3]+name[3].upper()+name[4:]

print(capitalize("saismaran"))

