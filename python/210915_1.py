"""
#1
#filter 사용하기
#filter는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져온다
#filter에 지정한 함수의 반환값이 True일때만 해당 요소를 가져온다
#filter는 함수의 참인 요소만 가져온다
    
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
#filter
def f(x):
    return x>5 and x<10
print(list(filter(f,a)))    #[8, 7, 9]


#함수 f를 람다 표현식으로
print(list(filter(lambda x:x>5 and x<10, a)))    #[8, 7, 9]


#reduce
#reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤
#이전 결과와 누적해서 반환하는 함수
#functools 에서 가져와야함

def f(x,y):
    return x+y
a = [1,2,3,4,5]
from functools import reduce
print(reduce(f, a))     #15
    #a를 f함수하니까 a의 요소 전부를 더한 15가 나온다
    #((((1+2)+3)+4)+5)


#lambda표현식으로 reduce사용
print(reduce(lambda x, y: x+y, a))     #15





#2
#클로저
#전역변수의 사용범위
#전역범위 : 전역변수에 접근할 수 있는 범위
x = 10          #전역변수
def foo():
    print(x)    #전역변수 출력

foo()
print(x)        #전역변수 출력



#지역변수의 사용범위
def foo():
    x = 10      #foo의 지역 변수
    print(x)    #foo의 지역 변수 출력

foo()
print(x)        #에러. foo의 지역 변수는 출력할 수 없다



#함수 안에서 전역 변수 변경하기
x = 10      #전역 변수
def foo():
    x = 20    #x는 foo의 지역 변수
    print(x)    #foo의 지역 변수 출력(20)

foo()
print(x)    #전역 변수 출력(10)


#함수 안에서 전역 변수의 값을 변경하려면 global 키워드 사용
x = 10      #전역 변수
def foo():
    global x    #전역 변수 x를 사용하겠다고 설정
    x = 20      #x는 전역 변수
    print(x)    #전역 변수 출력(20)

foo()
print(x)    #전역 변수 출력(20)


#만약 저녁 변수가 없을 때 함수 안에서 global을 사용하면 해당 변수는 전역변수가 됨
#전역변수 x가 없는 상태
def foo():
    global x    #x를 전역 변수로 만듦
    x = 20      #x는 전역 변수
    print(x)    #전역 변수 출력

foo()
print(x)    #전역 변수 출력



#함수 안에서 함수 만들기
#def로 함수를 만들고 그 안에서 다시 def로 함수를 만듦
#바깥쪽 함수의 지역 변수는 그 안에 속한 모든 함수에서 사용 가능
def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)
    print_message()

print_hello()       #Hello, world!


#지역 변수 변경하기
#안쪽 함수에서 바깥쪽 함수의 지역 변수를 변경
def A():
    x = 10      #A의 지역 변수 x
    def B():
        x = 20    #x에 20 할당

    B()
    print(x)    #x의 지역 변수 x 출력(10)

A()


#현재 함수의 바깥쪽에 있는 지역 변수의 값을 변경하려면
#nonlocal 사용
def A():
    x = 10              #A의 지역 변수 x
    def B():
        nonlocal x      #현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20          #A의 지역 변수 x에 20 할당

    B()
    print(x)            #A의 지역 변수 x 출력(20)

A()


#nonlocal은 현재 함수의 바깥쪽에 있는 지역 변수를 찾을때
#가장 가까운 함수부터 찾음
def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x += 30
            y += 300
            print(x)    #50
            print(y)    #400
        C()
    B()
A()


#함수 몇 단계든 상관없이 global 키워드를 사용하면 무조건 전역 변수 사용
x = 1
def A():
    x = 10
    def B():
        x = 20
        def C():
            global x
            x += 30
            print(x)    #31
        C()
    B()
A()



#클로저 사용하기
#함수 바깥쪽에 있는 지역 변수 a,b를 사용하여
#계산하는 함수 mul_add를 만둔 뒤에 mul_add자체를 반환
def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a*x + b    #함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add    #mul_add함수를 반환
                        #함수를 반환할때는 이름만 쓰고 ()는 쓰지 않는다

c = calc()  #함수의 리턴값이 c가 된다
            #calc의 리턴값은 mul_add
            #c를 이용해서 호출하면 mul_add를 사용
print(c(1),c(2),c(3),c(4),c(5))     #8 11 14 17 20
#c에 저장된 함수 mul_add가 클로저


#lambda로 클로저 만들기
def calc():
    a = 3
    b = 5
    return lambda x: a*x + b    #람다 표현식을 반환

c = calc()
print(c(1), c(2), c(3), c(4), c(5))     #8 11 14 17 20


#클로저의 지역 변수 변경하기
#nonlocal 사용

#total이 mul_add 외부에 있으므로 값이 변한상태에서 유지
def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add

c = calc()
c(1)    #8
c(2)    #19
c(3)    #33


#total이 mul_add 내부에서 매번 초기화
def calc():
    a = 3
    b = 5
    def mul_add(x):
        total = 0
        total = total + a * x + b
        print(total)
    return mul_add

c = calc()
c(1)    #8
c(2)    #11
c(3)    #34


#다른 변수의 클로저 사용
def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add

c = calc()
c(1)    #8(0 + 3*1 + 5)
c(2)    #19(8 + 3*2 + 5)
b = calc()
b(3)    #b클로저가 생성되며 total이 초기화 되어 14출력(0 + 3*3 + 5)
print('============')
print(b(3))     #28(14 + 3*3 + 5)   <- 이건 print값이지 리턴값은 아니다
                #None <- 리턴되는 값이 없다는 뜻(mul_add는 리턴은 없다)


#호출 횟수를 세는 함수 만들기
#함수 c를 호출할때마다 호출 횟수가 출력되게
#클로저 이용
def counter():
    i = 0
    def count():
    #==========내가 작성한 부분
        nonlocal i  #nonlocal해주지 않으면 위의 i를 사용하지 못한다(i의 값을 수정하지 못한다)
        i += 1      #global을 쓰면 밑에랑 겹치게 되고 클로저를 쓰는 의미가 없다
        return i    #밑에서 print를 했으니까 none없이 출력하려면 리턴을 해야된다
    return count    #count()함수를 호출해줘야 그 안에 식을 사용함
    #==========================
    
c = counter()
for i in range(10):
    print(c(), end=' ')
"""




#3
#텍스트 파일 입출력
#아래 코드로는 해당 행(5줄)만 출력할 수 있다
inFp = open("data_210915.txt","r",encoding='utf-8')#같은 폴더에 있으니까 처음에 좌표 안줘도 된다
inStr = inFp.readline()
print(inStr, end='')
inStr = inFp.readline()
print(inStr, end='')
inStr = inFp.readline()
print(inStr, end='')
inStr = inFp.readline()
print(inStr, end='')
inStr = inFp.readline()        #파일보다 읽어오는 줄이 더 많다면 그냥 안 읽어오고 끝난다
print(inStr, end='')    #내 파일에는 4줄만 있으니까 이 코드는 작동 안함
inFp.close()
