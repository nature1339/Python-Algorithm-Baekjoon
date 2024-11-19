import sys
sys.stdin = open('input_25593.txt')
readl = sys.stdin.readline

num = int(readl()) #num으로 주수를 받고있어서 50주는 상관없
labor = {}  #이름:시간 #최대 100명은 딕셔너리에 100개들어가서 상관없음
            #  {A: 20, B: 50 }
time = [4,6,4,10]
#     - - - - - pangyo puang
# - - - - - sally boss
# - - - - - leonard brown
# - - - - - edward edward
    
for i in range(num): #4    
    for j in range(4):   #name = [- - - - - 'pangyo' ,'puang']
        names = readl().split() #리스트로 한줄에 담김
        for name in names:
            if name == '-':
                continue
                
            if name not in labor:
                labor[name]= time[j] #사람이름이 없을때 줄생김
            else:
                labor[name]+= time[j] # 사람이름 있을때 시간더함

labor_time = list(labor.values()) #[]근무시간모음 
# difference = max(labor_time)-min(labor_time)
if len(labor_time) == 0 or max(labor_time)-min(labor_time) <= 12: 
    #len(labor_time) == 0 ->-작대기만 있을때 , value error , 아무것도 없는데 max 하려해서
    print('Yes')
else:
    print('No')    
        
        
        