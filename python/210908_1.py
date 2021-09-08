#1
#반복문 예제 13
#투표 진행한 결과 votes에 있는 번호 중
#가장 많은 표를 얻은 후보가 누구이며 몇표인지 출력
#votes = [5, 2, 3, 4, 1, 2, 1, 2, 2, 3]
#votes = [2, 5 ,3, 4, 1, 5, 1, 5, 5, 3]
votes = [1,2,3,4,1,2,3,4,3,3]
candidates = ['','전정국','김남준','박지민','정호석','김태형']
cnt = [0,0,0,0,0,0]
ncMax = cnt[0]
for i in range(1,6):         #후보번호(1~5)를 확인하기 위한 반복문
    for j in range(0,len(votes)):     #votes와 해당 후보번호가 맞는지 확인하는 반복문
        if i == votes[j]:         #후보번호와 votes안의 값이 같다면
            cnt[i] += 1             #cnt의 해당 개수 1 증가
print(cnt)
for i in range(1,len(cnt)):       #nMax가 어차피 0번째 값이니까 1부터 시작
    if ncMax < cnt[i]:  #nMax값 확인
        ncMax = cnt[i]
        nMax = i
print(candidates[nMax],"후보가 총",cnt[nMax],"표를 얻어 당선되었습니다.")

#=================================모범답안===================================
votes = [2, 5 ,3, 4, 1, 5, 1, 5, 5, 3]
candidates = ['','전정국','김남준','박지민','정호석','김태형']
count = [0]*6

#투표수 집계(count 만들기)
for x in votes:
    count[x] += 1
#print(count)

#최대표 얻은 후보 찾기
Max=0
i = 1
while i<len(count):
    if count[i]>Max:
        Max = count[i]
        elected = i
    i += 1
print(candidates[elected],"후보가 총",cnt[elected],"표를 얻어 당선되었습니다.")
#============================================================================


#2
#반복문 예제 14
#숫자를 입력받고 순환하는 광고판
n = int(input("순환할 숫자 : "))

#for문
for i in range(1,n+1):
    for j in range(i,n+1):  #처음 1~n나오는 부분
        print(j,end=' ')
    for j in range(1,i):    #n까지 갔을때 다시 1부터 입력하는 부분
        print(j,end=' ')
    print()
    
#while문
print()
i = 1
while i<=n:
    j = i
    while j <= n:           #처음 1~n나오는 부분
        print(j, end=' ')
        j += 1
    j = 1
    while j < i:            #n까지 갔을때 다시 1부터 입력하는 부분
        print(j, end=' ')
        j += 1
    print()
    i += 1

#=================================모범답안===================================
num = int(input("순환할 숫자 : "))
i = 0
while i<num:
    j=0
    while j<num:
        print((i+j)%num+1, end=' ')
        j+=1
    print()
    i += 1

print()
for i in range(1,num+1):
    for j in range(i,num+i):
        if j%num == 0:
            print(num,end=' ')
        else:
            print(j%num, end=' ')
    print()
#============================================================================


#3
#반복문 예제 15
#-(1^2)+(2^2)-(3^2)+(4^2)...-(99^2)+(100^)의 결과 출력
#10개 출력되면 한줄 띄울것

#while문
i = 1
nResult = 0
while i<=100:           #1부터 100까지 반복
    if i%2==0:          #짝수는 제곱 후 더한다
        nResult += i**2
        print('+', i*i, end='\t')
    else:               #홀수는 제곱 후 뺀다
        nResult -= i**2
        print('-', i*i, end='\t')
    if i%10==0:
        print()
    i += 1
print()
print(nResult)
print()

#for문
nResult = 0
for i in range(1,101):      #1부터 100까지 반복
    if i%2 == 0:          #짝수는 제곱 후 더한다
        nResult += i**2
        print('+', i*i, end='\t')
    else:               #홀수는 제곱 후 뺀다
        nResult -= i**2
        print('-', i*i, end='\t')
    if i%10==0:
        print()
print()
print(nResult)

#=================================모범답안===================================
i = 1
total = 0
line = 0
while i<=100:
    if i%2 == 0:
        total += i*i
        #print('+', i*i, end='\t')
    else:
        total -= i*i
        #print('-', i*i, end='\t')
    i += 1

    line += 1
    if line==10:
        line=0
        print()
print(total,"입니다")
#============================================================================


#4
#반복문 예제 16
#소수구하기
#2부터 입력받은 수까지의 소수를 한줄에 7개씩 출력
n = int(input("찾을 범위 : "))

#while문
i = 2
line = 0
while i<= n: #i=2부터 input까지 i를 1씩 증가시키면서 반복문 돌림
    j = 2
    while j<= i:    #j=2부터 i까지 j를 1씩 증가시키면서 반복문 돌림
        if i%j == 0:
            break
        j += 1
    if i == j:  #이때 i와 j가 같으면 i가 처음으로 j에 의해서 나눠진것이므로 i를 출력
        print(i, end='\t')
        line = line+1
        if line==7:
            line=0
            print()
    i += 1

#for문
n = int(input("숫자 : "))
line=0
for i in range(2,n+1):
    for j in range(2,i+1):
        if i%j == 0:
            break
    if i==j:
        print(i,end='\t')
        line += 1
        if line==7:
            print()
            line=0
