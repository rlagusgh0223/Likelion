#1
print(float(5))
print(float(1+2))
print(float('5.3'))

#2
print(13+(22-3)*4)
print(13+(((22-3)*4)/5))

#3
#소음이 가장 심한 층은?
#거리 : 12m
#소음 가장 심한 층 : 0.2467*거리+4.159
print('가장 시끄러운 층은 =',int(0.2467*12+4.159),"층")

#4
#냉장고 월 31,689원에 무이자 24개월 할부
#냉장고의 총 금액은?
print("냉장고 가격은",31689*24,"원 입니다")

#5
print("Number Words")
print()
print(1,": One")
print("2 : Two")
print(3,": Three")

#6
x = 100
x = 200
print(x)

#7
x = 100
y = 200
sum = x+y
print(sum)

#8
name = "홍길동"
address = "서울시 종로구 1번지"
print(name)
print(address)

#9
score = 10
score = score+1
print(score)

#10
x = 100
y = 200
total = x+y
print(x,"과",y,"의 합은",total,"입니다.")
#참고사항 - 변수를 만들때 아래 문자를 앞에 붙이면 알기 편하다
#n:정수 - nx = 5
#f:실수 - fx = 5.0
#str:문자열 - strx = '5'

#11
a = 2
b = 3.14
c = a+b #컴퓨터에서 부동소수점 표현방식상 표현
print(a)
print(b)
print(c)
print(round(c,2))   #c를 소수점 2자리까지만 표기
print("%.2f" %(c))
print(a+b)
print(a,b,a+b,c)
a = 10
print("a에 저장된 값은",a,"입니다.")

#12
nData1 = 7
nData2 = 3
nTotal = nData1+nData2
print(nData1,"+",nData2,"=",nTotal)
nTotal = nData1-nData2
print(nData1,"-",nData2,"=",nTotal)
nTotal = nData1*nData2
print(nData1,"*",nData2,"=",nTotal)
nTotal = nData1/nData2
print(nData1,"/",nData2,"=",nTotal)

#13
nData1 = 7
nData2 = 3
nTotal = divmod(nData1,nData2)  #몫과 나머지를 함께 구하기
print(nData1,"/",nData2,"의 몫과 나머지는",nTotal,"입니다.")
