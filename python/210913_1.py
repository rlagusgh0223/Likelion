#1
#반복문으로 2차원 리스트의 요소 모두 출력
#while 반복문 한번 사용하기
a = [[10, 20], [30, 40], [50, 60]]
i = 0
while i<len(a): #반복할때 리스트의 크기 활용(세로 크기)
    
    x, y = a[i] #요소 두개를 한꺼번에 가져오기
    print(x,y)  #10 20
                #30 40
                #50 60
    x = a[i]    #변수 하나에 요소 두개를 넣으면 리스트 형태로 받는다
    print(x)    #[10, 20]
                #[30, 40]
                #[50, 60]
    i += 1

#while 반복문 두 번 사용하기
a = [[10, 20], [30, 40], [50, 60]]
i = 0
while i < len(a):                   #1차원 리스트 요소 크기
    j = 0
    while j <len(a[i]):             #2차원 리스트 요소 크기
        print(a[i][j], end=' ')
        j += 1                      #2차원 리스트 인덱스를 1 증가시킴
    print()
    i += 1                          #1차원 리스트 인덱스를 1 증가시킴


#2
#for문과 while문 사용해서 화면에 표시
a = [[1,2,3], [5,6,7], [8,9,10], [12,13,14]]

#for문(이중 반복문) - 리스트의 요소가 바뀔 수 있으니 이게 좋은것 같다
for i in range(len(a)):         #range안써도 된다
    for j in range(len(a[i])):
        print(a[i][j],end=' ')
    print()
print()

#while문(단일 반복문)
i = 0
while i<len(a):
    x, y, z = a[i]
    print(x,y,z)
    i += 1


#3
#반복문으로 리스트 만들기
a = []                  #빈 리스트 생성
for i in range(10):
    a.append(0)         #append로 요소 추가
print(a)

#이중 for문으로 a = [[0,0], [0,0], [0,0]] 만들기
a = []
for i in range(3):
    aa = []
    for j in range(2):
        aa.append(0)
    a.append(aa)
print(a)

#리스트 표현식으로 2차원 리스트 만들기
a = [[0 for j in range(2)] for i in range(3)]
print(a)
#만약 for문을 한번만 하고 싶다면 리스트 자체를 곱할것
b = [[0]*2 for i in range(3)]
print(b)

#톱니형 리스트 만들기
#1차원적인 요소가 다른 리스트를 만들어보자
#[3,1,3,2,5] 활용하여 [[0, 0, 0], [0], [0, 0, 0], [0, 0], [0, 0, 0, 0, 0]]가 나오게 할 것
#아래는 입력을 받는식인데 문제에 맞지는 않지만 다양한 사항에 쓸 수 있을것 같아서 남겨둠
a = []
for i in range(5):
    n = int(input())
    aLine = []
    for j in range(n):
        aLine.append(0)
    a.append(aLine)
print(a)
#
a = [3,1,3,2,5]
for i in range(len(a)):
    aLine = []
    for j in range(a[i]):
        aLine.append(0)
    a[i] = aLine
print(a)
#============================모범답안=============================
a = [3,1,3,2,5]    #가로 크기를 저장한 리스트
b = [] #빈 리스트 생성
for i in a:    #가로 크기를 저정한 리스트로 반복
    aLine = []    #안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(i):    #리스트 a에 저장된 가로 크기만큼 반복
        aLine.append(0)
    b.append(aLine)    #리스트 b에 안쪽 리스트를 추가
print(b)

#리스트 표현식으로 작성
a = [[0]*i for i in [3,1,3,2,5]]
print(a)
#=================================================================

#2차원 리스트의 할당과 복사
#2차원 리스트를 만든 뒤 다른 변수에 할당하고,
#요소를 변경해보면 두 리스트에 모두 반영됨
a = [[10, 20], [30, 40]]
b = a
b[0][0] = 500
print(a)
print(b)
            #[[500, 20], [30, 40]]
            #[[500, 20], [30, 40]]
print()
a = [[10, 20], [30, 40]]
b = a.copy()    #리스트 a를 copy메서드로 b에 복사 한 뒤
b[0][0] = 500   #b의 요소를 변경해보면 리스트 a와 b에 모두 반영됨
print(a)        #2차원 리스트에는 copy만으로는 안된다
print(b)
            #[[500, 20], [30, 40]]
            #[[500, 20], [30, 40]]

#2차원 이상의 다차원 리스트는 리스트를 완전히 복사하려면
#copy 메서드 대신 copy 모듈의 deepcopy함수를 사용해야
import copy
a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)
b[0][0] = 500
print(a)    #[[10, 20], [30, 40]]
print(b)    #[[500, 20], [30, 40]]

#높이 2, 세로 4, 가로 3인 3차원 리스트 작성(리스트 표현식 사용)
a = [[[0 for k in range(3)] for j in range(4)] for i in range(2)]
print(a)
#출력시 줄바꿈 없이 붙어서 나온다
#[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]


#4
#문자열 조작하기

