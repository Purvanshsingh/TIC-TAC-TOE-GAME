import itertools
winning_positions=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
x=[]
o=[]
def pattern(n,k):
    C=1
    j=0
    print('-'*19)
    if(k=='X'):
        x.append(n)
    if(k=='O'):
        o.append(n)
    for i in range(3):
        while j<3:
            if (C<=9):
                if C in x:
                    print("| ",'X'," ",end='')
                    C=C+1
                    j=j+1
                elif C in o:
                    print("| ",'O'," ",end='')
                    C=C+1
                    j=j+1
                    
                else:
                    print("| ",C," ",end='')
                    C=C+1
                    j=j+1
        j=0
        print("|")
    print('-'*19)
def check():
    x1=sorted(x)
    o1=sorted(o)
    combinationsO=itertools.combinations(o1,3)
    combinations=itertools.combinations(x1,3)
    for i in combinations:
        if list(i) in winning_positions:
            print("Player 1 is Winner")
            return True
    for i in combinationsO:
        if list(i) in winning_positions:
            print("Player 2 is Winner")
            return True
    if len(x1)>=5 or len(o1)>=5:
        print("Match Draw")
        return True
while True:
    C=1
    print('-'*19)
    for i in range(3):
        for j in range(3):
            print("| ",C," ",end='')
            C=C+1
        print("|")
    print('-'*19)
    while True:
        print("Enter the position where to Place 'X'")
        pos=int(input())
        pattern(pos,'X')
        if check():
            break
        print("Enter the position where to Place 'O'")
        pos=(int(input()))
        pattern(pos,'O')
        if check():
            break
    ch=input("Do you Want to play again press y else press n")
    if ch in 'nN':
        break
    x.clear()
    o.clear()
