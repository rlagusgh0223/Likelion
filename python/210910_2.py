#1
#map은 리스트의 요소를 지정된 함수로 처리해주는 함수
#map은 원본 리스트를 변경하지 않고 새 리스트를 생성
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)        #[1, 2, 3, 4]
#매번 for반복문으로 반복하면서 요소를 변환하기보다
#map을 사용하면 편리
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int,a))
print(a)

#range를 이용해서 숫자를 만든 뒤 숫자를 문자열로 변환
a = list(map(str,range(10)))
print(a)    #['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a = list(map(int,range(10)))
print(a)    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(map(int,'12345')))    #[1, 2, 3, 4, 5]
print(list(map(float,'12345')))    #[1.0, 2.0, 3.0, 4.0, 5.0]
print(list(map(str,'12345')))    #['1', '2', '3', '4', '5']

#a, b = map(int, input().split())을 풀어쓰면 다음과 같은 코드가 됨
x = input().split()     #input().split()의 결과는 문자열 리스트
m = map(int, x)         #리스트의 요소를 int로 변환, 결과는 맵 객체
a, b = m                #맴 객체는 변수 여러 개에 저장할 수 있음
print(a, b)


#2
#튜플 응용하기
#값이 여러 개일 경우 처음 찾은 인덱스를 구함
a = (38, 21, 53, 62, 19, 53)
print(a.index(53))              #2

#특정 값의 개수 구하기
a = (10, 20, 30, 15, 20, 40)
a.count(20)                     #2

#a라는 튜플의 요소를 for문과 while문으로 하나씩 출력
a = (38, 21, 53, 62, 19)
for i in a:
    print(i,end=' ')
print()
i = 0
while i<len(a):
    print(a[i],end=' ')
    i += 1

#튜플 표현식 사용하기
#tuple(식 for 변수 in 리스트 if 조건식)
a = tuple(i for i in range(10) if i%2 == 0)
print(a)    #(0, 2, 4, 6, 8)

#튜플로 묶어주지 않으면 제너레이터 표현식이 됨
a = (i for i in range(10) if i%2 == 0)
print(a)    #<generator object <genexpr> at 0x000001A785D97DD0>

#tuple에 map사용하기
a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)    #(1, 2, 3, 4)

#tuple에서 min, max sum 사용 가능
a = (38, 21, 53, 62, 19)
print(min(a))
print(max(a))
print(sum(a))


#3
#리스트/튜플 응용 연습문제1
#리스트에서 특정 요소만 뽑아내기
#문자열 길이가 5인것들만 리스트 형태로 출력
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i)==5]
print(b)

#리스트/튜플 응용 연습문제2
#정수 두개 입력(첫번째 정수는 1~20, 두번째 정수는 10~30, 첫번째는 두번째보다 항상 작다)
#첫번째 정수부터 두번째 정수까지를 지수로하는 2의 거듭제곱 리스트
#리스트의 두번째 요소와 뒤에서 두번째 요소는 삭제 후 출력
n, m = map(int,input().split())   #정수 두개 입력
ans = []
if 1<=n<=20 and 10<=m<=30 and n<m:  #(첫번째 정수는 1~20, 두번째 정수는 10~30, 첫번째는 두번째보다 항상 작다)
    #for i in range(n,m+1):
     #   ans.append(2**i)            #첫번째 정수부터 두번째 정수까지를 지수로하는 2의 거듭제곱 리스트
    ans = [2**i for i in range(n,m+1)]
    ans.pop(1)
    ans.pop(-2)
    print(ans)                      #리스트의 두번째 요소와 뒤에서 두번째 요소는 삭제 후 출력
else:
    print("잘못된 입력")

