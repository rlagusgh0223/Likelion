#1
#파이썬에서 난수를 생성하려면 random모듈이 필요
#random모듈의 난수 : 0.0 <= random.random() < 1.0
import random
for i in range(10):
    print(random.random())

#
#random모듈의 위치 확인
import random
import inspect
print(inspect.getfile(random))

#
#while 이용해서 난수 10번 출력
import random
i = 0
while i<10:
    print(random.random())
    i += 1


#2
#1~6까지의 랜덤 숫자를 구하기
import random
for i in range(10):
    print(int((random.random()*10)%6)+1)


#3
#randint함수
#a <= random.randint(a,b) <= b
import random
i = 0
while i<10:
    print(random.randint(1,6))
    i += 1


#4
#난수의 개수 count
#6개의 요소를 가지는 리스트 만들기
#   cut_rand = [0,0,0,0,0,0]
#발생된 수는 1~6이므로 index를 0~5로 변경
#발생된 난수는 리스트의 인덱스
#=======정리하자면=======
#반복하면서 1~6까지 숫자가 나온다
#그 숫자를 cut_rand에 카운트할것
#ex)1이 나오면 cut_rand[0]에1을 더한다
import random
cut_rand = [0,0,0,0,0,0]
i=0
while i<1000:
    nrand = random.randint(1,6)
    cut_rand[nrand-1] += 1
    i += 1
print(cut_rand)


#5
#1 ~ 6 사이의 난수를 발생시켜 3이 나오면 종료하도록
#while의 조건문 사용할것(break사용하지 말고)
import random
cut_rand = [0,0,0,0,0,0]
while cut_rand[2]<1:
    nrand = random.randint(1,6)
    cut_rand[nrand-1] += 1
print(cut_rand)
#=================모범답안===================
import random
i = 0
while i != 3:
    i = random.randint(1,6)
    print(i)
#============================================


#6
#random예제
#컴퓨터가 1부터 30까지의 임의의 숫자를 정하기
#사용자가 숫자를 입력하면 수보다 큰지 작은지를 표시
#미리 정한 숫자를 맞히면 '정답입니다' 표시 후 종료
import random
i = random.randint(1,30)
n = int(input("숫자를 맞혀보세요 : "))
while n != i:
    if n>i :
        print("너무 큽니다")
    else:
        print("너무 작습니다")
    n = int(input("숫자를 맞혀보세요 : "))
print("정답입니다")

#====================모범답안=====================
import random
g = 0
n = random.randint(1,30)
while n != g:
    x = input("숫자를 맞혀 보세요?")
    g = int(x)
    if g == n:
        print("정답입니다")
    elif g < n:
        print("너무 작습니다")
    elif g > n:
        print("너무 큽니다")
#=================================================


#7
#while에 조건식은 두 개 지정
#두 변수를 모두 변화시킬것
#출력결과
#2 5
#4 4
#8 3
#16 2
#32 1
i = 2
j = 5
while i<64 or j>0:
    print(i,j)
    i *= 2
    j -= 1
#====================모범답안=====================
i = 2
j = 5
while i<=32 or j>=1:
    print(i,j)
    i *= 2
    j -= 1
#=================================================


#8
#금액 입력(정수)
#1회당 요금은 1350원
#교통카드를 사용할 때마다 잔액 표시
#최초 금액은 출력하지 않는다
#잔액은 음수가 될 수 없으며, 잔액이 부족하면 출력 끝
nmoney = int(input("금액을 입력하세요 : "))
nmoney -= 1350
while nmoney >= 0:
    print(nmoney)
    nmoney -= 1350
#====================모범답안=====================
nmoney = int(input("금액을 입력하세요 : "))
while nmoney >= 1350:
    nmoney -= 1350
    print(nmoney)
#=================================================


#9
#break로 반복문 종료
#0~100까지 총합 구하기
i = 0
n = 0
while True:
    if i == 100:
        break
    else:
        i += 1
        n += i
print(n)
#====================모범답안=====================
i = 0
n = 0
while True:
    i += 1
    n += i
    if i == 100:
        break
print(n)
#=================================================


#10
#for문 사용해서 0~100까지 합 구하기
#range(10000)
total = 0
for i in range(10000):
    total += i
    if i == 100:
        break
print(total)


#11
#continue로 코드 실행 건너뛰기
#for에서
for i in range(100):
    if i%2 == 0:
        continue
    print(i)
#while에서
i = 0
while i<100:
    i += 1
    if i % 2 == 0:
        continue


#12
#입력한 횟수대로 반복
#while문
count = int(input("반복할 횟수 : "))
i = 0
while True:
    print(i)    #입력한 숫자는 나오지 않는다
    i += 1
    if i == count:
        break

#for문
count = int(input("반복 횟수 : "))
for i in range(10000):
    print(i)    #while과는 다르게 입력한 숫자도 나온다
    if i == count:
        break


#13
#입력한 숫자까지 해당하는 홀수 출력
nData = int(input("정수 입력 : "))
for i in range(nData+1):
    if i%2 == 0:
        continue
    print(i)


#14
#0과 73 사이의 숫자 중 3으로 끝나는 숫자만 출력
i = 0
while True:
    if i%10 != 3:
        i += 1
        continue
    if i>73:
        break
    print(i, end=' ')
    i += 1
