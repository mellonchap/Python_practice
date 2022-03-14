from random import randrange
import time


class Lotto:
    print("** 로또 추첨을 시작합니다. **\n")
    # try:
    #     iin =  input("두 수를 입력하세요.예) 1, 100 >> ")
    #     n1, n2 = iin.strip().split(',')
    # except:
    #     print("에러")
    #     exit()    
    
    num=[]
    n1=0
    n2=0
    def __init__(self):
        n1, n2 =  input("두 수를 입력하세요.예) 1, 100 >> ").split(',')
        self.n1 = int(n1)
        self.n2 = int(n2)
        self.num = []

    def getNumber(self):    
        return randrange(self.n1, self.n2)

    def getLotto(self):
        while True:
            i = self.getNumber()

            if i not in self.num:
                self.num.append(i)
            if len(self.num) == 6:
                break
        # ssd = True
        # for i in range(6):
        #     temp = self.getNumber()
        #     for j in range(i):
        #         if(self.num[j]==temp):                   
        #             ssd = False
        #             break
        #     if(ssd==True):
        #         self.num.append(temp)
        #     else:
        #         i-=1
        #         continue

    def printLotto(self):
        print("\n추첨된 로또 번호 ==> ", end="")
        for i in self.num:
            
            print( "%d " %i ,end="", flush=True)
            # time.sleep(1)
            # print( "%d " %i)
            

        

L1 = Lotto()
L2 = Lotto()

L1.getLotto()
L2.getLotto()

L1.printLotto()
L2.printLotto()



# lotto_list.sort()