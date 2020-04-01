
#Q1: Print only word that starts with s in this sentence

st = 'Print only word that starts with s in this sentence'

st = st.split(' ')
for word in st:
    if(word[0].lower() == 's'):
        print(word)

#Q2:

for integer in range(1,101):
    if(integer%3 == 0 and integer%5==0):
       print("FizzBuzz")
    if(integer%3==0):
        print("fizz")
        continue
    if(integer%5):
        print("Buzz")
    print(integer)

#Q3:

st = 'Create a list of the first letters of every word in this string.'
newStr = ""
st = st.split(" ")
newStr = newStr.join([words[0] for words in st])
print(newStr)


