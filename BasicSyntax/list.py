
listOfBoys = ['Ram','Shyam','Gurprit']
listOfBoys.append('Teddy')
print(listOfBoys)

l1 = [1,[1,2,1,3],3]  #list Under a list
print(l1[1].count(1))

tup = ('Saismaran',245.0)

#Tuple doesnot allow assign i.e it is immutable i.e maintains data integrity
print(l1.index(3))
print(tup.count(255))

#Tuple = () List = []

#   List comprehension:

#   Usual method:

name = "Saismaran Hota"
nameList = []
for characters in name:
    nameList.append(characters)         #Remember the indentation
print(nameList)

#We can accomplish the same using

nameList = [characters for characters in name]

print(nameList)

numList = [ num+num for num in range(0,10) ]
print(numList)      #print 0, 2, 4, 6, 8, 10, 12, 14, 16, 18

#printing even squre number

print([ Int**2 for Int in range(0,11) if Int%2==0]) #0, 4, 16, 36, 64, 100]

# [ (Variable Update) for (initialise variable name) in condition/range body/logic part]

#--------------Nested for loop using List comprehension
List = []
for x in [2,3,4]:
    for y in [100,1000,10]:
        List.append(x*y)

print( [listEmems for listEmems in List] )

#Does same job as Upeer nested Loops With readability sacrifise: @Depricated

print( [elementX*elementY for elementX in [2,3,4] for elementY in [100,1000,10]] )