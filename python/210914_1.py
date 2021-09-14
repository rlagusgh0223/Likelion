#1
#함수예제
#함수는 사칙연산의 결과를 return(+, -, *, /)
#함수 안에서 프린트 되는 내용은 없음
#함수는 두개의 정수를 매개변수로 입력 받음
#메인 코드에서는 숫자 두개를 입력 받음
#함수를 호출하여 각각의 결과를 화면에 표시
#이때 문자열 %서식 이용하여, print는 한번만 쓸 것
def mad(x, y):
    return x+y, x-y, x*y, x/y

x, y = map(int,input().split())
n1, n2, n3, n4 = mad(x, y)
#nInput = list(map(int,input().split()))
#n1, n2, n3, n4 = mad(nInput[0],nInput[1])
print("+= %.2f  -= %.2f  *= %.2f  /= %.2f" %(n1,n2,n3,n4))


#2
#함수의 호출 과정(FILO) 알아보기
#함수는 스택 방식으로 호출된다
def mul(a, b):
    c = a*b
    return c

def add(a, b):
    c = a+b
    print(c)
    d = mul(a,b)
    print(d)

x = 10
y = 20
add(x, y)


#3
#몫과 나머지를 구하는 함수
#끝에 주석처리한 줄이 작성해야될 부분
x = 10
y = 3
def get_quotient_remainder(x,y):#
    return x//y, x%y#

quotient, remainder = get_quotient_remainder(x,y)
print('몫 : {0}, 나머지 : {1}'.format(quotient, remainder))


#4
#덧셈, 뺄셈, 곱셈, 나눗셈의 결과가 되도록 함수 작성
x, y = map(int, input().split())
def calc(x,y):#
    return x+y, x-y, x*y, x/y#

a, s, m, d = calc(x, y)
print('덧셈 : {0}, 뺄셈 : {1}, 곱셈 : {2}, 나눗셈 : {3}'.format(a, s, m, d))


#5
#사칙연산과 나머지를 구하는 함수 만들기
#각각의 연산을 하는 함수 5개 사용
#예외 상황에 대한 코드 포함
def add(x, y):
    return x+y
def sub(x, y):
    return x-y
def mul(x, y):
    return x*y
def div(x, y):
    return x/y
def rem(x, y):
    return x%y

while True:
    print('''===================
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
5. 나머지구하기
6. 나가기
===================''')
    n = int(input("원하는 연산자를 입력하세요 : "))
    if n == 6:
        print("종료를 선택하셨습니다. 프로그램을 종료합니다.")
        break
    elif 0 >= n or n >= 7:
        print("잘못 입력하셨습니다. 다시 입력해 주세요")
        print()
        continue
    a = int(input("첫번째 숫자를 입력하세요 : "))
    b = int(input("두번째 숫자를 입력하세요 : "))
    if n == 1:
        x = add(a,b)
    elif n == 2:
        x = sub(a,b)
    elif n == 3:
        x = mul(a,b)
    elif n == 4:
        x = div(a,b)
    elif n == 5:
        x = rem(a,b)
    print("결과는",x,"입니다.")
    print()


#6
#5번에서 5개의 함수를 1개의 함수로 만들것
def cal(n, x, y):
    if n == 1:
        return x+y
    elif n == 2:
        return x-y
    elif n == 3:
        return x*y
    elif n == 4:
        return x/y
    elif n == 5:
        return x%y

while True:
    print('''===================
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
5. 나머지구하기
6. 나가기
===================''')
    n = int(input("원하는 연산자를 입력하세요 : "))
    
    if 1 <= n <= 5:
        a = int(input("첫번째 숫자를 입력하세요 : "))
        b = int(input("두번째 숫자를 입력하세요 : "))
        x = cal(n, a, b)
        print("결과는",x,"입니다.")
        print()
        
    elif n == 6:
        print("종료를 선택하셨습니다. 프로그램을 종료합니다.")
        break
        
    else:
        print("잘못 입력하셨습니다. 다시 입력해 주세요")
        print()


#7
def cal(n, x, y):
    if n == '+':
        return x+y
    elif n == '-':
        return x-y
    elif n == '*':
        return x*y
    elif n == '/':
        return x/y
    elif n == '%':
        return x%y

while True:
    a = int(input("첫번째 숫자를 입력하세요 : "))
    b = int(input("두번째 숫자를 입력하세요 : "))
    strInput = input("연산자 입력(0누르면 종료) : ")

    if strInput == '0':
        print("종료를 선택하셨습니다. 프로그램을 종료합니다.")
        break
    
    elif strInput == '+' or strInput == '-' or strInput == '*' or strInput == '/' or strInput == '%':
        x = cal(strInput, a, b)
        print("결과는 %.2f입니다" %x)
        
    else:
        print("잘못 입력하셨습니다. 다시 입력해 주세요")
        print()


#8
#계산 맞추기 게임
#random모듈을 이용해서 간단한 덧셈,뺄셈,곱셈 문제를
#임의로 만들어줌
#답을 입력하면 정답인지 오답인지 계산해서 점수 매김
#반복 5회
#eval함수 쓰고 make_question함수 작성할것
import random

def make_question(x, n1, n2):
    return str(n1)+str(x)+str(n2)

cnt = 0
for i in range(5):
    n1 = random.randint(-99,99)
    n2 = random.randint(-99,99)
    ope = random.randint(1,3)
    if ope == 1:
        x = make_question('+', n1, n2)
    elif ope == 2:
        x = make_question('-', n1, n2)
    elif ope == 3:
        x = make_question('*', n1, n2)
    print(x,'=',end=' ')
    n = int(input())
    if eval(eval("x")) == n:
        cnt += 1

print("총 5문제중 %d문제 맞췄습니다"%cnt)
