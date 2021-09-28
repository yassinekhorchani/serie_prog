from random import randint
x=input("L'operateur TN vous souhaite la bienvenue")
y=randint(1,10)
print('la roulette sarrete sur ',y)
if y%2==0 :
    print('revenez la prochaine fois')
elif y==1 :
    print('Forfait Internet 500Mo')
elif y==3 :
    print('Forfait Internet 1Go')
elif y==5 :
    print('Forfait Internet 200Mo')
elif y==7 :
    print('Forfait Téléphonique 2h')
elif y==9 :
    print('Forfait Téléphonique 8h')
