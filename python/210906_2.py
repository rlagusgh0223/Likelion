"""
#1
#정수 두개 입력
#첫번째 1~200, 두번째 10~200
#첫번째 입력값은 두번째 입력값보다 작다
#두 정수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력
start, stop = map(int, input().split())
i = start
while True:
    if start<1 or start>200 or stop<10 or stop>200 or start>stop:
        break
    elif i%10 != 3:
        print(i,end=' ')
    if i == stop:
        break
    i += 1

#====================모범답안=======================
start, stop = map(int, input().split())
i = start
while True:
    if i%10 == 3:
        i += 1
        continue
    if i>stop:
        break
    print(i, end=' ')
    i += 1
# i+=1을 위로 올리는 코
start, stop = map(int, input().split())
i = start-1
while True:
    i += 1
    if i%10 == 3:
        continue
    if i>stop:
        break
    print(i, end=' ')
#===================================================


#2
#이중 for문을 이용한 별 출력
for i in range(5):
    for j in range(5):
        print('*',end='')
    print()
#
#중첩 루프 사용하기
for i in range(5):
    for j in range(5):
        print('j:',j,sep='',end=' ')
    print('i:',i,'\\n',sep='')


#3
#계단식으로 별 출력하기
#조건문 사용할 것
for i in range(5):
    for j in range(5):
        if j>i:
            break
        print('*',end='')
        #if j<=i: 이렇게 짤 수도 있다
        #    print('*',end='')
    print()
#
#for loop 2개로 조건문 없이 계단식으로 출력
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()
#
#for loop를 하나만 사용하여 계단식으로 출력
for i in range(5):
    print('*'*(i+1))


#4
#이중 for문으로 대각선으로 별찍기
#아래와 같이 하면 *이 아닌 부분은 공백으로 된다
#*____
#_*___
#__*__
#___*_
#____*
for i in range(5):
    for j in range(5):
        if j==i:
            print('*',end='')
        else:
            print(' ',end='')
    print()


#5
#중첩된 for 이용하여 이등변삼각형 모양 별짓기
for i in range(1,5):
    for j in range(5-i):
        print(' ',end='')
    for j in range(2*i-1):
        print('*',end='')
    print()
#
#for문 하나만
rows = 4
for i in range(1,rows+1):
    print(' '*(rows-i) + '*'*(2*i-1))


#6
#역직각삼각형 모양으로 출력
#이중 for문과 마지막 print는 문제에서 주어진 코드
for i in range(5):
    for j in range(5):
        if j <= i-1:
            print(' ',end='')
            continue
        print('*',end='')
    print()

#====================모범답안=======================
for i in range(5):
    for j in range(5):
        if j < i:
            print(' ',end='')
        else:
            print('*',end='')
    print()
#===================================================

#7
#삼각형의 높이 입력
#입력된 높이만큼 역삼각형으로 별 출력
n = int(input())
for i in range(n,0,-1):
    for j in range(n-i):
        print(' ',end='')
    print('*'*(i*2-1),end='')
    print()
#for문 하나
n = int(input())
for i in range(n,0,-1):
    print(' '*(n-i),end='')
    print('*'*(i*2-1))

#====================모범답안=======================
nValue = int(input())
for j in range(nValue, 0, -1):
    for i in range(nValue-j):
        print(' ',end='')
    for i in range(2*(j)-1):
        print("*",end='')
    print()
#===================================================


#8
#FIZZBUZZ문제
#1에서 100까지 출력
#3의 배수는 FIZZ
#5의 배수는 Buzz
#3과 5의 공배수는 FizzBuzz출력
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
#
#한 줄로 출력
for i in range(1,101):
    print('Fizz'*(i%3==0) + 'Buzz'*(i%5==0) or i)
#Fizz나 Buzz가 없다면 i출력(단락평가)
#i%3이 0이라면 True가 되므로 Fizz가 나온다
#i%5가 0이라면 True가 되므로 Buzz가 나온다
#+니까 동시에 되면 FizzBuzz가 나온다
"""

#9
#터틀 그래픽스로 익히는 GUI 개념
#Graphic User Interpase?
