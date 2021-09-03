#1
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
#next를 쓰면 다음 코드 확인 가능
#임의로 값을 입력해서 확인할 수 있다
#ex) total=4를 입력 가능


#2
#for 예제
#리스트 x에 들어있는 각 숫자(요소)에 10을 곱한 값 출력
#모든 숫자는 공백으로 구분
x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(i*10,end=' ')


#3
#정수 입력되면 입력된 정수의 구구단을 출력
n = int(input("입력 : "))
for i in range(1,10):
    print(n,'*',i,'=',n*i)


#4
#0부터 입력된 정수까지의 합
n = int(input("입력 : "))
ans = 0
for i in range(n+1):
    ans = ans+i
print(ans)


#5
#10개 돌의 무게를 입력 받은 후 평균
ans = 0
for i in range(10):
    print(i+1,"번째의 돌")
    n = float(input("무게(g) :"))
    ans = ans + n
print("평균 :",ans/10,'g')


#6
#학생의 수를 입력하고
#각 학생의 개별 점수를 입력 후 평균 계산
ans = 0
nStu = int(input("학생의 수 : "))
for i in range(nStu):
    print(i+1,"번 학생의 점수 : ",end='')
    n = int(input())        #input()은 변수를 받지 못한다
    ans += n
print("평균 :",ans/nStu,'점')


#7
cnt = int(input("반복 횟수 : "))
ans = cnt+1
while cnt>0:
    print('Hello, world!', ans - cnt)
    cnt-= 1


#8
#while문 예제
#1부터 10까지 순서대로 칸을 바꾸지 않고 공백 2자리 마다 표시
i = 0
while i<10:
    i += 1
    print(i, end='  ')


#9
#위의 식을 for문으로
for i in range(1,11):
    print(i, end='  ')


#10
#while문을 작성하여 -50에서 1까지의 수를 출력
#한 줄에 5개씩 표시하고 수와 수 사이는 탭만큼 띄워야 한다
i = -50
while i<2:
    j = 0
    while j<5 and i<2:
        print(i,end='\t')
        i+=1
        j+=1
    print()
#if문을 쓰고
#break를 안 배운걸로 기억해서 위에걸로 작성했음
i = -50
while i<2:
    j = 0
    while j<5:
        if i>=2:
            break
        else:
            print(i,end='\t')
            i+=1
            j+=1
    print()

#==================모범답안=========================
i = -50
count = 1
while i <= 1:   #이렇게 하면 내것과는 다르게 i가 2가 되면 바로 튕긴다
    print(i, end = '\t')
    if count%5 == 0:
        print()
    i+=1
    count+=1
#===================================================


#11
#while문을 이용하여 1부터 입력받은 수까지 더하는 프로그램
n = int(input("정수 입력 : "))
i = 0
ans = 0
while i<n:
    i += 1
    ans += i
print(ans)
#==================모범답안=========================
nData = int(input("입력 : "))
nTotal = 0
while nData > 0:
    nTotal += nData
    nData -= 1
print("총합 : ",nTotal)
#===================================================


#12
#정수를 받으면 그 정수에 대하여
#while문을 이용한 구구단
n = int(input("구구단 : "))
i = 0
while i<9:
    i += 1
    print(n,'*',i,'=',n*i)


#13
#5명의 학생들 합격인지 불합격인지
i = 0
marks=[90,25,67,45,80]
while i<5:
    if marks[i] >= 60:
        print(i+1,"번 학생은 합격입니다.")
    else:
        print(i+1,"번 학생은 불합격입니다.")
    i += 1


#14
#합격한 사람만 축하메시지
#불합격한 사람은 보이지 않도록
i = 0
marks=[90,25,67,45,80]
while i<5:
    if marks[i] >= 60:
        print(i+1,"번 학생 축하합니다. 합격입니다.")
    i += 1


#15
#while을 이용하여 이 학급의 평균점수를 구하시오
Kor = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
ans = 0
i = 0
while i<len(Kor):
    ans += Kor[i]
    i += 1
print("평균 :", ans/len(Kor))


#16
#2의 20승을 구하는 프로그램
n = 0
ans = 1
while n<20:
    n += 1
    ans *= 2
print("2의 20승은",ans,"입니다")


#17
#윤년판단
#4로 나누어 떨어지면 윤년
#단, 100으로 나누어떨어지면 평년
#단, 400으로 나누어 떨어지면 윤년
year = int(input("년도 : "))
while year != -1:
    if year % 400 == 0:
        print("윤년")
    elif year % 100 == 0:
        print("평년")
    elif year % 4 == 0:
        print("윤년")
    else:
        print("평년")
    print()
    year = int(input("년도 : "))
#===================모범답안====================
year = 0
while year != -1:
    year = int(input("년도 : "))
    if not year%400 or not year%4 and year%100:
        print("윤년")
    else:
        print("평년")
#===============================================
