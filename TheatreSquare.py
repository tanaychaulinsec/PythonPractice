n=int(input())
m=int(input())
a=int(input())
s=n*m
b=a*a
if s%b==0 :
    l=s//b
    print(l)
else :
    r=n//a +1
    r2=m//a+1
    print(r+r2)


