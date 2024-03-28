import sys
sys.stdin.readline = open('input_2675.txt')
readl = sys.stdin.readline

n = int(readl())
line = readl().split() #3 ABC
s = [] #[A,A,A,BBBCCC]
# 2
# 3 ABC
# 5 /HTP

for i in range(n): # 
    for j in range(1, int(line[0])): #line = '3', 'ABC'
        s.append(line[i][j])
        #J = 0일때 line[1][0] #A  s = [A,
        #j = 1     line[1][1] #A  s = [A,A]
        #J = 2     line[1][2] #A  s =[A, A, A] 
print(''.join(s))        