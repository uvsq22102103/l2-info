import random as rd

reponse = None
dico_decimal = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
dico_exceptions = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fiveteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
dico_dizaine = {20:'twenty',30:'thirty',40:'fourty',50:'fivety',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

while reponse != '':
    nb = (rd.randint(0,9),rd.randint(0,9))

    print(str((nb[0]*10)+nb[1]),'en anglais ?\n')
    reponse = input('>>>>>>')

    if nb[0] == 0:
        v = dico_decimal[nb[1]]
        print(v == reponse)
    elif nb[0] == 1:
        v = dico_exceptions[(nb[0]*10)+nb[1]]
        print(v == reponse)

    elif nb[1] == 0:
        v = dico_dizaine[nb[0]*10]
        print(v == reponse)
    else:
        v = dico_dizaine[nb[0]*10]+' '+dico_decimal[nb[1]]
        print(v == reponse)

    print('La réponse est : '+v)