#리스트/튜플 응용 연습문제3
#아래와 같은 딕셔너리가 주어졌을때 30살 이상인 사람의 이름과 나이 표시
#반복문과 조건문을 활용하여 딕셔너리의 키/값을 활용
ai_classes = {
     'class01' : [
                {'name' : '서준', 'age' : 24},
                {'name' : '하준', 'age' : 34},
                {'name' : '도윤', 'age' : 37},
                {'name' : '시윤', 'age' : 19},
                {'name' : '은우', 'age' : 31}
     ],
     'class02' : [
                  {'name' : '지호', 'age' : 34},
                  {'name' : '예준', 'age' : 19},
                  {'name' : '동원', 'age' : 21},
                  {'name' : '민정', 'age' : 22},
                  {'name' : '효주', 'age' : 24}
     ]
 }

for i in range(len(ai_classes['class01'])):
    if ai_classes['class01'][i]['age'] >= 30:
        print(ai_classes['class01'][i]['name'],":",ai_classes['class01'][i]['age'],'/',end=' ')
for i in range(len(ai_classes['class02'])):
    if ai_classes['class02'][i]['age'] >= 30:
        print(ai_classes['class02'][i]['name'],":",ai_classes['class02'][i]['age'],'/',end=' ')
print()

#=========================================모범답안=====================================
for class_name in ai_classes:
    #print(class_name)
    #print(len(ai_classes[class_name]))
    for i in range(len(ai_classes[class_name])):
        if ai_classes[class_name][i]['age'] >= 30:
            print(ai_classes[class_name][i]['name'],":",ai_classes[class_name][i]['age'],'/',end=' ')
#또 다른 방법
print()
for i in ai_classes.values():
    for j in i:
        if j['age'] >= 30:
            print(j['name'],':',j['age'],'/',end=' ')
#======================================================================================

#리스트/튜플 응용 연습문제4
#로또 번호 생성기
    #1~50사이에서 생성
    #총 7개의 번호 축출
    #축출된 번호는 오르차순으로
    #10번 반복해서 생성
import random
for i in range(10):
    lotto = []
    while len(lotto)<7:
        n = random.randint(1,50)
        if n not in lotto:
            lotto.append(n)
    #n = random.sample(range(1,51),7) 쓰면 한번에 중복되지 않는 랜덤한 값 출력
    lotto.sort()
    print(lotto)

#리스트/튜플 응용 연습문제5
#10진수를 입력 받아 2진수 변환하는 코드 작성
n = int(input("2진수 변환할 10진수 입력 : "))
a = []
while True:
    if n == 0:      #변환이 끝나 n이 더이상 변환할 수 없다면 반복 종료
        break
    else:
        a.append(n%2)   #현재 입력 받은 값을 2로 나눈 나머지는 리스트에 넣는다
        n = n//2        #2로 나눈값의 몫을 다시 n으로 받아 그 다음 2진수로 나누기
a.reverse()         #리스트에는 처음부터 나눈 나머지가 입력됐으므로 반대로 리스트를 나열해준다
for i in range(len(a)):
    print(a[i],end='')  #나열된 리스트값을 순서대로 출력한다



#4
#2차원 리스트
#아파트 동호수 부르는거 생각하면 편하다
#[x][y][z] x동 y층 z호 : 앞에가 큰 값이 나온다
a = [[10, 20], [30, 40], [50, 60]]
print(a[0][0])      #세로 인덱스 0, 가로 인덱스 0
print(a[1][1])      #세로 인덱스 1, 가로 인덱스 1
print(a[2][1])      #세로 인덱스 2, 가로 인덱스 1
print(a[0][1])      #세로 인덱스 0, 가로 인덱스 1
a[0][1] = 1000
print(a[0][1])

#2차원 리스트의 요소 모두 출력하기
a = [[10, 20], [30, 40], [50, 60]]
for i in a:
    for j in i:
        print(j, end=' ')
    print()
#2차원 for사용하지 않고도 같은 결과를 낼 수 있다
print()
for x, y in a:
    print(x,y)
#range를 이용해서 같은 결과
print()
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
