#1. word.txt.파일로부터 단어를 읽어들임
#2. 제시된 단어 5개까지 입력
#2. 리스트 단어를 썩어서, 랜덤하게 하나 제시
#2. 타이핑한 단어와 비교함
#2. 걸린시간, 맞춘개수 출력
#2. 2개이상 맞추면 합격

import pyglet
import time


sd = pyglet.resource.media('assets/good.wav', streaming=False)
sd.play()
time.sleep(2)