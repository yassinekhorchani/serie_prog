x=int(input('entrer le nombre des photocopies'))
y=0
for i in range (x) :
    if i<10 :
        y+=0.10
    elif 10<=i<30 :
        y+=0.07
    else :
        y+=0.05
print('le prix total est : ',y) 
