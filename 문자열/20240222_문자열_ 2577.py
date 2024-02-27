import sys
sys.stdin = open('input_2577.txt')
readl = sys.stdin.readline

# 150
# 266
# 427



a = int(readl())
b = int(readl())
c = int(readl())


x = a*b*c  #121232113 #숫자는 반복안되서 str화
cnt = [0] * 10  #[0,0,0,0] 
for i in str(x):    
    cnt[int(i)] += 1 # x[0] x=1, cnt[0]=0
for i in cnt:    
    print(i)
