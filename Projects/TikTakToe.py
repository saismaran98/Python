from IPython.display import clear_output

def displayBoard(userChoice):
    clear_output()
    print("+-----------+")
    print('| '+userChoice[0]+' | '+userChoice[1]+' | '+userChoice[2]+' | ')
    print("-------------")
    print('| '+userChoice[3]+' | '+userChoice[4]+' | '+userChoice[5]+' | ')
    print("-------------")
    print('| '+userChoice[6]+' | '+userChoice[7]+' | '+userChoice[8]+' |')
    print("+-----------+",end="")
    print()


displayBoard([' ']*9)
