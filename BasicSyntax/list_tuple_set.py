
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

#Sets set() = does not contain duplicate value and it can be used to delete duplicate
#values from list


l = [1,1,1,1,2,3,2,1,1]

newSet = set(l)     #Elements from list became unique set
newSet.add(5)       #add element to the set using .add()
print(newSet)

