while True :
    n=int(input('entrer un entier de 4 chiffre'))
    if 999>n or 9999<n :
        print(n,"n'est pas former de 4 chiffre")
    else:
        break
a=n//1000
b=n%1000//100
c=n%100//10
d=n%10
if b%a==0 and b%a==0 and c%a==0 and d%a==0 :
    print(n,' est valable')
else :
    print(n,"n'est pas valable")
