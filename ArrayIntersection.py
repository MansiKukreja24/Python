n1 = int(input())
s1 = input()
a = list(s1.split())
n2 = int(input())
s2 = input()
b = list(s2.split())
c = 0
for i in a:
    if i in b:
        c = 1
        print(i)
if (c == 0):
    print("-1");
