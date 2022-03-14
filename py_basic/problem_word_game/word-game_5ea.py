#1. word.txt.파일로부터 단어를 읽어들임
#2. 제시된 단어 5개까지 입력
#2. 리스트 단어를 적어서, 랜덤하게 하나 제시
#2. 타이핑한 단어와 비교함
#2. 걸린시간, 맞춘개수 출력
#2. 2개이상 맞추면 합격

import random
import pyglet
import time

f = open("data/word.txt", "r")
temp = f.read().split('\n')
f.close()
print(temp)
p = 0
start = time.time()

for i in range(5):
    random.shuffle(temp)
    print("*Question # {}".format(i+1))
    # qs =temp[random.randrange(0,len(temp))]
    qs =random.choice(temp)
    print(qs)
    ans = input()
    if(qs==ans):
        p+=1
        sd = pyglet.resource.media('assets/good.wav', streaming=False)
        sd.play()
        time.sleep(1)
    else:
        sd = pyglet.resource.media('assets/bad.wav', streaming=False)
        sd.play()
        time.sleep(1)
    print()
end = time.time()

if(p>=3):
    print("Pass!")
    print("결과 : 합격")
else:
    print("nonPass!")
    print("결과 : 불합격")

gametime = format((end-start), ".4f")
# print("게임 시간 : {:.4f} 초 정답 개수 : {}".format(end-start, p))
print("게임 시간 : {} 초 정답 개수 : {}".format(gametime, p))
