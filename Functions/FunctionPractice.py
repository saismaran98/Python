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

print("Animal Cracker",animal("This Shreater"))


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

#Given the word return the word reversed


def reverseSentense(sentence):
    revSen=""
    i = 1
    lengthOfSentence = sentence.split()
    reverse = lengthOfSentence[::-1]
    revStr = " ".join(reverse)
    return revStr



print(reverseSentense("I am home"))

#Given number is within the range of 10 from 100, 200

def checkAbsMethod(number):
    return (abs(100-number)<=10 or abs(200-number)<=10)         #difference betwn number and 100/200 is within 10 or not ex 94,204

print(checkAbsMethod(int(94)))

#Given a array return true if it has two consecutive 3 somewhere

def has_33(numArr):

    for i in numArr:
        if(numArr[i:i+2]) == [3,3]:     #Grabbing the slice of the array and comparing if its 3,3 Alternative: if nums[i] == 3 and nums[i+1] == 3: (code)
            return True
    return False

print(has_33([1,3,3]))  #returns True

#Given a string return a string with all char*3 times.

def paper_doll(text):
    result = ""
    for char in text:
        result += char*3
    return result

print("PaperDoll: "+paper_doll("Hello"))

#BlackJack GIven three integes between 1 and 11 return sum if sum <= 21, if sum>21 and 11 is there in array reduce sum by 10 and return if sum >21 return bust

def blackjack(a,b,c):

    if(sum([a,b,c])<21):
        return sum([a,b,c])
    else:
        if(a==11 or b==11 or c==11):
            newSum = sum([a,b,c])-10        #or elif 11 in [a,b,c] and sum([a,b,c]) -10<=21: return sum([a,b,c])-10
            if newSum>21:
                return "BUST"
            else:
                return newSum


    return "BUST"
print(blackjack(9,9,11))

#Summer_69:

def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6 :
                total+= num
                break
            else:
                add = False

        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
print(summer_69([2,1,6,9,11]))

def upper_lower(string):
    #maintain a dictionary insted of a counter to make it simple and readable.
    dictionary = {'upper':0,'lower':0}  #key upper -> initial value 0 and key lower -> initail value 0

    for character in string:
        if(character.isupper()):
            dictionary['upper'] += 1
        elif(character.islower()):
            dictionary['lower'] +=1
        else:
            pass
    print(f'upper_count = {dictionary["upper"]} and lower_count = {dictionary["lower"]}')       #since you use 'single quotes' outside use "double quotes" inside else you get an error.


upper_lower("SaismaranHOta")

#take a list and return the unieq element in the list

def unique(lst):
    return list(set(lst))   #we convert list to set and as set cannot contain duplicate elements we then conver it back to list and return it.

print(unique([1,1,1,4,5,6,3]))

#check pallindrome

def pallindrome(string):
    #remove spaces from the string
    string.replace(' ','')

    #check pallindrome
    if string == string[::-1]:
        return True
    else:
        return False

print(pallindrome("sas"))