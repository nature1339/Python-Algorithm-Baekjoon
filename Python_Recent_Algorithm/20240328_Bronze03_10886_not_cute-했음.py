import sys
sys.stdin = open('input_10886.txt')
readl = sys.stdin.readline

n = int(readl()) #n 은 홀수
cnt_1, cnt_0 = 0, 0
for i in range(n):
    line = int(readl().rstrip()) #1
    if line == 1:
        cnt_1 += 1 #1이 나온 횟수라 1을 더함
    else: 
        cnt_0 += 1 #0이 나온횟수라 1을 더함   
if cnt_0 > cnt_1:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")        
    
    

