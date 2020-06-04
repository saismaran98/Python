
#---------------------------------WHILE LOOP------------------------------------

#Simple while loop:

x = 0
while x<5:
    print(f'Value of x is {x}')
    x+=1
else:
    print('X is not less thrn 5')   #finally used when while condition fails

#   Break    : Break out of the current loop
#   Continue : Goes to the top of the loop
#   Pass     : Does nothing at all

itemList = ['Maggi','Chowmin','Soya Sause']

for items in itemList:
    #Wanna 'do nothing' or debugging purpouse hence no code inside the loop
    #Pyhon doesnt want blank codes in loop hence we use pass
    pass

for items in itemList:
    if items == 'Maggi':
        continue        #When item = Maggi it will go to the top and wont print Meggi
    print(items)


for items in itemList:
    if items == 'Chowmin':
        break        #Breaks loop when item = chowmin hence only print Meggi
    print(items)

#---------------------------------FOR LOOP--------------------------------------
List = [1,2,'3rd']

for index in List:
    print(index)

for _ in List:              # '_' tells we dont wamna use any variable
    print('Item Present')

myList = [(1,2),(3,4),(5,6),(7,8)]

for odd,even in myList:  #(a,b) tuple unpacking i.e duplicate the packet inside and unpack it.
    print(even)

#Iterating through a dictionary:

myDict = {'key1' : 'Value1','key2' : 'Value2'}

#By default it prints the key

for item in myDict:
    print(item),

print("\n")#nextLine

for key,value in myDict.items():    #as Items contains both key value pair
    print(key+" "+value,end="\t")
print("\n")
#If only want the values you can use tuple unpacking
#Generally Dictionary are unordered.
for values in myDict.values():
    print(values,end=" ")
print("\n")

#--------------------------------------------------Useful Operators:

#Range

for num in range(10):
    print(num)  #print 0 to 9
for num in range(5,10):
    print(num)  #print 5 to 9

#range(start, end, step size)

#Efficient Way = typecast to a list and print to save memory

print(list(range(0,10,2)))  # prints : [0, 2, 4, 6, 8]

#--------------Zip

List1 = ['a','b','c','d']
List2 = [1,2,3,4]

comboList = list(zip(List1,List2))
print(comboList)

#   List  Unpacking:

for a,b in comboList:
    print(a+" "+str(b))

#-----------------------------------------------------------IN KeyWord Opetator
#in Function to check if an item is present in the list

print(('b',2) in comboList)

print('Much' in 'nothingMuch') #Check for substring returns true

print('key1' in {'key1':'value1'})  #returns true
print('value1' in {'key1':'value1'}.values())   #returns true

from random import shuffle

print(min(List1))       #Returns a

shuffle(List2)
print(List2)    #Returns randomm shuffeled list.

#RandInt

from random import randint
randNo = randint(0,100)
print(randNo)   #Return random no bet^n 0-100 and the return type is 'Method'


