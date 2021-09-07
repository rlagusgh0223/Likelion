#1
#오각별 그리기
import turtle as t
n = 5
t.shape('turtle')
for i in range(n):
    t.forward(100)  #별의 꼭지점
    t.right(144)    #별의 꼭지점이 72도니까 별로 돌아가기 위해 144도((360/n)*2)
    t.forward(100)  #꼭지점에서 중간으로
    t.left(72)      #별의 꼭지점은 72도(360/n =>n은 5니까 72)


#Small Project
#2
#1부터 10까지 순서대로 칸을 바꾸지 않고 공백 2자리 마다 표시
#for/while 모두 작성
for i in range(1,11):
    print(i, end='  ')
print()
j = 0
while j<10:
    j+=1
    print(j,end='  ')


#3
#두 자연수 n부터 m을 받고, n부터 m까지의 합을 구하는 프로그램
#for/while 모두 작성
n1 = int(input("시작하는 정수 : "))
n2 = int(input("끝나는 정수 : "))
nRes = 0
for i in range(n1,n2+1):
    nRes += i
print(n1,"부터",n2,"까지의 합은",nRes,"입니다")
nRes = 0
i = n1
while i<=n2:
    nRes += i
    i+=1
print(n1,"부터",n2,"까지의 합은",nRes,"입니다")


#4
#n부터 m을 입력 받고, n부터 m까지의 수 중에 짝수들의 제곱의 합
#for/while 모두 작성
n = int(input("시작 정수 : "))
m = int(input("끝 정수 : "))

total = 0
for i in range(n,m+1):
    if i%2 == 0:
        total += i**2
print(n,"부터",m,"사이 짝수 제곱의 합은",total,"입니다")

total=0
i=n
while i<=m:
    if i%2 == 0:
        total += i**2
    i += 1
print(n,"부터",m,"사이 짝수 제곱의 합은",total,"입니다")


#5
#리스트에 있는 평균 점수 구하기
#for/while
Kor = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for i in range(10):
    total += Kor[i]
print(total/len(Kor))

total = 0
i=0
while i<len(Kor):
    total += Kor[i]
    i+=1
print(total/len(Kor))


#6
#3과 5의 공배수는 if,elif로 했으므로 3의 배수로 한번만 계산됩니다
total = 0
for i in range(1000):               #for문
    if i%3 == 0:
       total += i
    elif i%5 == 0:
        total += i
print("결과는",total,"입니다")

total = 0                           #while문
i = 0
while i<1000:
    if i%3 == 0:
       total += i
    elif i%5 == 0:
        total += i
    i += 1
print("결과는",total,"입니다")


#7
#5명의 시험관이 채점한 학생의 점수(split,map,list사용)
#최고점수와 최저점수는 제외하고 나머지 점수들의 합계를 총점
#이 학생의 최종 실기 평균
#for, while사용

n = list(map(int,input("실기점수 : ").split()))
nMax = n[0]
nMin = n[0]
nRes = 0
for i in range(len(n)):     #반복문을 이용해서 최댓값(nMax), 최솟값(nMin)구한다
    if nMax < n[i]:
        nMax = n[i]
    if nMin > n[i]:
        nMin = n[i]
    nRes += n[i]        #리스트의 모든 값을 더한다
total = (nRes-(nMax+nMin))/(len(n)-2)
#리스트 값의 합에서 최소,최댓값을 빼고 평균을 구하기 위해 종류에서도 2개를 뺀다
print("이 학생의 평균 점수는",total,"입니다.")

nMax = n[0]
nMin = n[0]
nRes = 0
i=0
while i<len(n):
    if nMax < n[i]:
        nMax = n[i]
    if nMin > n[i]:
        nMin = n[i]
    nRes += n[i]
    i+=1
total = (nRes-(nMax+nMin))/(len(n)-2)
print("이 학생의 평균 점수는",total,"입니다.")

#===============================================
#max, min함수 이용
n = list(map(int,input("실기점수 : ").split()))
nMax = max(n)
nMin = min(n)

total = 0
for i in range(len(n)):     #for문
    total += n[i]
total -= (nMax+nMin)
print(total/(len(n)-2))

