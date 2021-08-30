#사용자의 이름을 물어보고 이어서 2개의 정수를 받아서
#덧셈을 한 후 결과 출력하는 프로그램
nname = input("이름을 입력하시오 : ")
print(nname,"씨, 안녕하세요?")
print("파이썬에 오신 것을 환영합니다.")
nData1 = int(input("첫 번째 정수를 입력하시오 : "))
nData2 = int(input("두 번째 정수를 입력하시오 : "))
print(nData1,"과",nData2,"의 합은",nData1+nData2,"입니다.")

#
stadium = input("경기장은 어디입니까?")
winner = input("이긴팀은 어디입니까?")
loser = input("진팀은 어디입니까?")
mvp = input("우수선수는 누구입니까?")
score = input("스코어는 몇대몇입니까?")

print()
print("[기사내용]====================================")
print("오늘",stadium,"에서 야구 경기가 열렸습니다.")
print(winner,"과",loser,"은 치열한 공방전을 펼쳤습니다.")
print(mvp,"이 맹활약을 하였습니다.")
print("결국",winner,"이",loser,"를",score,"로 이겼습니다.")
print("==============================================")

#문자의 아스키코드 조회
print(ord('A'))
print(ord('1'))
print(ord('a'))

#특정 아스키코드에 해당하는 문자 조회
print(chr(45))
print(chr(97))
print(chr(75))

#
str = 'a'
encoded = str.encode('utf-8')
print(encoded)
encoded = str.encode('euc-kr')
print(encoded)
encoded = str.encode('ascii')
print(encoded)
print()
str = '가'
encoded = str.encode('utf-8')
print(encoded)
encoded = str.encode('euc-kr')
print(encoded)
encoded = str.encode('ascii')
print(encoded)

#
s1, s2 = input("두 수를 입력하세요 : ").split()
i1 = int(s1)
i2 = int(s2)
print("두 수의 합은 : ",i1+i2)

#입력받은 값을 '/'을 기준으로 분리
s1, s2 = input("두 수를 입력하세요 : ").split('/')
i1 = int(s1)
i2 = int(s2)
print("두 수의 합은 : ",i1+i2)

#
hour,minute,sec = input("시간을 hh:mm:ss 형태로 입력하세요 : ").split(":")
print("결과)")
print("시 :",hour)
print("분 :",minute)
print("초 :",sec)

#
nData1,nData2 = input().split()
nResult = int(nData1) + int(nData2)
print(nResult)

#
#map을 사용하여 정수로 변환하기
i1,i2,i3,i4,i5 = map(int, input("5개의 값 입력 : ").split())
print("합은",i1+i2+i3+i4+i5)

#
#국어,영어,수학,과학 점수 평균으로(실수) 출력
nKor, nEng, nMat, nSci = map(int,input("국어,영어,수학,과학 점수를 / 로 구분하여 입력하시오 : ").split('/'))
total = nKor+nEng+nMat+nSci
print(type(total))
favr = total/4
#정수를 정수로 나누면 정수가 나올수도,
#실수가 나올수도 있다
#그래서 자동으로 실수로 나온다
print(type(favr))
print(favr)

#
nKor, nEng, nMat, nSci = map(int,input("국어,영어,수학,과학 점수를 / 로 구분하여 입력하시오 : ").split('/'))
total = nKor+nEng+nMat+nSci
favr = total/4
print(int(favr))

#
#sep로 값 사이에 문자 넣기
print(1,2,3,sep=', ')   #1, 2, 3
print(4,5,6,sep=',')   #4,5,6
print('Hello', 'Python',sep='')   #HelloPython
print(1920,1080,sep='X')   #1920X1080

#
#줄바꾸기 해보기
print(1,2,3,sep='\n')
#탭으로 떨어트려 보기
print(1,2,3,sep='\t')

#
#파이썬 변수와 입력 사용해보기+출력
#출력할때는
#85+90+80+95
#총합은 350 입니다.
#로 출력할 것
nKor, nEng, nMat, nSci = map(int,input("국어,영어,수학,과학 점수를 입력하시오 : ").split())
total = nKor+nEng+nMat+nSci
print(nKor, nEng, nMat, nSci,sep='+')
print("총합은",total,"입니다.")

#
#\n도 문자이므로 print에 바로 넣어서 사용 가능
print('1\n2\n3')
#1
#2
#3
print('1\\n2\\n3')
#1\n2\n3

#
#줄 바꾸기 금지해보기
print(1,end=' ')
print(2,end=' ')
print(3)
#기본적으로 print의 end에 '\n'이 지정된 상태인데
#빈 문자열을 지정하면 '\n'을 지워주기 때
