#1(210915_1의 #3에서 이어짐)
#텍스트 파일 입출력
#아래 코드로는 해당 행(5줄)만 출력할 수 있다
#r : 읽기
#w : 쓰기
#r+ : 읽기/쓰기
#a : 내용 추가

#읽어오기(한줄씩)
inFp = open("data_210915.txt","r",encoding='utf-8')#같은 폴더에 있으니까 처음에 좌표 안줘도 된다

print(type(inFp))       #<class '_io.TextIOWrapper'>   <-텍스트를 입출력하는 객체
inStr = inFp.readline()
print(inStr, end='')
inStr = inFp.readline()
print(inStr, end='')
inStr = inFp.readline()
print(inStr, end='')
inStr = inFp.readline()
print(inStr, end='')
inStr = inFp.readline()        #파일보다 읽어오는 줄이 더 많다면 그냥 안 읽어오고 끝난다
print(inStr, end='')    #내 파일에는 4줄만 있으니까 이 코드는 작동 안함

inFp.close()


#몇 줄인지 몰라도 다 읽는다는 코드로 입력
inFp = None     #타입이 정해져 있지 않은 객체 생성
inStr = ''      #문자열로 쓰일게 명확하니까 ''로 문자열 생성
inFp = open("data_210915.txt","r",encoding='utf-8')
while True:
    inStr = inFp.readline()
    if inStr == '':     #더 이상 읽을을 내용이 없음(EOF) - 엔터도 \n은 있다
        break
    print(inStr,end='')
inFp.close()    #open으로 권한 빌렸으니 close로 돌려줘야지 다른 사람도 사용할 수 있다


#readlines로 통으로 읽어오기
#['210915에서 쓰기 위한 파일\n', 'EfuCoding\n', '에듀코딩\n', '파이썬 Python\n', '\n', '출력테스트']
inFp = open('data_210915.txt','r',encoding='utf-8')
inList = []
inList = inFp.readlines()
print(inList)
inFp.close()

#위 내용 한 줄씩 출력
inFp = open('data_210915.txt','r',encoding='utf-8')
inList = []
inList = inFp.readlines()
for i in inList:        #inList에 리스트로 들어갔으니까 for로 받아서 하나씩 출력하게 해준다
    print(i,end='')     #리스트 자체적으로 \n을 받기때문에 여기서 엔터 안하게 해줘야 두줄 안뛴다
inFp.close()


#연습문제
#파일명을 입력 받으면 해당 파일을 읽어오는 프로그램
strData = input("파일명을 입력하세요 : ")
inFp = open(strData,'r',encoding='utf-8')
#inList = []             #생략해도 동작된다. 아랫줄에서 선언과 동시에 입력이 되니까
inList = inFp.readlines()
print("결과)")
for inStr in inList:
    print(inStr,end='')
inFp.close()


#파일 생성 및 내용 작성
outFp = None
outStr = ''

outFp = open('data2_210915.txt','w',encoding = 'utf-8')

while True:
    outStr = input("내용 입력 : ")
    if outStr != '':
        outFp.write(outStr+'\n')
    else:
        break

outFp.close()
print("---정상적으로 파일에 써졌음---")


#이미 만들어진 파일 복사
#data2_210915의 내용을 data2_210915_copy로 복사
inFp, outFp = None, None
outStr = ''

inFp = open('data2_210915.txt','r',encoding = 'utf-8')
outFp = open('data2_210915_copy.txt','w',encoding = 'utf-8')

while True:
    outStr = inFp.readline()
    if outStr != '':
        outFp.write(outStr)
    else:
        break

outFp.close()
inFp.close()

#또 다른 방법
inFp, outFp = None, None
outStr = ''

inFp = open('data2_210915.txt','r',encoding = 'utf-8')
outFp = open('data2_210915_copy.txt','w',encoding = 'utf-8')

inList = inFp.readlines()
for inStr in inList:
    outFp.write(inStr)

outFp.close()
inFp.close()

#또 다른 방법
inFp, outFp = None, None

inFp = open('data2_210915.txt','r',encoding = 'utf-8')
outFp = open('data2_210915_copy.txt','w',encoding = 'utf-8')

inList = inFp.readlines()   #파일 전부 읽어오기
outFp.writelines(inList)    #파일 전부 쓰기

outFp.close()
inFp.close()


#파일 암호화 및 암호 해동 프로그램
#ord() 함수 : 문자의 고유한 숫자를 알려줌
#chr() 함수 : 숫자에 해당하는 문자를 알려줌
while True:
    nData = int(input("암호 : 1, 복호 : 2, 종료 : 0"))
    if nData == 0:
        print("프로그램 종료")
        break
    
    elif nData == 1:
        str1 = input("입력 파일명 : ")
        str2 = input("출력 파일명 : ")
        inFp = open(str1,'r',encoding='utf-8')
        outFp = open(str2,'w',encoding='utf-8')

        while True:
            outStr = inFp.readline()
            if outStr != '':
                for i in outStr:
                    num = chr(ord(i)+100)
                    outFp.write(num)
            else:
                break
            
        inFp.close()
        outFp.close()
        
    elif nData == 2:
        str1 = input("입력 파일명 : ")
        str2 = input("출력 파일명 : ")
        inFp = open(str1,'r',encoding='utf-8')
        outFp = open(str2,'w',encoding='utf-8')
        while True:
            outStr = inFp.readline()
            if outStr != '':
                for i in outStr:
                    num = chr(ord(i)-100)
                    outFp.write(num)
            else:
                break
        inFp.close()
        outFp.close()
        
    else:
        print("잘못된 입력")

#================================모범답안===============================
#변수 선언
inFp, outFp = None, None
inStr, outStr ='',''
i = 0
secu = 0

#메인 코드 부분
secuYN = input("1:암호화 2:암호해석 중 선택 : ")
inFname = input("입력 파일명 : ")
outFname = input("출력 파일명 : ")

if secuYN == '1':
    secu = 100
elif secuYN == '2':
    secu = -100

inFp = open(inFname, 'r', encoding = 'utf-8')
outFp = open(outFname, 'w', encoding = 'utf-8')

while True:
    inStr = inFp.readline()
    if not inStr:
        break

    outStr = ''
    for i in range(0,len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)
        chNum = chNum + secu
        ch2 = chr(chNum)
        outStr = outStr + ch2

    outFp.write(outStr)

outFp.close()
inFp.close()
print("%s-->%s 변환 완료" %(inFname, outFname))
#=======================================================================


#cmd 파일 이용
#파이썬 돌리면 에러 나는거 정상이다
#cmd로 돌려야 확인된다
import sys

option = sys.argv[1]    #cmd창에서 실행시 첫번째 옵션 사용
                        #ex) python 210915_2.py -a

if option == '-a':  #cmd창에서 옵션 -a하면 타이핑한 내용이 메모장에 쓰임
    memo = sys.argv[2]    #cmd창에서 실행시 두번째 옵션 사용
                          #ex) python 210915_2.py -a asdfsgd <- 아래 코드는 이거 입력한다는 내용
    f = open('memo.txt','a')  #a는 이전에 쓰인 내용 다음에 추가된다
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':  #cmd창에서 옵션 -v하면 타이핑한 내용이 cmd창에 나옴
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)


#시분초 출력하는 코드
#import time
#print(time.strftime('%Y%m%d' + '' + '%H%S%M')) 연월일 시분초 출력

import sys
import time

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt','a')
    num = time.strftime('%Y%m%d'+'_'+'%H%S%M'+'  ')+memo
    f.write(num)     #변수 num에 입력받을 당시의 시간과 입력받은 내용을 합해서 파일에 작성
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)


