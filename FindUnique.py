n = int(input())
s = input()
elist = list(s.split(" "))
for i in range(0, n):
    c = 0
    for j in range(0, n):
        if (elist[i] == elist[j]):
            c = c + 1
    if (c == 1):
        print(elist[i])
