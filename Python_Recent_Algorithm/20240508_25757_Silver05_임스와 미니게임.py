import sys
sys.stdin = open('input_25757.txt')
readl = sys.stdin.readline

n, game = readl().split()  #7 Y
n = int(n)

played = set() # 한번에 찾기 위해서 set 자료형 이용


if game == 'Y': 
    need = 2
elif game == "F":      
    need = 3
elif game == "O":
    need = 4

cnt = 0
temp = set()
for i in range(n):#7
    x = readl().rstrip() #lms0806
    # member.append(x)
    
    if x in played: #play한적있으면 건너뛰려고 ---> 여기서 빨리하려고 set 씀
        continue
    # else:
    temp.add(x) #플레이하지 않은 사람
    if len(temp) + 1 == need: # 임스와 같이할사람을 추가해서 need에 맞으면
        cnt += 1   # 게임수가 늘어남. 한사람이랑 하면. 다른게임 f=3, o=4
        
        played |= temp  #played = played | temp (합집합) #add의 의미 #합집합은 한번만씀. 중복만 한번만 쓴다.
        temp = set() #[] 빈리스트 의미 --> 빈집합을 만드는것
    
print(cnt)        
        
    