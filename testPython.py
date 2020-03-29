List = []
for x in [2,3,4]:
    for y in [100,1000,10]:
        List.append(x*y)

print( [listEmems for listElems in List] )

#Does same job as Upeer nested Loops

print( [elementX*elementY for elementX in [2,3,4] for elementY in [100,1000,10]] )