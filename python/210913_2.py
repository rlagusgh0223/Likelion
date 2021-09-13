#1
#'pl'을 찾아 해당 인덱스를 모두 표시
#문자열을 변경하지 말고 find와 슬라이스 문법 사용
Str = 'apple pineapple apple pineapple'
for i in range(4):
    ans = Str.find('pl')
    Str = Str[ans+2:]
    ans += len(Str[:ans+2])
    print(Str)
    print(ans)
print()

#================모범답안====================
strMy = 'apple pineapple apple pineapple'
nFind1 = strMy.find('pl')
print(nFind1)
newNFind = nFind1 + 2
strMy = strMy[newNFind:]
nFind2 = strMy.find('pl')
nFind2 = (newNFind) + nFind2
print(nFind2)

#반복문 사용
str1 = 'apple pineapple apple pineapple'
str2 = 'pl'

cnt = str1.find(str2)
print(cnt)
while str1[cnt+2:].find(str2) != -1:
    cnt = str1[cnt+2:].find(str2) + cnt + 2
    print(cnt)
#2
#12
#18
#28

#처음 cnt도 whlie 안에 넣기
str1 = 'apple pineapple apple pineapple'
str2 = 'pl'

cnt = -2
while str1[cnt+2:].find(str2) != -1:
    cnt = str1[cnt+2:].find(str2) + cnt + 2
    print(cnt)

#=============================================
#find 메소드를 모른다면
s = 'apple pineapple apple pineapple'
count = 0
a = 0
ina = [0,0,0,0,0,0,0,0,0,0]
while True:
    if count == len(s):
        break
    if s[count] == 'p' and s[count+1] == 'l':
        ina[a] = count
        a += 1
    count += 1
print('count :',a)
for i in range(len(ina)):
    if ina[i] == 0:
        break
    print(ina[i])

#for문을 이용하여 re.finditer(특정문자열, 원래문자열)을
#돌리면 순차적으로 a에 특정 문자열의 iterator값이 들어감
#a.start() : 시작위치 반환
#a.end() : 끝위치 + 1 반환
import re
str1 = 'apple pineapple apple pineapple'
str2 = 'pl'
for a in re.finditer(str2, str1):
    print(a.start(), a.end())


#2
#서식 지정자와 포매팅 사용

#서식 지정자로 문자열 넣기
#'%s' % '문자열'
print('I am %s.' %'james')
#%s는 문자열이란느 뜻이며 문자열을 바로 지정하지 않고 변수를 지정할 수 도 있다
name = 'maria'
print('I am %s.' % name)

#서실 지정자로 숫자 넣기
#숫자는 %d 넣고 %뒤에 숫자를 지정하면 됨
print('I am %d years old.' %20)
age = 17
print('I am %d years old.' %age)

#서식 지정자로 소수점 표현
#소수점 이하 자릿수를 지정하고 싶다면 f앞에 .(점)과 자릿수 지
print('%f' % 2.3)
age = 1.7
print('%.2f' % age)

#서식 지정자로 문자열 정렬
#%길이s
#%뒤에 숫자를 붙이면 문자열을 지정된 길이로 만든 뒤
#오른쪽으로 정렬하고 남는 공간을 공백으로 채움
print('|%10s|' % 'python')  #|    python|

#왼쪽정렬
#%-길이s
print('|%-10s|' % 'python')  #|python    |

#서식 지정자로 문자열 안에 값 여러개 넣기
#문자열 안에 값을 두 개 이상 넣으려면 %를 붙이고
#괄호 안에 값(변수)을 콤마로 구분해서 넣어줌
#괄호로 묶지 않으면 에러
print('Today i %d %s.' %(3, 'April'))   #Today i 3 April.
print('Today i %d%s.' %(3, 'April'))   #Today i 3April.

#format 메서드 사용하기
#서식지정자보다 간단한 문자열 포매팅 방법이 있다
print('Hello, {0}'.format('world!'))    #Hello, world!
print('Hello, {0}'.format(100)) #Hello, 100

#format 메서드로 값을 여러개 넣기
#{숫자}에 의해 뒤에 값은 순서를 변화시킬 수도 있다
print('Hello, {0} {2} {1}'.format('Python','Script',3.6))
    #Hello, Python 3.6 Script

#format메서드로 같은 값을 여러개 넣기
print('{0} {0} {1} {1}'.format('Python','Script'))
    #Python Python Script Script

#format메소드에서 인덱스를 생략하면 순서대로 들어간다
print('Hello, {} {} {}'.format('Python','Script',3.6))
    #Hello, Python Script 3.6

#인덱스 대신 이름을 지정할 수 있다
print('Hello, {language} {version}'.format(language='Python', version=3.6))
    #Hello, Python 3.6

#문자열 포매팅에 변수를 그대로 사용하기
#{}에 변수 이름을 지정하면 된다
#이때는 문자열 앞에 f를 붙인다(포매팅이라는 뜻)
language = 'Python'
version = 3.6
print(f'Hello, {language} {version}')
    #Hello, Python 3.6

