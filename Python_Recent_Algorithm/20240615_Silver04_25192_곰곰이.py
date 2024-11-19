import sys
sys.stdin = open('input_25192.txt')
readl = sys.stdin.readline

n = int(readl())
cnt = 0
polite = set() #pjshwa chansol chogahui05 

for i in range(n):
    line =  readl().rstrip()  #ENTER
                              #pjshwa
    if line == 'ENTER':
        cnt += len(polite)
        polite = set() #집합초기화
        continue # Enter들어왔으면 뒤에거 안하고 다시 for반복
                 # Enter나오면 다음줄로 넘어가서 사람이 호출됨
    polite.add(line)
cnt += len(polite)
print(cnt)                          
                                        

