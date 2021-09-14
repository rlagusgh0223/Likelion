#1
#앞의 8번과 이어진다
#계산 맞추기 게임
#random모듈을 이용해서 간단한 덧셈,뺄셈,곱셈 문제를
#임의로 만들어줌
#답을 입력하면 정답인지 오답인지 계산해서 점수 매김
#반복 5회
#eval함수 쓰고 make_question함수 작성할것
import random

def make_question():
    n1 = random.randint(-99,99)
    n2 = random.randint(-99,99)
    ope = random.randint(1,3)
    if ope == 1:
        x = str(n1)+'+'+str(n2)
    elif ope == 2:
        x = str(n1)+'-'+str(n2)
    elif ope == 3:
        x = str(n1)+'*'+str(n2)
    return x

cnt = 0
for i in range(5):
    x = make_question()
    print(x,'=',end=' ')
    n = int(input())
    
    #if eval(eval("x")) == n:   #결과는 같다
    if eval(x) == n:
        cnt += 1
        print("정답")
    else:
        print("오답")

print("총 5문제중 %d문제 맞췄습니다"%cnt)


#2
#인적사항 관리(등록, 수정, 삭제) 프로그램

#=============딕셔너리 입력===============
dic_student = {}
nNumber = input('학번')
strName = input("이름")
nScore = input("성적")
dic_student[nNumber] = [strName,nScore]
print(dic_student)
#=========================================

dic_student = {}

def dic(n):
    if n == 1:
        nNumber = input("학번을 입력하세요 : ")
        strName = input("이름을 입력하세요 : ")
        nScore = input("학점을 입력하세요 : ")
        dic_student[nNumber] = [strName,nScore]
        print("등록이 완료되었습니다")
    elif n == 2:
        number = input("원하는 학생의 학번을 입력하세요 : ")
        print("학번 :",number)
        print("이름 :",dic_student[number][0])
        print("학점 :",dic_student[number][1])
    elif n == 3:
        number = input("수정을 원하는 학생의 학번을 입력하세요 : ")
        print("학번 :",number)
        print("이름 :",dic_student[number][0])
        print("학점 :",dic_student[number][1])
        nInput = input("수정할 항목을 입력하세요(이름,학점) : ")
        if nInput == '이름':
            dic_student[number][0] = input("수정할 값 : ")
        elif nInput == '학점':
            dic_student[number][1] = input("수정할 값 : ")
        else:
            print("잘못된 입력")
    elif n == 4:
        number = input("삭제를 원하는 학생의 학번을 입력하세요 : ")
        print("학번 :",number,"이름 :",dic_student[number][0],"학점 :",dic_student[number][1],"가 삭제되었습니다")
        del dic_student[number]
    elif n == 5:
        print(dic_student)
        #print(person)    #5번 선생님 코드
        #for key in person.keys():
            #a, b = person[key]
            #print(key,'=',a,b)

while True:
    print('1. 인적사항 등록\t2. 학생 검색\t3. 학생 수정\n4. 학생 삭제\t5. 전체학생 보기\t6. 프로그램 종료')
    n = int(input("원하는 번호를 입력하세요 : "))
    if 1<= n <= 5:
        dic(n)
    elif n == 6:
        print("프로그램 종료")
        break
    else:
        print("잘못 입력 하셨습니다.")
    print()

#=======================================모범답안===========================================
person = {}

#======================함수======================
def make_data(nSchoolNo, strName, nScore):
    person[nSchoolNo] = [strName, nScore]

def search_student(nSchoolNo):
    if nSchoolNo in person:
        return person[nSchoolNo]
    else:
        return False

def change_info(nSchoolNo):
    nSel = input("항목을 선택(이름, 학점)")
    if nSel == '이름':
        strNewName = input("바꾼 후 이름")
        person[nSchoolNo] = [strNewName, person[nSchoolNo][1]]
    elif nSel == '학점':
        nNewScore = input("바꾼 후 학점")
        person[nSchoolNo] = [person[nSchoolNo][0], nNewScore]
    else:
        print("잘못된 입력")

def delete_student(nSchoolNo):
    del person[nSchoolNo]

def display_info():
    for key in person.keys():
        a, b = person[key]
        print(key,'=',a,b)
