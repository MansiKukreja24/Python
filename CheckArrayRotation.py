n=int(input())
a=input()
arr=list(a.split())
t=len(arr)
r=arr.copy()
r.sort()
b=int(r[0])
for i in range(0,t):
    c=int(arr[i])
    if(c==b):
        print(i)
        break