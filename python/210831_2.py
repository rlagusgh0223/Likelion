"""
#리스트와 튜플 사용하기
#리스트 = [요소,요소,요소]
a = [38,21,53,62,19]
print(a)
#리스트는 모든 자료형을 저장할 수 있으며,
#자료형을 섞어서 저장해도 됨
person = ['David',49,173.3,True]
print(person)

#빈 리스트 만들어보기
a = []
print(a)
b = list()
print(b)

#
#range
print(range(10))
print(type(range(10)))
a = list(range(10))
print(a)
b = list(range(5,12))
print(b)
c = list(range(-4,10,2))
print(c)
d = list(range(10,0,-1))
print(d)

a = list(range(11))
b = list(range(0,13,2))
c = list(range(13,2,-2))
d = list(range(-8,9,2))
e = list(range(-100,101,50))
print(a)
print(b)
print(c)
print(d)
print(e)

#
#튜플
#변경, 추가, 삭제 불가능(읽기 전용 리스트)
#()로 묶어주거나 ,로 구분하면 튜플이 됨
a = (38, 21, 53, 62, 19)
print(a)
print(type(a))
a = 38, 21, 53, 62, 19
print(a)
print(type(a))

#튜플도 여러 자료형을 섞어서 사용할 수 있다.
person = ('james', 17, 175.3, True)
print(person)

#괄호 안에 요소가 한개인 튜플을 만들려면 ,를 써야 한다
a = (38)
print(a)
print(type(a))  #int
b = (38,)
print(b)
print(type(b))  #tuple

#튜플은 리스트로, 리스트는 튜플로 변경 가능
a = [1,2,3]
print(a)
print(tuple(a))
b = (1,2,3)
print(b)
print(list(b))

print(list('Hello'))
print(tuple("Hello"))

a, b, c = [1,2,3]
print(a,b,c)
print(type(a))
print(a)    #a는 언팩킹이 되니까 int로 받는다.
d,e,f = (4,5,6)
print(d,e,f)
print(type(d))
print(d)

x = [1,2,3]
a,b,c = x
print(a,b,c)
y = (4,5,6)
d,e,f = y
print(d,e,f)

print(input().split())
x = input().split()
print(x)
print(type(x))
a,b=x   #a,b = input().split()과 같음
print(a,b)
print(type(a))

#리스트 [5, 3, 1, -1, -3, -5, -7, -9]가 출력되도록
#리스트 만들때는 range 사용
a = list(range(5,-10,-2))
print(a)

#정수가 입력되면 시작 숫자 -10, 끝 숫자 10
#입력된 정수만큼 증가하는 숫자가 들어가도록 튜플을 만들고 출력
n = int(input("정수 입력 : "))
print(tuple(range(-10,11,n)))

#정수가 입력되면 시작, 끝, 증가하는 숫자가 들어가도록 튜플 만들고 출력
fir,las,n = map(int,input("시작,끝,증가폭 입력 : ").split())
print(tuple(range(fir,las,n)))
#map 사용하지 않고
n1 = int(input("시작값 : "))
n2 = int(input("끝 값 : "))
n3 = int(input("증가값 : "))
print(tuple(range(n1,n2,n3)))

#
#시퀀스(연속적) 자료형 활용하기
#시퀀스 자료형(값이 연속적으로 이어진 자료형) : 리스트, 튜플, range, 문자열
#in : 특정 값이 있는지 확인
#not in : 특정 값이 없는지 확인
a = [0,10,20,30,40,50,60,70,80,90]
print(30 in a)  #True
print(100 in a) #False
print('=================')
print(30 not in a)  #False
print(100 not in a) #True

print(43 not in (38,76,43,62,19))
print(1 not in range(10))
print('P' not in 'Hello, Python')

#0 ~ 20 사이의 홀수 리스트 작성
#13이 리스트에 없는지 확인
#4가 리스트에 없는지 확인
lst = list(range(1,20,2))
print(lst)
print(13 not in lst)
print(4 not in lst)

#0 ~ 20 사이의 홀수 리스트 작성
#값을 받아서 그 값이 리스트에 있는지
lst = list(range(1,20,2))
n = int(input("리스트 확인 : "))
print(n not in lst)

#+연산자로 두 객체를 연결해 새 객체를 만들 수 있음
a = [0,10,20,30]
b = [9,8,7,6]
print(a+b)  #[0, 10, 20, 30, 9, 8, 7, 6]
a = [1,2,3]
b = (4,5)
print(a+list(b))   #[1, 2, 3, 4, 5]

a = [1,2]
b = [3,4]
c = a+b
print(a+b)
print(a)
print(b)
print(c)

#두개의 리스트 안에 '사과'가 있는지 확인
#연결하기로 작성
#논리 연산자로 작성
data1 = ['사과','배','귤','오렌지']
data2 = ['토마토','바나나','수박','딸기']
data = data1+data2
print('사과' in data)
print(('사과' in data1) or ('사과' in data2))

#range는 +로 연결 불가
#range를 연결하려면 리스트나 튜플에 넣어서 연결해야됨
#range(10) + range(10,20)은 작성 불가
print(list(range(10)) + list(range(10,20)))
print(tuple(range(10)) + tuple(range(10,20)))

#문자열은 +연산자로 연결할 수 있다
print('Hello, '+'world!')


#*연산자 : 특정 횟수 만큼 반복해서 새 시퀀스 객체를 만듬
print([0,10,20,30]*3) #[0, 10, 20, 30, 0, 10, 20, 30, 0, 10, 20, 30]

#range는 사용할 수 없다
#아래의 방법을 이용할 것
print(list(range(0,5,2))*3) #[0, 2, 4, 0, 2, 4, 0, 2, 4]

#문자열은 사용 가능
print('Hello, ' *3) #Hello, Hello, Hello,


#len : 시퀀스 객체의 요소 개수 구하기
a = [0,10,20,30,40,50,60,70,80,90]
print(len(a))
b = (38,76,43,62,19)
print(len(b))

#두개의 리스트 내부 요소의 총 개수 구하기
fru1 = ['사과','배','귤','오렌지']
fru2 = ['토마토','바나나','수박','딸기']
print(len(fru1+fru2))

print(len(range(0,10,2)))

#문자열의 길이 구하기
#hello = 'Hello, world!'
hello = '안녕하세요' #한글도 한 글자당 길이 1로 나옴
print(len(hello))

#시퀀스 객체의 각 요소는 순서가 정해져 있으며,
#이 순서를 인덱스라고 부름
a = [38,21,53,62,19]
print(a[0])
print(a[2])
print(a[4])

#튜플의 인덱스도 대괄호[]로 출력
b = (38,21,53,62,19)
print(b[0])

#range 인덱스도 출력 가능
r = range(0,10,2)
print(list(r))
print(r[2])

#문자열 인덱스도 출력 가능
hello = 'Hello. world!'
print(hello[7])

#1~20까지의 정수중 홀수를 요소로 가지는 리스트
#이 중 3번째 홀수를 찾아내어 표시하는 코드
lst = list(range(1,20,2))
print(lst)
print(lst[2])

#음수 인덱스 지정하기
#맨 뒤가 -1, 그 앞이 -2....
a = [38,21,53,62,19]
print(a[-1])    #19
print(a[-5])    #38

#튜플도 마찬가지
b = (38,21,53,62,19)
print(b[-1])    #19
print(b[-5])    #38

#range도 음수로 접근 가능
r = range(0,10,2)
print(list(r))    #[0,2,4,6,8]
print(r[-3])    #4

#문자열
hello = 'Hello, world!'
print(hello[-4])

#1~100까지 정수 중 짝수를 요소로 가지는 리스트
#마지막에서 3번째 짝수를 표시
lst = list(range(2,101,2))
print(lst)
print(lst[-3])

#인덱스의 범위를 벗어나면 아래와 같은 에러가 난다
a = [38,21,53,62,19]
print(a[5]) #IndexError: list index out of range
#
print(a[len(a)-1]) #a리스트의 마지막 출력
"""

#요소에 값 할당하기
a = [0,0,0,0,0]
a[0] = 38
a[1] = 21
a[2] = 53
a[3] = 62
a[4] = 19
print(a)
print(a[0])
print(a[4])
