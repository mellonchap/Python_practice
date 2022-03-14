import random
import pyglet
import time
def file_read():
    try:
        f = open("data/word.txt", "r")
    except:
        print("파일이 없습니다.")
        exit()
    temp = f.read().split('\n')
    f.close()
    return temp

def ques(a):
    p=0
    start = time.time()
    for i in range(5):
        random.shuffle(a)
        print("*Question # {}".format(i+1))
        # qs =temp[random.randrange(0,len(a))]
        qs =random.choice(a)
        print(qs)
        ans = input()
        if(qs==ans):
            p+=1
            sd = pyglet.resource.media('assets/good.wav', streaming=False)
            sd.play()
            time.sleep(1)
            print()
        else:
            sd = pyglet.resource.media('assets/bad.wav', streaming=False)
            sd.play()
            time.sleep(1)
            print()    
    end = time.time()
    gametime = end-start
    return p, gametime



def result(p, gametime ):
    if(p>=3):
        print("Pass!")
        print("결과 : 합격")
    else:
        print("nonPass!")
        print("결과 : 불합격")
    # gametime = format((end-start), ".4f")
    # print("게임 시간 : {:.4f} 초 정답 개수 : {}".format(end-start, p))
    print("게임 시간 : {} 초 정답 개수 : {}".format(gametime, p))

words =file_read()
print(words)
p, gametime = ques(words)
result(p, gametime)