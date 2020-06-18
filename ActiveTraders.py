from collections import Counter

n =int(input())
customers=[]
for i in range(n):
    a=input()
    customers.append(a)

c=Counter(customers)
l=([(i,c[i]/n*100) for i in c])

print(l)
traders = []
for i in l:
    key = i[0]
    value= i[1]
    if(value>=5):
        traders.append((key))

print(traders)
















