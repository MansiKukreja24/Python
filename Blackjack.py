def blackjack(a,b,c):
    s=sum((a,b,c))
    if(s<=21):
        return s
    elif(s>21 and 11 in(a,b,c)):
        return s-10
    else:
        return "BUST"

print(blackjack(10,20,30))

