

def myfunc(*args):
    #passing n no of arguments to the function
    for item in args:
        print(item)
    return sum(args)

print(myfunc(1,1,1,1,1))

#Take arbitary number and return a list of number that are even:
#----------------------------------Solution 1----------------------
def newfunc(*args):
    return [number for number in args if(number%2==0)]

result = [ newfunc(num) for num in range(1,11) if(len(newfunc(num))!=0)]
for num in result:
    print(num,end=" ")
print()

#---------------------------------Solution 2------------------------

def evenfunc(*args):
    result = []
    count = 0
    for number in args:
        print(count)
        if number%2==0:
            result.append(number)

    return result

result = evenfunc(1,2,3,4,5,6,7,8,9,10)

print(result)