#문자열 바꾸기
#replace('바꿀 문자열', '새문자열')은 문자열 안의 문자열을
#다른 문자열로 바꿈
#문자열 자체는 변경하지 않으며 바뀐 결과를 반환함
print('Hello, world!'.replace('world', 'Python'))
#바뀐 결과를 유지하고 싶다면 문자열이 저장된 변수에
#replace를 사용한뒤 다시 변수에 할당해주면 됨
s = 'Hello, world!'
s = s.replace('world', 'Python')
print(s)

#문자 바꾸기
#translate는 문자열 안의 문자들을 다른 문자로 바꿈
#먼저 str.maketrans('바꿀문자''새문자')로 변환 테이블을 만듬
#그 다음에 translate(테이블)을 사용하면 문자를 바꾼 뒤 결과 반환
#아래는 a->1, e->2, i->3, o->4, u->5로 바꿈
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table)) #1ppl2

#문자열 분리하기
print('apple pear grape pineapple oragne'.split())
    #['apple', 'pear', 'grape', 'pineapple', 'oragne']
print('apple, pear, grape, pineapple, oragne'.split(', '))
    #['apple', 'pear', 'grape', 'pineapple', 'oragne']

#join(리스트)는 구분자 문자열과 문자열리스트의 요소를 연결하여 문자열로 만듬
print(' '.join(['apple','pear','grape','pineapple','orange']))
    #apple pear grape pineapple orange
print('-'.join(['apple','pear','grape','pineapple','orange']))
    #apple-pear-grape-pineapple-orange

#소문자를 대문자로 바꾸기
eng = 'python'.upper()
print(eng)          #PYTHON
print(type(eng))    #<class 'str'>
#대문자를 소문자로 바꾸기
eng = 'PYTHON'.lower()
print(eng)          #python
print(type(eng))    #<class 'str'>

#왼쪽 공백 삭제하기
Str = '  Python  '.lstrip()
print(Str)          #'Python  '
print(type(Str))    #<class 'str'>
#오른쪽 공백 삭제
Str = '  Python  '.rstrip()
print(Str)          #'  Python'
print(type(Str))    #<class 'str'>
#양쪽 공백 삭제
Str = '  Python  '.strip()
print(Str)          #'Python'
print(type(Str))    #<class 'str'>

#왼쪽의 특정 문자 삭제하기
Str =', python.'.lstrip(',.')
print(Str)  #' python.'
Str ='. python.'.lstrip(',.')
print(Str)  #' python.'
Str ='., python.'.lstrip(',.')
print(Str)  #' python.'
#오른쪽의 특정 문자 삭제하기
Str =', python.'.rstrip(',.')
print(Str)  #', python'
#양쪽의 특정 문자 삭제
Str =', python.'.strip(',.')
print(Str)  #' python'

#문자열을 왼쪽/오른쪽 정렬하기
#문자열을 지정된 길이로 만든 뒤 왼쪽/오른쪽으로 정렬하며
#남는 공간을 공백으로 채움
Str = 'python'.ljust(10)
print('|',Str,'|',sep='')  #|python    |
Str = 'python'.rjust(10)
print('|',Str,'|',sep='')  #|    python|
#문자열을 가운데 정렬하기
Str = 'python'.center(10)
print('|',Str,'|',sep='')  #|  python  |
#남는공간이 홀수가 된다면 왼쪽에 공백이 한칸 더 들어감

#메서드 체이닝
#메서드를 줄줄이 연결한다
#input().split()도 메서드 체이닝임
Str = 'python'.rjust(10).upper()
print('|',Str,'|',sep='')   #|    PYTHON|

#문자열 왼쪽에 0 채우기
#오른쪽에 채우는건 없다
Str = '35'.zfill(4)
print(Str)  #0035
Str = '3.5'.zfill(6)
print(Str)  #0003.5
Str = 'hello'.zfill(10)
print(Str)  #00000hello

#문자열 위치 찾기
#find('찾을문자열')은 문자열에서 특정 문자열을 찾아서
#인덱스를 반환하고, 없으면 -1을 반환
#왼쪽에서부터 문자열을 찾고, 여러개이면 처음 위치 반환
Str = 'apple pineapple'.find('pl')
print(Str)  #2
Str = 'apple pineapple'.find('xy')
print(Str)  #-1

#오른쪽에서부터 문자열 위치 찾기(rfind())
#lfind()는 없다
#문자열에서 처음 나오는 값을 오른쪽에서부터 계산
Str = 'apple pineapple'.rfind('pl')
print(Str)  #12
Str = 'apple pineapple'.rfind('xy')
print(Str)  #-1

#index('찾을문자열')은 왼쪽에서부터 특정 문자열을 찾아서
#문자열을 반환, 없으면 에러
#문자열이 여러개일 경우 처음 찾은 문자열의 인덱스 반환
#find 쓰는게 좋을것 같다
Str = 'apple pineapple'.index('pl')
print(Str)  #2

#오른쪽에서부터 문자열 위치 찾기
Str = 'apple pineapple'.rindex('pl')
print(Str)  #12

#문자열 개수 세기
#처음 나오는 pl의 수 세기
Str = 'apple pineapple'.count('pl')
print(Str)  #2
