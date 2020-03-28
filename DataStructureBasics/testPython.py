
#Useful Operators:

#Range

for num in range(10):
    print(num)  #print 0 to 9
for num in range(5,10):
    print(num)  #print 5 to 9

#range(start, end, step size)

#Efficient Way = typecast to a list and print to save memory

print(list(range(0,10,2)))  # prints : [0, 2, 4, 6, 8]