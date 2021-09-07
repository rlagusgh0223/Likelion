#1
#2중 for문을 이용하여 4각형 4개 만들기
#끝위치 != 시작위치
import turtle as t
t.shape('turtle')
t.left(90)
for i in range(4):
    for j in range(4):
        t.forward(100)
        t.left(90)
    t.right(90)
    if i==3:
        continue
    t.up()
    t.forward(100)
    t.down()
#
#끝 위치 == 시작위치
import turtle as t
t.shape('turtle')
t.left(90)
for i in range(4):
    for j in range(4):
        t.forward(100)
        t.left(90)
    t.right(90)
    t.up()
    t.forward(100)
    t.down()
#
#사각형 4개 그리기
#goto를 이용해서 다음 사각형 시작 좌표 이동
import turtle as t
t.shape('turtle')
t.left(90)          #시작점을 처음 사각형중 우측 아래로 잡았으므로 위로 올라가게 하기 위해
for i in range(4):  #처음 사각형 작성
    t.forward(100)
    t.left(90)
t.forward(100)      #문제에서 제시한 다음 사각형으로 이동위치로 가기 위해

t.up()
t.goto(100,100)     #두번째 사각형은 시작점을 기준으로 위(100), 오른쪽(100)에 있다
t.down()

for i in range(4):  #사각형을 만들기 이동위치로 돌아오게 만듬
    t.right(90)
    t.forward(100)

t.up()
t.goto(200,-100)    #시작점을 기준으로 세번째 사각형의 시작위치로 옮김
t.down()

for i in range(4):  #왼쪽으로 이동해야 별 다른 이동없이 다음 위치로 이동하기 위한 곳으로 옮길 수 있다
    t.left(90)
    t.forward(100)

t.up()
t.goto(0,-200)      #시작점을 기준으로 네번째 사각형의 시작위치로 옮김
t.down()

for i in range(4):  #위치에 맞게 사각형 만들기
    t.forward(100)
    t.left(90)
#???
import turtle as t
t.shape('turtle')
cnt=0
for i in range(4):
    for j in range(4):
        t.forward(100)
        t.rt(90)
        cnt += 1
    t.up()
    if cnt==1:
        t.goto(200,0)
    elif cnt=2:
        t.goto(300,-200)
    elif cnt=3:
        t.goto(100,-300)
    t.down()


#2
#사각형 색깔 입히기
#reset() : 초기화
#pensize(width) : 펜의 굵기
#pencolor(color) : 펜 색깔
#filecolor(color) : 그림 채우는 색 - begin_fill / end_fill 써야된다
#color(red,green,blue) : 각각 FF까지 쓸 수 있다
#t.pencolor("#00fffee")

import turtle as t
t.shape('turtle')

t.pencolor('#dcdcdc')   #펜 색깔 지정(선의 색깔)
for i in range(4):
    t.lt(90)
    t.forward(100)
t.up()
t.forward(100)
t.down()

t.pencolor("#ff0000")
for i in range(4):
    t.forward(100)
    t.lt(90)
t.rt(90)
t.up()
t.forward(100)
t.down()

t.pencolor("#0000ff")
for i in range(4):
    t.forward(100)
    t.lt(90)
t.rt(90)
t.up()
t.forward(100)
t.down()

t.pensize(5)            #펜 두께 지정
t.pencolor("#00ff00")
for i in range(4):
    t.forward(100)
    t.lt(90)

#사각형 색 채우기
import turtle as t
t.shape('turtle')

t.pencolor('#dcdcdc')   #펜 색깔 지정(선의 색깔)
t.fillcolor('red')      #사각형 안의 색 지정
t.begin_fill()          #색 지정 시작
for i in range(4):
    t.lt(90)
    t.forward(100)
t.end_fill()            #색 지정 끝
t.up()
t.forward(100)
t.down()

t.pencolor("#ff0000")
t.fillcolor("BLUE")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.lt(90)
t.end_fill()
t.rt(90)
t.up()
t.forward(100)
t.down()

