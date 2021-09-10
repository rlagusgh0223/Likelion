#1
#리스트에서 특정 값의 인덱스 구하기
a = [10,20,30,15,20,40]
print(a.index(20))

#a리스트 안에 20을 가지는 모든 indx를 구하시오
#첫번째 방법

a = [10,20,30,40,20,50,20,30,60,70,20]
b = []
while 20 in a:                  #20이 a리스트 안에 있는 동안 반복
    b.append(a.index(20))       #b리스트에 a리스트의 20이 처음 나오는 숫자 입력
    a.insert(a.index(20),0)     #a리스트에 20이 있는 자리의 앞에 0 입력
    a.pop(a.index(20))          #a리스트에 처음 있는 20 삭제
print(b)    #[1, 4, 6, 10]

#========================모범답안==========================
#다양한 방법이 있다.
a = [10,20,30,40,20,50,20,30,60,70,20]
result = []
while 20 in a:
    idx = a.index(20)
    result.append(idx)
    a[idx] = 'x'
print(a)    #[10, 'x', 30, 40, 'x', 50, 'x', 30, 60, 70, 'x']
print(result)    #[1, 4, 6, 10]
#==========================================================


#2
#count(값)은 리스트에서 값의 개수를 구함
a = [10, 20, 30, 15, 20, 40]
print(a.count(20))  #2
#reverse()는 리스트에서 요소의 순서를 반대로 뒤집음
a.reverse()
print(a)    #[40, 20, 15, 30, 20, 10]


#3
#리스트 정렬
a = [10, 20, 30, 15, 20, 40]
a.sort()                #오름차순
print(a)                #[10, 15, 20, 20, 30, 40]
a.sort(reverse=True)    #내림차순
print(a)                #[40, 30, 20, 20, 15, 10]


#4
#리스트 모든 요소를 삭제
a = [10, 20, 30]
a.clear()
print(a)    #[]
#del a[:]와 같이 시작, 끝 인덱스를 입력하여
#리스트의 원하는 요소를 삭제할 수 도 있음
a = [10,20,30]
del a[1:2]
print(a)    #[10, 30]


#5
#리스트를 슬라이스로 조작하기
#a[len(a):]는 시작 인덱스를 len(a)로 지정해서
#리스트의 마지막 인덱스보다 1이 더 크다
#리스트의 끝에서 시작하겠다는 뜻
a = [10, 20, 30]
a[len(a):] = [500]
print(a)    #[10, 20, 30, 500]


#6
#리스트의 할당과 복사
a = [0, 0, 0, 0, 0]
b = a           #리스트가 복사되는게 아니라 a와 b가 같은 리스트를 지칭하는거다
print(a is b)   #True
b[2] = 99
print(a)        #[0, 0, 99, 0, 0]
print(b)        #[0, 0, 99, 0, 0]
#===============================
a = [0, 0, 0, 0, 0]
b = a.copy()    #리스트 복사
print(a is b)   #False
b[2] = 99
print(a)        #[0, 0, 0, 0, 0]
print(b)        #[0, 0, 99, 0, 0]


#7
#인덱스와 요소를 함께 출력
#enumerate는 순서가 있는 자료형의
#index번호와 index값을 반환하는 함수
a = [38, 21, 53, 62, 19]
for index,value in enumerate(a):
    print(index, value) #0 38
                        #1 21
                        #2 53
                        #3 62
                        #4 19
#표시되는 인덱스 숫자는 내가 지정할 수 있다
for index, value in enumerate(a, start=10):
    print(index,value)  #10 38
                        #11 21
                        #12 53
                        #13 62
                        #14 19

#리스트 안에 특정값 모든 index 구해보기
#리스트에 20을 가지는 모든 인덱스
a = [10,20,30,40,20,50,20,30,60,70,20]
b = []
for index, value in enumerate(a):   #변수 하나만 주면 (x,x)로 변수 하나에 들어간다
    if value == 20:
        b.append(index)
print(b)        #[1, 4, 6, 10]


#8
#가장 큰 수와 작은 수 찾기
#위에서 쓴 리스트 함수는 쓰지 말고 오직 코드로만 구할것
a = [38, 21, 53, 62, 19]
max_val = a[0]
min_val = a[0]
for i in a:
    if i > max_val:
        max_val = i
    elif i < min_val:
        min_val = i
print(max_val,min_val)

#sort()이용해서
a = [38, 21, 53, 62, 19]
a.sort()
min_val = a[0]
a.sort(reverse=True)
max_val = a[0]
print(min_val, max_val)

#min, max함수 이용
a = [38, 21, 53, 62, 19]
print(min(a))
print(max(a))


#9
#sum 이용하여 합계 구하기
a = [10, 10, 10, 10, 10]
print(sum(a))


#10
#리스트 종합 예제
#빈 리스트 만들기
numbers=[]
#자연수 1부터 10까지 추가
for i in range(1,11):
    numbers.append(i)
#홀수 제거
#======================
#내가 짠건데 얼떨결에 됐다
#어차피 pop이 되니까 하나씩만 더하고
#다음으로 넘어가면 자연스럽게
#2씩 증가하는셈
#print(numbers)
#i = 0
#while i<len(numbers):
#    numbers.pop(i)
#    print(numbers)
#    i += 1
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#[2, 3, 4, 5, 6, 7, 8, 9, 10]
#[2, 4, 5, 6, 7, 8, 9, 10]
#[2, 4, 6, 7, 8, 9, 10]
#[2, 4, 6, 8, 9, 10]
#[2, 4, 6, 8, 10]
#======================
i = len(numbers) - 1
while i >= 0:
    if numbers[i] % 2 == 1:
        numbers.pop(i)
    i = i - 1
print(numbers)

#인덱스 0 자리에 20값 삽입
numbers.insert(0,20)
print(numbers)

#20을 찾아서 삭제
numbers.remove(20)    #맨 앞에것만 지운
print(numbers)

#4의 인덱스 찾기
print(numbers.index(4))

#numbers를 내림차순으로 출력
numbers.sort(reverse=True)
print(numbers)


#리스트에서 반복문과 if문 쓰기

a = [i for i in range(10)]
print(a)
b = list(i for i in range(10))
print(b)

a = [i for i in range(10) if i%2 == 0]
print(a)

b = [i+5 for i in range(10) if i%2 == 1]
print(b)


#구구단의 결과를 표시하는 리스트 만들어보기
a = [i*j for i in range(2,10) for j in range(1,10)]
#a = [i*j for i in range(2,10)
#             for j in range(1,10)]#이렇게 보면 이중 for문이랑 똑같다
print(a)
