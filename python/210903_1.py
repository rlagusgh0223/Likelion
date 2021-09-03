#if 조건문 예제 13
#1
#딕셔너리 이용해서 계산기 만들기
#+, -, *, / 사칙연산만 처리
#잘못된 연산자, 0으로 나누기 예외 처리
nData1 = int(input("첫번째 숫자 : "))
nData2 = int(input("두번째 숫자 : "))
cCal = input("연산자 : ")
sCal = {"+":nData1+nData2, "-":nData1-nData2, "*":nData1*nData2, "/":nData1/nData2}

if cCal not in sCal:
    print("잘못된 연산자")
elif nData2 == 0 and cCal == '/':       #지금 코드로는 이거 에러난다. 이미 sCal에서 계산을 한 후이기 때문에
    print("0으로 나눌 수 없습니다.")
else:
    print("정답:",sCal[cCal])
#=========================================
#이렇게 해야 에러 안난다
nData1 = int(input("첫번째 숫자 : "))
nData2 = int(input("두번째 숫자 : "))
cCal = input("연산자 : ")
if nData2 == 0 and cCal == '/':
    print("0으로 나눌 수 없습니다.")
else:
    sCal = {"+":nData1+nData2, "-":nData1-nData2, "*":nData1*nData2, "/":nData1/nData2}
    if cCal not in sCal:
        print("잘못된 연산자")
    else:
        print("정답:",sCal[cCal])


#2
#과일 사과 150, 귤 30원
#사과와 귤의 수를 입력하여 총액계싼
#사과는 10개 넘어가면 10프로 할인
fru = input("사고 싶은 과일 : ")
n = int(input("개수 : "))
if fru == '사과':
    if n >=10 :
        money = int((150*n)*0.9)
    else:
        money = 150*n
    print("총액 :", money)
elif fru =='귤':
    print("총액 :",30*n)
else:
    print("잘못된 입력")
#============모범답안==============
apple = 150
orange = 30
a_c = int(input("사과의 개수 : "))
o_c = int(input("귤의 개수 : "))
if a_c<10:
    x = apple*a_c + orange*o_c
else:
    x = int((apple*a_c*0.9)+(orange*o_c))
print()
print("가격은",x,"원")
#===================================


#3
#사과 5개, 귤 3개 이상이면 30프로 할인
apple = 150
orange = 30
a_c = int(input("사과 : "))
o_c = int(input("귤 : "))
if a_c >=5 and o_c >=3 :
    x = int((apple*a_c + orange*o_c) * 0.7)
else:
    x = apple*a_c + orange*o_c
print("총액 :",x,'원')


#4
#if 조건문 예제 끝
#윤년 계산하기
#2월 29일이 있는 해는 매년 4년 마다 반복
#윤달의 조건
#1. 연도가 4로 나누어 떨어지는 경우, 윤달이 있음
#2. 단, 연도가 100으로 나누어 떨어지는 경우, 윤달이 없음
#3. 단, 연도가 400으로 나누어 떨어지는 경우, 윤달이 잇음
#연도를 입력 받아 윤달이 있는지 없는지
nyear = int(input("연도 : "))
if nyear % 4 == 0:
    if nyear % 100 == 0:
        if nyear % 400 == 0:
            print("윤달이 있습니다")
        else:
            print("윤달이 없습니다")
    else:
        print("윤달이 있습니다")
else:
    print("윤달이 없습니다.")
#==========================모범답안===========================
nyear = int(input("연도 : "))
if nyear%4 != 0:
    print("평년입니다")
else:
    if nyear%400 == 0:
        print("윤년")
    elif nyear%100 == 0:
        print("평년")
    else:
        print("윤년")
#다른 코드
nyear = int(input("연도 : "))
if nyear %4 == 0 and (nyear % 100 != 0 or nyear %400 == 0):
    print("윤년")
else:
    print("평년")
#=============================================================


#5
for i in reversed(range(10)):   #reversed를 사용하면 거꾸로 계산해준다
    print("Hello, world!",i)


#6
#숫자를 입력 받아 표시
start = int(input("시작 숫자 : "))
end = int(input("끝 숫자 : "))
interval = int(input("간격 : "))
for i in range(start, end+1, interval):
    print(i)


#7
#증가 또는 감소되는 경우를 모두 표현할 수 잇는 코드 작성
#시작 / 끝 / 증가폭이 형식에 맞지 않는 경우 안내 메시지 후 종료
n1 = int(input("시작 숫자 : "))
n2 = int(input("끝 숫자 : "))
interval = int(input("간격 : "))
if interval>=0:
    if n2>=n1:
        for i in range(n1, n2+1, interval):
            print(i)
    else:
        print("입력된 내용이 부적절")
else:
    if n1>=n2:
        for i in range(n1, n2-1, interval):
            print(i)
    else:
        print("입력된 내용이 적절하지 않습니다")
        
#=====================모범답안=======================
start = int(input("시작 숫자 : "))
end = int(input("끝 숫자 : "))
interval = int(input("간격 : "))
if start>end and interval<0:
    for i in range(start,end-1,interval):
        print(i)
elif start<end and interval>0:
    for i in range(start,end+1,interval):
        print(i)
else:
    print("입력된 내용이 적절하지 않습니다.")
#====================================================


#8
#range대신 시퀀스 객체를 넣어도 됨
#for는 리스트, 튜플, 문자열 등 시퀀스 객체로 반복할 수 있음
#리스트
a = [10,20,30,40,50]
for i in a:
    print(i)
    
#튜플
fruits = ("apple","orange","grape")
for fruit in fruits:
    print(fruit)
    
#문자열
for letter in 'Python':
    print(letter, end=' ')
print()
for i in "LikeLion":
    print(i, end='')
    
#reversed()는 리스트, 튜플, 문자열에서도 쓸 수 있다
for letter in reversed("Python"):
    print(letter, end=' ')        #n o h t y P


#9
#디버깅 해보기
#pdb 모듈은 파이썬 프로그램을 위한 대화형 소스 코드 디버거
#소스 라인 단계의 중단점 및 단계 실행 설정,
#스택 프레임 검사, 소스 코드 목록, 그리고 모든 스택 프레임의 컨텍스트에서
#임의의 파이썬 코드 평가를 지원
import pdb
pdb.set_trace() #이곳에서 프로그램 중단
total = 0
number = int(input("숫자를 입력하세요 : "))
for i in range(number+1):
    total = total + i
print(total)
#next이전으로 돌아가는 코드는?
