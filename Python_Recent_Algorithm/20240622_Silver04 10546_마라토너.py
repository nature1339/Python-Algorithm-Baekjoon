import sys
sys.stdin = open('input_10546.txt')
readl = sys.stdin.readline

n = int(readl())
all = []
finish = []
unfinish = []
finish_unfinish = []

# leo
# kiki
# eden

for i in range(n):
    name = readl().rstrip() # 모든 참가자
    all.append(name)
for j in range(n-1): #2  #완주한 참가자
    finish_unfinish = readl().rstrip()   
    if finish_unfinish not in all:  #모든 참가자 - 완주한 참가자
        print(finish_unfinish)
       

    
    
    