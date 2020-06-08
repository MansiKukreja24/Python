s=input();
c=list(s.split())
min=c[0];
n=len(c);
for i in range(0,n):
    if(len(min)>len(c[i])):
        min=c[i]
print(min)
