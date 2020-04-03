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