t.pencolor("#0000ff")
t.fillcolor('green')
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.lt(90)
t.end_fill()
t.rt(90)
t.up()
t.forward(100)
t.down()

t.pensize(5)            #펜 두께 지정
t.pencolor("#00ff00")
for i in range(4):
    t.forward(100)
    t.lt(90)


#3
#다각형 그리기
#turtle.circle(r,ext,step)
#r:반지름
#ext:이동할 길이
#step:원 반경내 몇번 만큼의 다각형 ex)3이면 삼각형

import turtle as t
t.pensize(3)

start = -300                    #시작위치 지정시 X좌표 초기값
for i in range(5):
    start += 100                #X좌표는 -200,-100,0,100,200이니까 100씩 더해줌
    t.penup()           #up()과 동일
    t.goto(start,-50)           #Y좌표는 고정, X좌표는 변경된 값 입력
    t.pendown()         #down()과 동일
    if i==4:                    #마지막 도형(원)의 경우는 stps가 없어야 한다
        t.circle(40)
        continue
    t.circle(40,steps = i+3)    #4번째 도형까지는 steps가 하나씩 증가한다
#
#start 초기값 지정하지 않고 만들어보기 
import turtle as t
t.pensize(3)

for i in range(3,8):
    start = i*100-500   #i는 3,4,5,6,7이니까 100씩 곱해서 500을 빼면 -200,-100,0,100,200이 된다
                        #start라는 변수 없이 식만 goto좌표에 넣어도 된다
    t.up()
    t.goto(start,-50)
    t.down()
    if i==7:         
        t.circle(40)
        continue
    t.circle(40,steps = i)


#4
#cicle 사용하지 않고 다각형 만들기
#오각형
import turtle as t
t.shape('turtle')
for i in range(5):
    t.forward(100)
    t.right(360/5)
#
#정다각형인 n각형
import turtle as t
n = int(input())
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right(360/n)


#5
#키보드 입력 받아 쉘에 표시하기
#import keyboard는 cmd창에서 pip install keyboard한 다음에 쓸 수 있다
import keyboard
import time
while True:         #while 안쓰면 화면에 뜨지 않는다
    time.sleep(0.1)     #너무 빨라서 지연시켰다
    if keyboard.is_pressed('left'):
        print('left')
    elif keyboard.is_pressed('right'):
        print('right')
    elif keyboard.is_pressed('up'):
        print('up')
    elif keyboard.is_pressed('down'):
        print('down')
    elif keyboard.is_pressed('a'):
        print('quit')
        quit()    #화면 종료
        break
#
#거북이를 키보드로 움직여보기
import turtle as t
t.shapesize(1,1,1)
t.shape('turtle')
t.pensize(3)

pos_angle=0
pos_pos=0

import keyboard
while True:
    if keyboard.is_pressed('left'):
        pos_angle += 1     #좌/우 좌표 하나씩 증가
        t.lt(pos_angle)
        print('left')
    elif keyboard.is_pressed('right'):
        pos_angle += 1
        t.rt(pos_angle)
        print('right')
    elif keyboard.is_pressed('up'):
        pos_pos += 1      #앞/뒤 좌표 하나씩 증가
        t.forward(pos_pos)
        print('up')
    elif keyboard.is_pressed('down'):
        pos_pos += 1
        t.backward(pos_pos)
        print('down')
    elif keyboard.is_pressed('a'):
        print('quit')   #콘솔종료
        t.bye()     #turtle종료
        break


#6
#원을 반복해서 그리기
import turtle as t
n = 60                  #60번을 그림
t.shape('turtle')
t.speed('fastest')      #거북이 속도를 가장 빠르게
for i in range(n):
    t.circle(120)       #반지름이 120인 원을 그림
    t.right(360/n)      #오른쪽으로 6도 회전

#선으로 복잡한 무늬 그리기
import turtle as t
t.shape('turtle')
t.speed('fastest')
for i in range(300):
    t.forward(i)        #i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
    t.right(91)         #오른쪽으로 91도 회전








