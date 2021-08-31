"""
#
#실행결과
#2019/1/31
#10:33:57
year = 2019
month = 1
day = 31
hour = 10
minute = 33
second = 57
print(year, month, day, sep='/')
print(hour, minute, second, sep=":")

#실행결과
#2019/1/31 10:33:57
year = 2019
month = 1
day = 31
hour = 10
minute = 33
second = 57
print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=":")

#
#사과 1개 150원, 귤 1개 30원
#사과와 귤을 샀을때 총액은?
apple = 150
orange = 30
napple = int(input("사과의 개수 : "))
norange = int(input("귤의 개수 : "))
nTotal = apple * napple + orange * norange
print("총 가격은 ",nTotal,"원",sep='')

#
#사과 1개 150원, 귤 1개 30원
#사과와 귤을 샀을때 총액은?
apple = 150
orange = 30
napple, norange = map(int,input("사과와 귤의 개수(예:5/3) : ").split('/'))
nTotal = apple * napple + orange * norange
print("총 가격은 ",nTotal,"원",sep='')

#
#참,거짓 연산자 / 비교연산자
print(True)
print(False)

print(3>1)
print(3<1)

print(10 == 10)
print(10 != 5)
print('Python' == 'Python')
print("Python" == 'python')
print("Python" != 'python')

print(10>20)
print(10<20)
print(10>=10)
print(10<=10)

#==, !=는 값 자체를 비교
#is, is not은 객체(object)를 비교 <= 사용 빈도가 높지 않음
print(1 == 1.0)     #True
print(1 is 1.0)     #False
print(1 is not 1.0) #True

#
#논리 연산자
#and : 둘 다 참일때만 참
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#or : 둘 중 하나만 참이어도 참(둘 다 거짓일때만 거짓)
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#not : 논릿값 반대로
print(not True)
print(not False)

#not, and, or순으로 판단
print(not True and False or not False)
#1. not True 와 not False를 판단
#2. False and False or True가 된다
#3. False and False를 판단하여 False가 나와,
#   False or True가 되므로 최종 결과는 True
#실제로 잘 쓰이지는 않는다. 보통 ()를 이용한다.

#
#논리 연산자 + 비교 연산자
#논리 연산자와 비교 연산자를 같이 쓸 때는
#()를 이용하여 보는 사람이 알기 쉽게 해줘야 된다.
print(10 == 10) and (10 != 5)
print(10 > 5) or (10 < 3)
print(not (10>5))
print(not (1 is 1.0))

#bool : 문자열의 내용 관계 없이 값이 있으면 True
#       숫자는 0이 아니면 True
print(bool(1))
print(bool(0))
print(bool(1.5))
print(bool('False'))
print(bool(''))
print(bool(' '))

#
#단락 평가
#첫 번째 값만으로 결과가 확실할 때 두번째 값은 확인하지 않는 방법
#ex) and - 첫 값이 False면 두번째 값 확인 없이 False
print(True and 'Python')
#반환값 : Python
#파이썬에서 논리연산자는 단락평가에 따라 반환하는 값이 결정
#마지막으로 단락 평가를 실시한 값을 그대로 반환하기 때문
#논리연산자는 무조건 bool을 반환하지는 않는다.

print('Python' and True)
print("Python" and False)
#문자열 'Python'은 True니까 and 연산자가
#두번째 값을 확인하고 두번째 값을 반환

print(False and 'Python')
print(0 and 'Python')
#단락평가를 했을때 처음부터 값이 안되므로 처음 값을 반환한다.

#or
print(True or 'Python')
print('Python' or True)
#앞에 값이 True이므로 더 볼 것 없어서 앞에값 반환

print(False or 'Python')
print(0 or False)
#두번째 값까지 판단해야 한다면 두번째 값이 반환

#국어,영어,수학,과학 점수가 있을때 한 과목이라도 50점 미만이면 불합격
#합격이면 True, 불합격이면 False
korean = 92
english = 47
math = 86
science = 81
print(korean>=50 and english>=50 and math>=50 and science>=50)

#국어,영어,수학,과학 점수 입력
#국어는 90점 이상, 영어 80점 초과, 수학 85 초과, 과학 80점 이상 합격
#한 과목이라도 조건에 만족하지 않으면 불합격
#합격이면 True, 불합격이면 False
kor, eng, mat, sci = map(int, input("입력 : ").split())
print("결과 :",kor>=90 and eng>80 and mat>85 and sci>=80)

#map쓰지 않고
kor, eng, mat, sci = input("입력 : ").split()
print("결과 :",int(kor)>=90 and int(eng)>80 and int(mat)>85 and int(sci)>=80)

#
#문자열
hello = 'Hello, world!'
print(hello)
print(type(hello))
print('===========')
hello = "Hello, world!"
print(hello)
print(type(hello))

#여러줄로 된 문자열
#문자열 변수에 입력하면 그건 주석이 아니라 엔터를 포함한 문자열로 받아들임
hello = '''Hello, world!
안녕하세요.
Python입니다.'''
print(hello)
print('================')
hello = '''Hello, world!
안녕하세요.
Python입니다.'''
print(hello)

#작은따옴표를 넣고 싶다면 문자열을 큰따옴표로,
#큰따옴표를 넣고 싶다면 문자열을 작은따옴표로 묶어줌
#둘 다 쓰고 싶다면 '''~'''쓰면 된다
#(큰따옴표 3개로 해도 되지만 여기선 주석이랑 겹치므로 생략한다.)
s = "Python isn't difficult"
print(s)
s = 'He said "Python is easy"'
print(s)
h = '''aaa 'bbb' "ccc"'''
print(h)
"""
#하나의 변수s와 print를 사용하여 문자열 나오도록 코딩
s = '''Python is a programming language that lets you work quickly
and
integrate systems more effectively.'''
print(s)
