from random import randrange
import time
num=[]

class Lotto:
    print("** 로또 추첨을 시작합니다. **\n")
    # try:
    #     iin =  input("두 수를 입력하세요.예) 1, 100 >> ")
    #     n1, n2 = iin.strip().split(',')
    # except:
    #     print("에러")
    #     exit()
    n1, n2 =  input("두 수를 입력하세요.예) 1, 100 >> ").split(',')
    n1 = int(n1)
    n2 = int(n2)
    def getNumber(self):    
        return randrange(self.n1, self.n2)

    def getLotto(self):
        # while True:
        #     num = getNumber(n1, n2)

        #     if num not in looto_list:
        #         lotto_list.append(num)
        #     if len(lotto_list) == 6:
        #         break
        ssd = True
        for i in range(6):
            temp = self.getNumber()
            for j in range(i):
                if(num[j]==temp):                   
                    ssd = False
                    break
            if(ssd==True):
                num.append(temp)
            else:
                i-=1
                continue
            
def printLotto():
    print("\n추첨된 로또 번호 ==> ", end="")
    for i in num:
        
        print( "%d " %i ,end="", flush=True)
        time.sleep(1)
        # print( "%d " %i)
        

L1 = Lotto()
L1.getLotto()
printLotto()



# lotto_list.sort()