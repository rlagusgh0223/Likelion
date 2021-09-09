import turtle as t
import random
import math

#전역변수 선언
t1, t2, t3 = [None]*3   #3개의 객체는 만들지만 객체 타입은 만들지 않는다
                        #if에서 만드는걸 받기 위해
t1X, t1Y, t2X, t2Y, t3X, t3Y = [0]*6
swidth, sheight = 300, 300

if __name__ == "__main__":
    t.title('거북이 만나기')
    t.setup(width = swidth + 50, height = sheight+50)  #창 크기
    t.screensize(swidth,sheight)   #거북이 활동범위

    t1 = t.Turtle('turtle'); t1.color('red'); t1.speed(10); t1.penup()
    t2 = t.Turtle('turtle'); t2.color('green'); t2.speed(10); t2.penup()
    t3 = t.Turtle('turtle'); t3.color('blue'); t3.speed(10); t3.penup()
    #;을 쓰면 여러 코드를 한 줄에 쓸 수 있다

    t1.goto(-100,100); t2.goto(0,0); t3.goto(100,100)

    while True:
        angle = random.randrange(0,360)
        dist = random.randrange(1,50)
        t1.left(angle)
        t1.forward(dist)

        angle = random.randrange(0,360)
        dist = random.randrange(1,50)
        t2.left(angle)
        t2.forward(dist)

        angle = random.randrange(0,360)
        dist = random.randrange(1,50)
        t3.left(angle)
        t3.forward(dist)

        t1X = t1.xcor(); t1Y = t1.ycor()
        t2X = t2.xcor(); t2Y = t2.ycor()
        t3X = t3.xcor(); t3Y = t3.ycor()

        #각 거북이가 화면 밖으로 나가면 각자의 처음 위치로 이동
        if not((-swidth/2 <= t1X <= swidth/2) and (-sheight/2 <= t1Y <= sheight/2)):
            t1.goto(-100,100)
        if not((-swidth/2 <= t2X <= swidth/2) and (-sheight/2 <= t2Y <= sheight/2)):
            t2.goto(-100,100)
        if not((-swidth/2 <= t3X <= swidth/2) and (-sheight/2 <= t3Y <= sheight/2)):
            t3.goto(-100,100)

        #만났을때 도장
        #피타고라스 정리 의거 상대방과의 거리가 20이하(거북이 하나 넓이)일때
        if math.sqrt(((t1X-t2X) * (t1X-t2X)) + ((t1Y-t2Y) * (t1Y-t2Y))) <= 20:
            t1.stamp(); t2.stamp()
        elif math.sqrt(((t1X-t3X) * (t1X-t3X)) + ((t1Y-t3Y) * (t1Y-t3Y))) <= 20:
            t1.stamp(); t3.stamp()
        elif math.sqrt(((t2X-t3X) * (t2X-t3X)) + ((t2Y-t3Y) * (t2Y-t3Y))) <= 20:
            t2.stamp(); t3.stamp()
