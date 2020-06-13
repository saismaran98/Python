def squre(num):
    return num*num

newArr = [1,3,4]
for number in map(squre,newArr):
    print(number)

print(list(map(squre,newArr))[0])

squre = lambda num: num**2

print(squre(5))

names = ["andy","rose","charlie"]

print(list(map(lambda name:name[::-1],names)))      #Reverse all the names in the array names.


