#조건문 이용 예제 풀이(210902_1의 15번에서 이어짐)
#1
#입력받은 값에 +20을 출력
#출력값의 범위는 ~255
#255를 초과하는 경우 255를 출력
n = int(input("입력값 : "))
n = n + 20
if n>255:
    print("출력값 : 255")
else:
    print("출력값 :", n)


#2
#입력 받은 후 해당값에 20을 뺀값을 출력
#출력 값의 범위는 0 이상
#0보다 작으면 0을 출력
n = int(input("입력값 : "))
n -= 20
if n<0:
    n = 0
#else:
#    n = n
print("출력값 :",n)


#3
#입력 받은 후 해당값에 20을 뺀 값을 출력
#값의 출력 범위는 0~255
#0보다 작은 값이 되는 경우 0
#255보다 크면 255를 출력
n = int(input())
n = n-20
if 0<=n<=255:
    print("출력값 :",n)
elif n<0:
    print("출력값 : 0")
#elif n>255:
else:
    print("출력값 : 255")


#4
#사용자로부터 입력 받은 시간이 정각인지 판별하라
#내 풀이
time,minuit = map(int,input("현재시간 : ").split(':'))
if minuit == 00:
    print("정각입니다")
else:
    print("정각이 아닙니다")
#슬라이스 이용(r[:])
time = input("현재시간 : ")
if time[3:] == '00':
    print("정각입니다.")
else:
    print("정각이 아닙니다.")
    
#=================모범답안==================
#1번째 풀이
hour, min = input("현재시간 : ").split(':')
if min == '00':
    print("정각입니다.")
else:
    print("정각이 아닙니다.")
#2번째 풀이
time = list(map(int,input("현재시간 : ").split(':')))
print(time[0],time[1])
if time[1] != 0:
    print("정각이 아닙니다.")
else:
    print("정각입니다.")
#3번째 풀이    <- 이게 익숙해야된다.
data = input("입력값 : ")
if data[3:] == '00':
    print("정각입니다.")
else:
    print("정각이 아닙니다.")
#=====================================================


#5
#만나이를 입력 받고 미성년자인지 판별
#나이는 '15세'와 같은 형식으로 입력
#입력범위 : 10 ~ 99세
#19세 이상이 성년
age = input("나이는 : ")
if 10<=int(age[0:2])<=99:
    if int(age[0:2])>=19:
        print("성년 입니다.")
    else:
        print("미성년 입니다.")
else:
    print("잘못된 입력")


#6
#주민등록번호 뒷자리 7자리중 맨 앞번호 1,3은 남자
#2,4는 여자를 의미함
#주민등록번호 뒷자리를 입력받아 남/여를 확인하는 코드
#자릿수가 틀리면 틀리다는 메시지 표시하고 종료
number = input("주민번호 뒷자리 : ")
if len(number) == 7:
    if int(number[0]) == 1 or int(number[0]) == 3:
        print("남자입니다.")
    elif int(number[0]) == 2 or int(number[0]) == 4:
        print("여자입니다.")
else:
    print("자릿수가 틀립니다.")
#======================모범답안=====================
q = input()
if len(q) != 7:
    print("잘못된 자릿수")
else:
    q = int(q[0])
    if q==1 or q==3:
        print("남성")
    elif q==2 or q==4:
        print("여성")
    else:
        print("잘못된 입력")
#===================================================


#7
#만나이를 입력 받고 미성년자인지 판별
#나이는 '15세'와 같은 형식으로 입력
#19세 이상이 성년
#입력범위(0 ~ 99세) 이외의 입력은 예외 처리할 것
age = input("나이는 : ")
if len(age) != 3:
    print("잘못된 입력")
else:
    age = int(age[:2])
    if age >=19:
        print("성년 입니다.")
    else:
        print("미성년 입니다.")
#======================모범답안=====================
strAge = input("나이는 :")
nAge = int(strAge[:len(strAge)-1])
print(nAge)
if 99 < nAge or nAge<10:
    myStr = "잘못된 입력"
elif 0<= nAge < 19:
    myStr = "미성년입니다."
else:
    myStr = "성년입니다."
print(myStr)
#===================================================


#8
#입력받은 단어가 아래 fruit리스트에 포함되어 있는지 확인
#포함되었다면 '정답입니다'를, 아닐경우 '오답입니다'를 출력
fruit = ["사과","포도","홍시"]
strData = input("좋아하는 과일은? : ")
if strData in fruit:        #변수 in 자료구조 : 변수가 리스트 안에 있으면 True 반환
    print("정답입니다.")
