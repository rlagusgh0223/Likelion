#1
#학과 거북이 합친 수 8
#다리 수는 22
#학, 거북이 몇마리?
nTotal = 8
nLeg = 22
nTurtle = 4*nTotal  #전체가 거북이일때 다리 수
nSub = nTurtle - nLeg   #다리 수의 차 계산
nD1 = int(nSub/2)   #다리 수를 2로 나누면 학의 수(학 다리는 2개니까)
#학과 거북이를 합한 수에서 학의 수를 빼면 거북이의 수
nD2 = nTotal-nD1
print('학 :',nD1,"거북이:",nD2)

#2
money = 1000
cookiePrice = 600
print(id(money))
print(id(cookiePrice))
print(id(1000))
print(id(600))

money = money - cookiePrice
print(money)
print(id(money))

#3
x=3
y=4#y=3에서 변화
z=5
print(id(x),id(y),id(3),id(z),id(5),sep='\n')

#4
x = 10
print(x)
y = 'Hello, world!'
print(y)
print(type(x))
print(type(y))

#5
x,y,z = 10,20,30
print(x)
print(y)
print(z)

#6
x=10
print(x)
del x   #변수삭제
print(x) #x는 없다고 에러 나오게 됨

#7
x = None    #빈 변수 만들기
print(x)

#8
number = input("숫자를 입력하세요 : ")
print(number)

#9
nData1 = int(input("첫번째 수 : "))
nData2 = int(input("두번째 수 : "))
nResult = nData1 + nData2
print(nResult)

#10
name = input("이름을 입력하시오 : ")
print(name,"씨, 안녕하세요?")
print("파이썬에 오신 것을 환영합니다.")

