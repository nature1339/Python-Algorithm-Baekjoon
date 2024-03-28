# line0 = aabb len(line0) = 4
# line1 = bb   len(line1) = 2
# len(line0)-len(line1) = 최소개수
# aabbcc 
# xxyybb

import sys
sys.stdin = open('input_1919.txt')
readl = sys.stdin.readline

#공통부분
line0 = readl().rstrip()  # input()
line1 = readl().rstrip()  # input()

cnt_0 = [0] * 26  #[0,0,0,] #0 1 2 3 sum(line[i])
cnt_1 = [0] * 26            #1 3 5 4
 
for j in line0:  
   cnt_0[ord(j)-97] += 1 
for j in line1:    
   cnt_1[ord(j)-97] += 1    
      
sum = 0
for i in range(26):
    sum += abs(cnt_0[i]-cnt_1[i])           
print(sum)
    
    
    