else:
    print("오답입니다.")


#9
#투자 경고 종목 리스트가 있을 때
#사용자로부터 종목명을 입력받은 후
#투자 경고 종목이면 '투자 경고 종목입니다'
#아니면 '투자 경고 종목이 아닙니다' 출력
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
strData = input()
if strData in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")


#10
#fruit딕셔너리가 정의되어 있다
#사용자가 입력한 값이 딕셔너리 키값에 포함되었다면 '정답입니다'
#아니면 '오답입니다' 출력
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
strData = input("제가 좋아하는 계절은 : ")
if strData in fruit:    #또는 fruit.keys()
                        #딕셔너리에 key가 생략되면 기본적으로 키값으로 검사하기 때문
    print("정답입니다")
else:
    print("오답입니다")


#11
#fruit딕셔너리가 정의되어 있다
#사용자가 입력한 값이 딕셔너리 values값에 포함되었다면 '정답입니다'
#아니면 '오답입니다' 출력
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
strData = input("좋아하는 과일은 : ")
if strData in fruit.values():    
    print("정답입니다")
else:
    print("오답입니다")


#12
#자판기 만들기
#금액 입력(최대 금액은 10,000원)
#금액이 부족한 경우와 최대 금액 초과 두가지 경우 정리
#음료선택 : 1-사이다(700원), 2-콜라(600원), 3-오렌지쥬스(800원)
nPay = int(input("금액을 입력하세요 : "))
if nPay<=10000:
    nDrink = int(input("음료를 선택하세요 : "))     #음료 선택 후 계산
    if nDrink == 1:
        nPay = nPay - 700
    elif nDrink == 2:
        nPay = nPay - 600
    elif nDrink == 3:
        nPay = nPay - 800
    else:
        print("잘못된 입력")             #없는 음료 선택시 출력
        
    if nPay<0:
        print("잔액이 부족합니다")          #잔액 부족
    else:
        print("잔액은", nPay,"원입니다.")
        
else:
    print("입력 한도를 초과했습니다.")     #최대 금액 초과

#===========================모범답안==============================
nData = int(input("금액을 입력하세요"))
nSel = int(input("선택"))
if(nData > 10000):
    print("10000원 초과")
else:
    if(nSel == 1):
        if(nData<700):
            print("금액부족")
        else:
            print("잔액은",nData-700,"원입니다")
    elif(nSel == 2):
        if(nData<600):
            print("금액부족")
        else:
            print("잔액은",<nData-600,"원입니다")
    elif(nSel == 3):
        if(nData<800):
            print("금액부족")
        else:
            print("잔액은",<nData-800,"원입니다")
    else:
        print("잘못된 선택입니다.")
#=================================================================

#딕셔너리 이용
input_money = int(input("금액을 입력하세요 : "))
menu_dic = {"1":700, "2":600, "3":800}

if input_money>10000:
    print("금액 초과")
else:
    input_menu = input("음료 선택 : ")
    if input_money - menu_dic[input_menu]<0:
        print("금액 부족")
    else:
        return_money = input_money - menu_dic[input_menu]
        print("잔액은", return_money,"입니다")


#13
#text계산기 만들기
#+, -, *, / 사칙연산만 처리
#잘못된 연산자, 0으로 나누기 예외 처리
n1 = int(input("첫번째 숫자 : "))
n2 = int(input("두번째 숫자 : "))
text = input("연산자 : ")
if text != '+' and text != '-' and text != '*' and text != '/':
    print("잘못된 연산자")
elif text == '/' and n2 == 0:
    print("0으로 나눌 수 없습니다")
else:
    if text == '+':
        nResult = n1+n2
    elif text == '-':
        nResult = n1-n2
    elif text == '*':
        nResult = n1*n2
    elif text == '/':
        nResult = n1/n2
    print("정답 :",nResult)

#==========================모범답안=============================
cCal = input("연산자")
nData1 = int(input("첫번째 숫자"))
nData2 = int(input("두번째 숫자"))
if cCal == '+':
    print(nData1, '+', nData2, '=', nData1+nData2)
elif cCal == '-':
    print(nData1, '-', nData2, '=', nData1-nData2)
elif cCal == '*':
    print(nData1, '*', nData2, '=', nData1*nData2)
elif cCal == '/':
    if nData2 != 0:
        print(nData1, '/', nData2, '=', nData1/nData2)
    else:
        print("0으로 나눌 수 없습니다")
else:
    print("잘못된 연산자")
#===============================================================
