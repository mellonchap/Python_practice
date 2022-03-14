from random import randrange

n1, n2 =  input("두 수를 입력하세요.예) 1, 100 >> ").split(',')
n1 = int(n1)
n2 = int(n2)
lnum=[]
def getNumber():    
    return randrange(n1, n2)

    
def getLotto():
    # for i in range(6):
    #     temp = getNumber()
    #     for j in range(i):
    #         if(num[j]==temp):
    #             i-=1
    #             break
    #     num.append(temp)
    while True:
        num = getNumber()

        if num not in lnum:
            lnum.append(num)
        if len(lnum) == 6:
            break
        

def printLotto():
    for i in lnum:
        print( "%d " %i ,end="")

getLotto()
printLotto()