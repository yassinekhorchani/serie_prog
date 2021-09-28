while True :
    ch=input('entrer 4 chiffre (obligatoire)')
    y=ch.isnumeric()
    if len(ch)==4 and y==True :
        break
x=1
for i in range (4) :
    x*=int(ch[i])
print('le produit de ses chiffres est : ',x)
    
