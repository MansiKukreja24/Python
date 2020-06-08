def count_primes(num):
    prime=[2]
    x=3
    if num<2:
        return 0
    while x<=num:
        for y in prime:
            if(x%y==0):
                x=x+2
                break
        else:
            prime.append(x)
            x=x+2
    print(prime)
    return len(prime)
num=int(input())
print((count_primes(num)))
