x=input('entrer un mots')
ch=''
for i in range (1,len(x)) :
    ch+=x[i]
    print(ch)
ch=ch+x[0]+'us'
print(ch)