total = 0
i = 0
while i<len(n):             #while문
    total += n[i]
    i += 1
total -= (nMax+nMin)
print(total/(len(n)-2))

#===========================모범답안============================
Scores = list(map(int,input("실기점수 : ").split()))
total = 0
for i in Scores:
    total += i

largest = 0
smallest = 100
for i in Scores:
    if i>largest:
        largest = i
    elif i<smallest:
        smallest = i
avr = (total - largest - smallest) / (len(Scores)-2)
print(avr)
#===============================================================


#8
#각 학점별 학생들의 수 리스트로 출력
#grade_counter = [A학점인원, B학점인원,....,F학점인원]
scores = [86,72,98,60,45]
grade_counter = [0,0,0,0,0]

for i in scores:
    if i>=85:
        grade_counter[0] += 1
    elif i>=70:
        grade_counter[1] += 1
    elif i>=55:
        grade_counter[2] += 1
    elif i>=40:
        grade_counter[3] += 1
    else:
        grade_counter[4] += 1

print(grade_counter)


#9
#리스트에서 이름에 m 또는 h가 있는 사람 수(중복시 1명으로 간주)
name_list = ['matthew', 'mark', 'luke', 'john', 'paul', 'peter']
count = 0
for i in name_list:
    nlist = list(i)
    j = 0
    while j<len(nlist):
        if nlist[j] == 'm' or nlist[j] == 'h':
            count += 1
            break
        j+=1
print("m 또는 h가 이름에 포함된 사람은",count,"입니다")
#=========================모범답안===============================
#이중 for
name_list = ['matthew', 'mark', 'luke', 'john', 'paul', 'peter']
count = 0
for name in name_list:
    for n in name:
        if n=='m' or n=='h':
            count+=1
            break
print("m 또는 h가 이름에 포함된 사람은",count,"입니다")

#for 하
name_list = ['matthew', 'mark', 'luke', 'john', 'paul', 'peter']
count = 0
for name in name_list:
    if 'm' in name or 'h' in name:
        count += 1
print("m 또는 h가 이름에 포함된 사람은",count,"입니다")
#===================================================================


#10
#5명의 시험 점수 중 60점이 넘은 사람만 축하
#안넘었으면 안보이게
marks = [90, 25, 67, 45, 80]
j = 0
for i in marks:
    j+=1
    if i>60:
        print(j,"번째 학생 축하합니다. 합격입니다")

print()
i = 0
while i<len(marks):
    if marks[i]>60:
        i += 1
        print(i,"번째 학생 축하합니다. 합격입니다")
    i += 1

#continue 사용
marks = [90, 25, 67, 45, 80]
for i in range(len(marks)):
    if marks[i]<=60:
        continue
    print(i+1,"번째 학생 축하합니다. 합격입니다")

print()
i = 0
while i<len(marks):
    i += 1
    if marks[i-1]<=60:
        continue
    print(i,"번째 학생 축하합니다. 합격입니다")


#11
#'#'부분을 채워 arr[1,4,2,3]을 arr[3,2,4,1]로 바꾸기
arr = [1, 4, 2, 3]
left, right = 0, len(arr)-1 #left=0, right=len(arr)-1
#len(arr)//2    #정수로 받는다
#len(arr)/2    #실수로 받는다
while left < len(arr)//2:   #
    #left < right도 가능
    #중앙값을 기준으로 바꾼다
    #홀수라서 남는수는 바꿀 필요 없다
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print("변환된 arr은",arr,"입니다.")


#12
#입력된 정수의 구구단 출력
#숫자 * 숫자 = 숫자 형태
#for, while 둘 다
n = int(input("정수 : "))
for i in range(9):
    print(n,"*",i+1,"=",n*(i+1))
print()
i = 0
while i<9:
    i += 1
    print(n,"*",i,"=",n*i)


#13
#for, while문 작성
#구구단 세로로 9단까지 작성
#2단 3단 4단...9단
for i in range(1,10):
    for j in range(2,10):
        print(j,"*",i,"=",i*j,sep='',end='\t')
    print()

print()
i=1
while i<10:
    j=2
    while j<10:
        print(j,"*",i,"=",i*j,sep='',end='\t')
        j+=1
    print()
    i+=1
