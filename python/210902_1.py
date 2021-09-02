#1
n = int(input())                #1개의 값을 받아들임
if n == 10:                     #받아들인 값이 10이면 '10입니다.'
    print("10입니다.")
else:                           #아니면 '10이 아닙니다'라고 출력
    print("10이 아닙니다.")


#2
#if와 else 동작해보기
if True:
    print("참")      #True는 참
else:
    print("거짓")
 
if False:
    print("참")
else:
    print("거짓")     #False는 거짓

if None:
    print("참")
else:
    print("거짓")     #None은 거짓


#3
#숫자는 0이면 거짓, 0이 아니면 참
if 0:
    print("참")
else:
    print("거짓")     #0은 거짓
    
if 1:
    print("참")          #1은 참
else:
    print("거짓")
    
if 0x1F:
    print("참")          #16진수 0x1F는 참
else:
    print("거짓")
    
if 0b1000:
    print("참")          #2진수 0b1000은 참
else:
    print("거짓")
    
if 13.5:
    print("참")          #실수 13.5는 참
else:
    print("거짓")


#4
#문자열은 내용이 있으면 참, 없으면 거짓
if 'Hello':
    print("참")      #문자열은 참
else:
    print("거짓")

if '':
    print("참")
else:
    print("거짓")     #빈 문자열은 거짓(공백도 없어야 된다)


#5
#조건식을 여러개 지정하기(if, else)
x = 10
y = 25
#y = 20
#if x == 10 and y == 20:
if x == 10 or y == 20:
    print("참")
else:
    print("거짓")


#6
#입사 시험은 필기 시험 점수가 80점 이상이면서
#코딩시험을 통과해야 합격(통과여부는 True,False로 구분)
#합격, 불합격이 되게 출력
#
#에제에서는 아래와 같이 점수와 합격이 주어졌으나 코드 새롭게 만들었음
#written_test = 75
#coding_test = 'True'
written_test = int(input('필기시험 점수는? : '))
coding_test = input("코딩시험 합격?불합격? : ")
if written_test >= 80 and coding_test == 'True':
    print("합격")
else:
    print("불합격")


#7
#국어 시험 점수가 90점 이상이면서
#영어 시험 점수가 70점 이상이면 시험 통과
#합격, 불합격 출력
Kor_test = 75
Eng_test = 75
if Kor_test >= 90 and Eng_test >= 70:
    print("합격")
else:
    print("불합격")


#8
#국어, 영어, 수학, 과학 점수 입력
#네 과목의 평균 점수가 80점 이상일때 합격
#합격, 불합격 출력
#단, 점수는 0점부터 100점까지만 입력받을 수 있다
#범위를 벗어났다면 '잘못된 점수'를 출력
nkor, neng, nmat, nsci = map(int,input("국어, 영어, 수학, 과학 : ").split())
    #input().split()은 리스트로 받기때문에 int를 이용해서 바로 입력할 수 없다
    #값이 하나만 입력된다고 해도 그 값은 리스트다
if 0<=nkor<=100 and 0<=neng<=100 and 0<=nmat<=100 and 0<=nsci<=100:
    if (nkor+neng+nmat+nsci)/4 >=80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 점수")


#9
#조건식을 여러개 지정하기(if, elif, else)
x = 30
if x == 10:
    print("10입니다.")
elif x == 20:
    print('20입니다.')
else:
    print('10도 20도 아닙니다.')


#10
#음료수 자판기
#1번은 콜라, 2번은 사이다, 3번은 환타
#각 버튼에 따라 음료수 이름 출력
#이외의 숫자는 제공하지 않는 메뉴 출력
n = int(input("원하는 음료수 : "))
if n == 1:
    print("콜라")
elif n == 2:
    print("사이다")
elif n == 3:
    print("환타")
else:
    print("제공하지 않는 메뉴")
##################################
#dict을 사용한 풀이법
menu = {1:'콜라',2:'사이다',3:'환타'}
print(menu)
n = int(input("원하는 음료수 : "))
if n == 1:
    print(menu[1])
elif n == 2:
    print(menu[2])
elif n == 3:
    print(menu[3])
else:
    print("제공하지 않는 메뉴")


#11
#2중 반복문 사용
#학생인지(1) 아닌지(0)를 먼저 입력 받음
#학생인 겨우 1:초등학생, 2:중학생, 3:고등학생
#결과는 '학생이며 초등학생입니다' 또는 '학생이 아닙니다'
n = int(input("학생이면 1, 아니면 0 입력 : "))
if n==1:
    m = int(input("어느 학교에 다니십니까? : "))
    if m == 1:
        print("학생이며 초등학생입니다.")
    elif m == 2:
        print("학생이며 중학생입니다")
    elif m == 3:
        print("학생이며 고등학생입니다.")
    else:
        print("잘못입력하셨습니다.")
else:
    print("학생이 아닙니다.")


#12
#금액을 입력받고 자판기 번호를 선택하면 잔액을 계산하는 프로그램
pay = int(input("금액을 입력하세요 : "))
money = int(input("음료선택 : 1/콜라 600원, 2/사이다 700원, 3/환타 800원 : "))
if money == 1:
    pay = pay-600
elif money == 2:
    pay = pay-700
elif money == 3:
    pay = pay-800
else:
    print("잘못된 입력")
print("잔액 :",pay)


#13
#x가 11과 20사이면 '11~20', 21과 30사이면 '21~'30'
#아무것도 해당하지 않으면 '아무것도 해당하지 않음'이 출력
x = int(input())
if 11 <= x <= 20:
    print("11 ~ 20")
elif 21 <= x <= 30:
    print("21 ~ 30")
else:
    print("아무것도 해당하지 않음")


#14
#만 나이 입력(입력 값은 7 이상)
#각 나이에 맞게 요금을 착맣산 뒤 잔액 출력
#현재 교통카드에는 9000원
#주어진 문제 안에서 작성
#
age = int(input())
balance = 9000      #교통카드 잔액
#===========작성부분===========
if 7 <= age <= 12:
    balance = balance - 650
elif 13 <= age <= 18:
    balance = balance - 1050
elif 19 <= age:
    balance = balance - 1250
else:
    print("무료")
#===========작성부분============
print(balance)
#
#내 식대로 풀이
age = int(input())
balance = 9000      #교통카드 잔액
if age>=7:
    if age<=12:
        print("어린이 :",balance - 650,"원")
    elif 13 <= age <= 18:
        print("청소년 :", balance - 1050,"원")
    elif 19 <= age:
        print("어른 :", balance - 1250,"원")
    else:
        print("잘못된 입력")
else:
    print("무료입니다.")


#조건문 이용 예제 풀이
#15
#사용자로부터 하나의 숫자를 입력 받고 짝수/홀수 판별
n = int(input())
if n%2 == 0:
    print("짝수")
else:
    print("홀수")

