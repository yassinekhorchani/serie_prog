while True :
    date=input("entrer un date")
    x=date[0:2].isnumeric()
    y=date[3:5].isnumeric()
    z=date[6:].isnumeric()
    w=date[2]==date[5]=='/'
    if len(date)==10 and x and y and z and w :
        break
ch=''
ch=date[0:2]+'-'+date[3:5]+'-'+date[6:]+'.'
print('nous somme le',ch)
    
