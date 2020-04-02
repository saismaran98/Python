
def skyline(s):
    result = ""
    for i, v in enumerate(s):
        if i%2==0:
            result = ''.join(v.upper())
        else:
            result = ''.join(v.lower())
    return result

print(skyline("Thiismyname"))