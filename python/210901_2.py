#딕셔너리
#연관된 값을 묶어서 저장할 때 씀
#ex) 게임 캐릭터 생명력, 능력치, 공격력, 방어력
#딕셔너리 = {키1:값1, 키2:값2, 키3:값3}
fruits = {'apple':1000, 'banana':700, 'orange':1500, 'pineapple':2000}
print(type(fruits))
print(fruits)

#키 이름이 중복되면 마지막 값이 나온다
lux = {'health':490, 'mana':334, 'health':800, 'melee':500, 'armor':18.72}
print(lux['health'])    #800
print(lux)              #{'health': 800, 'mana': 334, 'melee': 500, 'armor': 18.72}

#키에는 문자열, 정수, 실수, 불, 자료형 쓸 수 있다
#값에는 모든 자료형 쓸 수 있다
x = {100:'hundred', False:0, 3.5:[3.5,3.5]}
print(x)

#빈 딕셔너리 만들기
dict1 = {}
dict2 = dict()
print(dict1)
print(dict2)

#딕셔너리 = dict(키1=값1, 키2=값2)
#dict메소드를 사용하면 문자열에 '' 안써도 된다
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
print(lux1)
#딕셔너리 = dict(zip([키1,키2],[값1,값2]))
#zip() : 리스트 값을 묶어줌
lux2 = dict(zip(['health','mana','melee','armor'],[490,334,550,18.72]))
print(lux2)
#딕셔너리 = dict([(키1,값1),(키2,값2)])
#리스트 안에 (키,값)형식의 튜플을 나열
lux3 = dict([('health',490),('mana',334),('melee',550),('armor',18.72)])
print(lux3)
#딕셔너리 = dict({키1:값1, 키2:값2})
#dict안에 중괄호로 딕셔너리를 생성
lux4 = dict({'health':490, 'mana':334, 'melee':550, 'armor':18.72})
print(lux4)

#딕셔너리는 특정 주제에 대해 연관된 값들을 모아둘 때 주로 사용
#ex)게임 캐릭터 능력치
lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
print(lux['health'])
print(lux['armor'])

#과일 이름을 입력하면 가격이 출력되는 프로그램
fruits = dict(apple = 1000, banana=700, orange=1500, pineapple=2000)
#fruits = {'apple':1000, 'banana':700, 'orange':1500, 'pineapple':2000}
order = input("과일이름을 입력하세요 : ")
print("선택한",order,"의 가격은",fruits[order],"원 입니다.")

#딕셔너리는 []로 키에 접근한 뒤 값을 할당함
lux = dict(health=490, mana=334, melee=550, armor=18.72)
lux['health'] = 2037
lux['mana'] = 1184
print(lux)          #{'health': 2037, 'mana': 1184, 'melee': 550, 'armor': 18.72}

#사과의 가격을 입력 받은 금액으로 변경하기
fruits = dict(apple = 1000, banana=700, orange=1500, pineapple=2000)
print("변경전 딕셔너리는",fruits,"입니다.")
nData = int(input("변경된 사과 가격을 입력하세요 : "))
fruits['apple'] = nData
print("변경된 딕셔너리는",fruits,"입니다.")

#딕셔너리는 없는 키에 값을 할당하면 해당 키가 추가되고 값이 할당됨
lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
lux['mana_regen'] = 3.28
print(lux)              #{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72, 'mana_regen': 3.28}
#딕셔너리는 없는 키에서 값을 가져오려고 하면 에러 발생
print(lux['attack_speed'])      #KeyError: 'attack_speed'

#딕셔너리에 키가 있는지 확인하기
#in연산자 사용
#키에대한 값을 할당할때 혹시 오타가 있을지도 모르니 확인할때 사용
lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
print('health' in lux)          #True
print('attack_speed' in lux)    #False
#not in
print('attack_speed' not in lux)    #True
print('health' not in lux)          #False

#사과, 바나나, 오렌지, 파인에플 가격이 0으로 초기화
#사용자로부터 각각의 과일가격을 입력 받아 과일 딕셔너리를 완성
fruits = dict(apple = 0, banana=0, orange=0, pineapple=0)
d1,d2,d3,d4 = map(int,input("사과, 바나나, 오렌지, 파인애플 값 입력 : ").split())
fruits['apple'] = d1
fruits['banana'] = d2
fruits['orange'] = d3
fruits['pineapple'] = d4
print(fruits)

#체력(health)과 이동속도(movement_speed)가 출력되게 만드시오
camille = {
   'health': 575.6,
   'health_regen': 1.7,
   'mana': 338.8,
   'mana_regen': 1.63,
   'melee': 125,
   'attack_damage': 60,
   'attack_speed': 0.625,
   'armor': 26,
   'magic_resistance': 32.1,
   'movement_speed': 340
}
print(camille['health'])
print(camille['movement_speed'])

#첫째줄에는 딕셔너리의 키, 둘째줄에는 값을 받는다
#한번에 합쳐서 딕셔너리 완성 후 출력
d1 = input().split()
d2 = map(float, input().split())
lux2 = dict(zip(d1,d2)) #zip([],[])인데 input().split()으로 입력받으면 어차피 list로 받는다
print(lux2)


#
#if 조건문
#pass가 없으면 if에 코드가 없을때 에러가 나온다(if문이 돌아가든 안돌아가든)
#pass는 if문을 우선 만들고 나중에 조건문을 채우려고 할때 쓴다
#x = 9
x = 10
if x == 10:
    #pass    #에러
print('test')

#들여쓰기가 맞지 않으면 에러 나온다
x=10
if x==10:
    print('x에 들어있는 숫자는')
        print('10입니다.')         #에러

x = 9
if x == 10:
    print('x에 들어있는 숫자는')
print('10입니다.')

#1개의 값을 받아들임
#받아들인 값이 7이면 '행운'이라고 화면에 표시
n = int(input())
if n==7:
    print('행운')

#1개의 값을 받아들임
#받아들인 값이 10이상이면 '크다'라고 화면에 표시
nData = int(input())
if nData>=10:
    print("크다")

#변수의 값이 10 이상이면 '10 이상입니다.'
#를 출력한 뒤 15면 '15입니다.', 20이면 '20입니다.'출력
x = 15
if x >= 10:
    print('10 이상입니다.')
    if x == 15:
        print('15입니다.')
    if x == 20:
        print('20입니다.')

#10이나 20을 입력받으면 출력
x = int(input())
if x == 10:
    print('10입니다.')
if x == 20:
    print('20입니다.')

#가격과 쿠폰 이름이 각 줄에 입력
#Cash3000쿠폰은 3000원, Cash5000쿠폰은 5000원 할인
#쿠폰에 따라 할인된 가격을 출력하는 프로그램
print("입력")
nData = int(input("값 입력 : "))
cash = input("쿠폰입력 : ")
if cash == 'Cash3000':
    nData -= 3000
if cash == 'Cash5000':
    nData -= 5000
print("결과")
print(nData)

#정수를 입력 받는다
#값이 짝수인지 홀수인지 화면에 표시
nData = int(input())
if nData %2 == 0:
    print("짝수입니다.")
if nData %2 == 1:
    print("홀수입니다.")

#정수를 입력받고
#10보다 큰지, 작은지, 같은지를 화면에 표시
nData = int(input())
if nData > 10:
    print("10보다 큽니다.")
if nData < 10:
    print("10보다 작습니다.")
if nData == 10:
    print("10과 같습니다.")
