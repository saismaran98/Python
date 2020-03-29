
priceOf = {'Apple':120.0,'Banana':60.0,'Coconut':20.0}

print(priceOf['Apple'])

nestedDict = {'k1':[{'nested_key':['this is deep',['hello']]}]}

print(nestedDict['k1'][0]['nested_key'][1][0])

print(nestedDict.items())  #Fetch the value from nested dict and made it upper case and gave outuput : NESTTED DICT_VALUE

 #Add new key value pair to a existing dict

priceOf['Iphone'] = 60000.0
priceOf['Iphone'] = 60000.87999
print(priceOf)

print(f'Values: {priceOf.keys()}') # returns the set of all keys
print(priceOf.values())     #returns the value of all keys

  