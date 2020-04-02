
def myfunc(**kwargs):
    print(kwargs)
    if 'key1' in kwargs:         #If the key is present in the dict 'kwargs'
        print(f"The value of the key is {kwargs['key1']}")
def newfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print(f"args0: {args[0]}\tkwargs['key2']: {kwargs['key2']}")

myfunc(key1='value1',key2='value2')
newfunc(10,20,30,key1='value1',key2='value2')   #maintain the order according to the parameter function


