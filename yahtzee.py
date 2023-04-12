def handToDice(hand): #works
    first= hand//100
    second= hand//10%10
    third= hand%10
    return first, second, third

def diceToOrderedHand(a, b, c):
    d=max(a,b,c)
    f=min(a,b,c)
    middle=(a+b+c)-(d+f)
    return (d*100)+ (middle*10)+ f

def playStep2(hand, dice):
    a,b,c=handToDice(hand)
    if a!=b or a!=c:
        if a==b:
            c=dice%10
            dice//=10
        elif a==c:
            b=dice%10
            dice//=10
        elif b==c:
            a=dice%10
            dice//=10
        else:
            a=max(a,b,c)
            b=dice%10
            dice//=10
            c=dice%10
            dice//=10
    hand=diceToOrderedHand(a,b,c)
    return (hand,dice)
    

def score(hand):
    a,b,c=handToDice(hand)
    if a==b==c:
        score=20+a+b+c
        return score
    if (a==b and a!=c):
        score=10+a+b
        return score
    if (b==c and b!=a):
        score=10+b+c
        return score
    if (a==c and a!=b):
        score=10+a+c
        return score
    else:
        score=max(a,b,c)
        return score

def playThreeDiceYahtzee(dice):
    first=dice//100
    second=dice//10%10
    third=dice%10
    thing=first%10
    dice=(dice-(thing*100)-(second*10)-(third))//1000
    hand=(thing*100)+(second*10)+(third)
    hand, dice = playStep2(hand,dice)
    hand, dice = playStep2(hand,dice)
    return hand, score(hand)
