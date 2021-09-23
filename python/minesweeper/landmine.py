import random
x = int(input("가로 : "))
y = int(input("세로 : "))
Inmap = [['0' for i in range(x)] for j in range(y)]     #가로*세로 곱한 값이 10 이상이어야 맵이 생긴다
nland = x*y//10             #지뢰의 개수
if nland == 0:              #맵이 너무 작을경우(가로*세로//10의 결과가 0인경우)
    nland = 1               #지뢰의 개수는 1
landmine=[0]*nland          #지뢰 좌표 입력할 변수
count = 0                   #찾은 지뢰의 개수 계산할 변수

i = 0                       #지뢰의 랜덤한 좌표를 만들기 위한 반복문
while i<nland:
    l1 = random.randint(0,nland)
    l2 = random.randint(0,nland)
    landmine[i] = l1,l2
    if nland>=2 and landmine[i-1] == landmine[i]:    #지뢰의 좌표가 중복될 경우 동작
        i -= 1    #i를 1 줄여서 다시 반복하여 중복된 좌표가 나오지 않도록 함
    i += 1
print(landmine)     #지뢰 위치 표시. 편의를 위해 만들었으나 실제론 없어야 될 코드

def search(X,Y):    #탐색함수
    uInput = X,Y    #사용자가 입력한 좌표값 리스트로 받음
    global Inmap    #본문에서 사용하는 변수 및 리스트 받음
    global count
    for i in range(nland):      #지뢰의 개수만큼 반복
        if uInput == landmine[i]:   #사용자가 입력한 좌표와 지뢰 좌표가 일치할 경우
            print("지뢰를 밟았습니다! 게임 오버")
            for j,k in landmine:    #모든 지뢰 위치 맵에 입력
                Inmap[j][k] = '★'
            for j in range(y):          #모든 지뢰 위치 표시된 맵 출력
                print(Inmap[j])
            count = nland       #count의 개수를 지뢰의 개수와 일치시켜 본문의 반복문 종료
            return count
        else:                   #사용자가 입력한 좌표와 지뢰 좌표가 다를 경우
            for j,k in landmine:    #지뢰 위치로부터 3,2,1칸 떨어져 있으면 그만큼 거리 표시
                                    #만약 더 가까이 있는 지뢰 위치가 사전에 입력되지 않았다면
                                    #현재 지뢰와 떨어져 있는 거리 맵에 입력
                   #사용자 편의를 위해 X,Y값은 1이 줄어있는 상태이므로 계산시 대입한다
                    #j는 세로, k는 가로 X,Y는 받을때부터 세로, 가로로 받았다
                if (j+3 == X and k == Y) or (j-3 == X and k == Y) or (j == X and k+3 == Y) or (j == X and k-3 == Y) or (j+3 == X and k+3 == Y) or (j-3 == X and k+3 == Y) or (j+3 == X and k-3 == Y) or (j-3 == X and k-3 == Y):
                    if Inmap[X][Y] != '2' or Inmap[X][Y] != '1':
                        Inmap[X][Y] = '3'
                elif (j+2 == X and k == Y) or (j-2 == X and k == Y) or (j == X and k+2 == Y) or (j == X and k-2 == Y) or (j+2 == X and k+2 == Y) or (j-2 == X and k+2 == Y) or (j+2 == X and k-2 == Y) or (j-2 == X and k-2 == Y):
                    if Inmap[X][Y] != '1':
                        Inmap[X][Y] = '2'
                elif (j+1 == X and k == Y) or (j-1 == X and k == Y) or (j == X and k+1 == Y) or (j == X and k-1 == Y) or (j+1 == X and k+1 == Y) or (j-1 == X and k+1 == Y) or (j+1 == X and k-1 == Y) or (j-1 == X and k-1 == Y):
                    Inmap[X][Y] = '1'
                else:               #지뢰와 인접하지도 않고, 지뢰 위치도 아니면
                    Inmap[X][Y] = '◎'   #지뢰가 없다는 표시 맵에 입력
                
def eliminate(X,Y):         #제거함수
    uInput = X,Y    #사용자가 입력한 좌표값 리스트로 받음
    global Inmap    #본문에서 사용하는 변수 및 리스트 받음
    global count
    for i in range(nland):  #지뢰의 개수만큼 반복
        if uInput == landmine[i]:   #지뢰의 좌표와 사용자의 입력 좌표가 같으면
            count += 1              #발견횟수 증가하고 발견했다고 표시
            print("지뢰 발견! 남은지뢰 : ",nland-count)
            Inmap[X][Y] = '●'
            if count == nland:      #모든 지뢰를 발견하면 게임 종료
                print("지뢰를 모두 찾았습니다. 게임을 종료합니다")
            return count
    print("틀렸습니다")      #제거를 시도했으나 지뢰가 없다면 틀렸다고 출력

while count < nland:                #지뢰를 전부 발견할때까지 돌아가는 반복문
    for i in range(y):              #지뢰찾기 맵 출력
        print(Inmap[i])
    choice = int(input("1: 탐색 / 2:제거"))     #탐색시 밟으면 게임오버, 찾으면 카운트 증가를 위한 조건문
    if choice == 1:
        X = int(input("가로 : "))
        Y = int(input("세로 : "))
        search(Y,X)             #탐색시 탐색함수를 호출하고 좌표를 넘김
    elif choice == 2:
        X = int(input("가로 : "))
        Y = int(input("세로 : "))
        eliminate(Y,X)          #제거시 제거함수를 호출하고 좌표를 넘김
    else:
        print("잘못된 입력")     #제시된 1이나 2가 아니면 잘못된 입력이라고 하고 다시 반복

