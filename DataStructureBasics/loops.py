
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

itemList = ['Meggi','Chowmin','Soya Sause']

for items in itemList:
    #Wanna 'do nothing' or debugging purpouse hence no code inside the loop
    #Pyhon doesnt want blank codes in loop hence we use pass
    pass

for items in itemList:
    if items == 'Meggi':
        continue        #When item = Meggi it will go to the top and wont print Meggi
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