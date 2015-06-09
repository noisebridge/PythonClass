"""Choose 3 colors at random from the six color options - 
"red","blue","green","purple","yellow","orange"
"""

import random
myColors=(["red","blue","green","purple","yellow","orange"])
a=random.choice(myColors)
b=random.choice(myColors)
c=random.choice(myColors)
d=random.choice(myColors)
line=[a,b,c,d]
D=dict()
for color in line:
    if color not in D:
        D[color]=1
    else:
        D[color] +=1


guess=[0]*4
C=dict()
def guess_colors():
    w=input("Enter a color")
    x=input("Enter a second color")
    y=input("Enter a third color")
    z=input("Enter a fourth color")
        
    guess[0]=w
    guess[1]=x
    guess[2]=y
    guess[3]=z

    for color in guess:
        if color not in C:
            C[color]=1
        else:
            C[color] +=1
        
    return(w,x,y,z)


def cf_colors(A):

    results=0
    for i,j in zip(guess,line):
        q=D.get(i)
        r=C.get(i)
        if i==j:
            results+=1
            print("Black", None)
        elif i not in line:
            print("Wrong", None)
        else:
            if r<=q:
                print("White", None)
            else:
                print("Wrong", None)
    return (results)


B=0
n=10
for i in range (n):
    print("You have "+str(n-i) +" guesses left")
    if B<4:
        A=guess_colors()
        B=cf_colors(A)
        C.clear()
    elif B==4:
        print("You win - you don't need them")
        break