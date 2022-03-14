class Car:
    color=""
    speed=0

    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2

    def upSpeed(self, value):
        self.speed+=value

    def downSpeed(self, value):
        self.speed-=value

    def getColor(self):
        return self.color

    def getSpeed(self):
        return self.speed

# myCar1 = Car()
# myCar1.color = "빨강"
# myCar1.speed = 0
# myCar2 = Car()
# myCar2.color = "파랑"
# myCar2.speed = 0
# myCar3 = Car()
# myCar3.color = "노랑"
# myCar3.speed = 0

myCar1 = Car("빨강", 30)
myCar2 = Car("파랑", 60)
myCar3 = Car("노랑", 90)

myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." %(myCar1.color, myCar1.getSpeed()))
myCar2.upSpeed(60)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." %(myCar2.color, myCar2.speed))
myCar3.upSpeed(30)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." %(myCar3.color, myCar3.speed))