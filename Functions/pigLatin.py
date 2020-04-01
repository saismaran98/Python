#if word starts with a vowel add ay to the end
#if does not starts with a vowel put first letter to last and then add ay

def pigLatin(word):
    vowels = 'aeiou'
    if(word[0].lower() in vowels):
        return word+"ay"
    else:
        return word[1:]+word[0]+"ay"

print(pigLatin("apple"))    #prints appleay
print(pigLatin("word"))     #prints ordway