#==========================================
#=================메인코드=================
while True:
    n = int(input('''1. 인적사항 등록\t2. 학생 검색\t3. 학생 수정
4. 학생 삭제\t5. 전체학생 보기\t6. 프로그램 종료'''))
    if n == 1:
        nSchoolNo = input("학번을 입력하세요 : ")
        strName = input("이름을 입력하세요 : ")
        nScore = input("학점을 입력하세요 : ")
        make_data(nSchoolNo, strName, nScore)
    elif n == 2:
        nSchoolNo = input("원하는 학생의 학번을 입력하세요 : ")
        rtn = search_student(nSchoolNo)
        if rtn == False:
            print("존재하지 않는 학번")
        else:
            print("이름 = %s  학점 = %s"%(rtn[0],rtn[1]))
    elif n == 3:
        nSchoolNo = input("수정을 원하는 학생의 학번을 입력하세요 : ")
        if nSchoolNo in person:
            change_info(nSchoolNo)
        else:
            print("존재하지 않는 학번")
    elif n == 4:
        nSchoolNo = input("삭제를 원하는 학생의 학번을 입력하세요 : ")
        delete_student(nSchoolNo)
    elif n == 5:
        display_info()
    elif n == 6:
        print("종료합니다")
        break
    else:
        print("잘못된 입력")
#==========================================================================================


#3
#람다 표현식 사용하기
#함수를 간편하게 작성할 수 있다
#다른 함수의 인수로 넣을때 주로 사용

#람다 표현식은 람다에 매개변수를 지정하고
#뒤에 반환값으로 사용할 식을 지정
def plus(x):
    return x+10
#위의 함수와 같은 람다 표현식은 다음과 같다
rlt = lambda x:x+10    #매개변수 x하나를 받고 x에 10을 더해준다
print(rlt(10))      #20

#람다 표현식은 다음과 같이 쓸 수도 있다
print((lambda x:x+10)(1))   #11

#변수는 람다 표현식에 넣을 수 없다
#람다 표현식은 함수를 간단하게 만든건데
#변수를 넣으면 함수와 차이가 없다
#print((lambda x: y=10; x+y)(1))    <- 에러

#바깥에 변수를 만들어서 대입하는건 가능
y = 10
print((lambda x:x+y)(1))    #11

#람다 표현식을 인수로 사용하기
def plus_ten(x):
    return x+10
print(list(map(plus_ten, [1,2,3])))     #[11, 12, 13]
#함수를 사용하지 않고 람다 표현식으로 간단하게 사용 가능
print(list(map(lambda x: x+10, [1,2,3])))   #[11, 12, 13]

#람다 표현식에 조건부 표현식 사용하기
a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: str(x) if x%3 == 0 else x, a)))
    #a 리스트의 값 중 x를 3으로 나눴을때 나누어 떨어지는 수는 문자열로,
    #나누어 떨어지지 않는 수는 그대로 출력
    #[1, 2, '3', 4, 5, '6', 7, 8, '9', 10]

#람다 표현식에서 if-else는 :을 붙이지 않는다
#if만 쓰면 에러가 나며, elif는 사용할 수 없다
#식1 if 조건식1 else 식2 if 조건식2 else 식3
a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x+10, a)))
    #x가 1일때는 문자열로, 2일때는 실수로, 나머지는 0을 더해서 출력
    #['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]

#람다표현식이 알아보기 힘든 경우에는 그냥 함수로 만드는게 좋다
def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x+10

a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(f,a)))
#['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]

#map에 객체 여러개 넣기
#람다 표현식의 매개변수 개수에 맞게 반복 가능한 객체도
#콤마로 구분해서 넣어주면 된다
a = [1,2,3,4,5]
b = [2,4,6,8,10]
print(list(map(lambda x, y:x*y, a, b)))    #[2, 8, 18, 32, 50]

#lambda의 일반적 형태
#map이 반환하는 맵 객체는 이터레이터(값을 차례대로 꺼낼 수 있는 객체)
#라서 변수 여러개에 저장하는 언패킹이 가능
a = [1,2,3,4]
b = [2,4,6,8]
a_l = list(map(lambda x,y:x*y,a,b))
print('a_l = ',a_l)     #a_l =  [2, 8, 18, 32]

a2, b2, c2, d2 = map(lambda x, y: x*y, a, b)
print(a2, b2, c2, d2)   #2 8 18 32

a3, b3, c3, d3 = list(map(lambda x, y:x*y, a, b))
print(a3, b3, c3, d3)   #2 8 18 32

print(map(lambda x,y:x*y, a, b))    #<map object at 0x0000021E2AD7A5E0>
print(list(map(lambda x, y: x*y, a, b)))    #[2, 8, 18, 32]

a1, b1, c1, d2 = a_l
print(a1, b1, c1, d2)   #2 8 18 32
print(type(a1))     #<class 'int'>






