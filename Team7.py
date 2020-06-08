n=int(input())
count=0
for i in range(0,n):
    x,y,z=input().split()
    c=0
    a=int(x)
    b=int(y)
    d=int(z)
    if(a==1):
        c=c+1
    if(b==1):
        c=c+1
    if(d==1):
        c=c+1
    if(c>=2):
        count=count+1
print(count)