#문자열 정렬하기
#인덱스 뒤에 :를 붙이고 정렬할 방향과 길이를 지정하면 됨
#< : 왼쪽으로 정렬
#> : 오른쪽으로 정렬
#{인덱스:<길이}.format(값)
print('|{0:<10}|'.format('python'))     #|python    |
print('|{0:>10}|'.format('python'))     #|    python|
#인덱스를 사용하지 않는다면 :과 정렬 방법만 지정해도 됨
print('|{:>10}|'.format('python'))     #|    python|
#인덱스를 쓰는 이유는 순서를 부여하기 위해서이다
print('|{0:<10}|{2:>10}|{1:<10}|'.format('python','abc',123))
    #|python    |       123|abc       |

#숫자 개수 맞추기
#{}를 사용할 때는 인덱스나 이름 뒤에 :를 붙이고
#03d처럼 0과 숫자 개수를 지정하면 됨
print('%03d' %1)        #001    3자리 중 %값
print('{0:03d}'.format(35))     #035
#특히 소수점 이하 자릿수를 지정하고 싶으면 .뒤에 자릿수를 지정
print('%08.2f' % 3.6)   #00003.60   8자리 중 소수점 2자리
print('{0:08.2f}'.format(150.37))   #00150.37

#채우기와 정렬을 조합해서 사용
print('{0:0<10}'.format(15))    #길이 10, 왼쪽으로 정렬하고 남는 공간은 0으로 채움
                                #1500000000
print('{0:0>10}'.format(15))    #길이 10, 오른쪽으로 정렬하고 남는 공간은 0으로 채움
                                #0000000015
print('{0:>10.2f}'.format(15))  #길이 10, 오른족 정렬하고 소수점 자릿수는 2자리
                                #     15.00

print('{0: >10}'.format(15))    #남는 공간을 공백으로 채움
                                #        15
print('{0:>10}'.format(15))     #채우기 부분을 생략하면 공백이 들어감
                                #        15
print('{0:x>10}'.format(15))    #남는 공간을 문자 x로 채움
                                #xxxxxxxx15


#3
#다음 소스 코드를 완성하여 파일 경로에서 파일명만 출력되게 하시오
#단, 경로에서 폴더의 길이가 달라지더라도 파일명만 출력할 수 있어야 한다
path = 'C:\\Users\\Edu\\AppData\\Local\\Programs\\Python\\Python36-32\\data.txt'
file = path.split('\\')#
filename = file[-1]#
print(filename)
#===========find 이용한 답안===============
filename = path[path.rfind('\\')+1:]

str1 = 'apple pineapple apple pineapple'
str2 = 'pl'

cnt = -2
while str1[cnt+2:].find(str2) != -1:
    cnt = str1[cnt+2:].find(str2) + cnt + 2
    print(cnt)


#4
#입력받는 문자열에서 'the'의 개수 출력
#'them', 'there'같은 문자는 안됨
str1 = input()
print(str1.count('the ') + str1.count('the,') + str1.count('the.'))



#5
#파이썬 함수 사용하기
#제일 중요!!!!!!

#5-1
#함수를 만든 부분 아래에서 함수를 적어주면 호출할 수 있다
#함수 만들기
def hello():
        print('Hello, world!')
        
#함수 호출
hello()

#5-2
#덧셈함수 만들기
def add(a,b):   #여기서 a,b를 매개변수라고 한다
    print(a+b)

add(10,20)

#5-3
#함수의 결과 반환
#return을 사용하면 함수 바깥으로 반환함
def add(a,b):
    return a+b

x = add(10,20)
print(x)
#print(add(10,20))도 가능

#5-4
#예제
#함수는 세개의 숫자를 곱해서 return
#메인 코드에서는 숫자 세 개를 입력 받음
#함수를 호출하여 결과를 화면에 표시
def cal(x,y,z):
    return x*y*z

i,j,k = map(int,input('곱할 숫자 3개 : ').split())
print(cal(i,j,k))

#5-5
#함수에서 값을 여러개 반환할 때는 return에 값이나
#변수를 ,로 구분해서 지정하면 된다
def add_sub(a,b):
    return a+b, a-b

x, y = add_sub(10,20)
print(x)
print(y)

x = add_sub(10,20)  #변수를 하나로만 하면 튜플로 나온다
                    #리턴에서 ()가 생략된 형태이기 때문이다 원래는 return (a+b,a-b)
                    #리스트로 출력하고 싶으면 []로 리턴하면 된다
print(type(x))  #<class 'tuple'>
print(x)    #(30, -10)
#
def add_sub(a,b):
    return [a+b, a-b]

x = add_sub(10,20)
print(type(x))  #<class 'list'>
print(x)    #[30, -10]

#5-6
#예제
#함수 세개 숫자 입력 받음
#세 숫자의 곱셈 결과와 덧셈 결과를 return하고 각각을 변수에 대입
#함수를 호출하여 그 결과를 화면에 표시
def malti(x,y,z):
    return x*y*z, x+y+z                 #곱셈, 덧셈 함수

a, b, c = map(int, input().split())     #입력받는 세 숫자
n1, n2 = malti(a,b,c)                   #함수 리턴값 대입
print("곱셈결과 :",n1)
print("덧셈결과 :",n2)
