import sys
sys.stdin = open('input_1110.txt')
readl = sys.stdin.readline

n = readl().rstrip() #'26'  2+6 , n[0]='2'
# sum = 0
# l = [] #[8,]
# m = []
#sum += int(n[0])+int(n(1))
# if sum = 26: break

# 26 (n) -> 6 
# 2 + 6 = 8 (sum) -> 8
# 68 (new = prev) -> 가장오른쪽수(화살표) 8
# 6 + 8 = 14 (sum) -> 4
# 84 -> 4
# 8 + 4 = 12 -> 2
# 42


prev = n
cycle = 0
while True:  # prev - '26', '68', '84', ... 
    
    sum = int(prev[-1])
    if len(prev) > 1:
        sum += int(prev[0])
    sum = str(sum)
    new = prev[-1] + sum[-1]  # 68
    
    prev = new
    cycle += 1
    
    if new == n:  
        break

print(cycle)
# for i in range(99):
#   sum += int(n[i]) #8
#   #8+6
#   m.append(l[i]+n[i])
#   l.append(sum)      
#   if sum == n:  #26 ==처음수
#       break
# print(len(l)) #사이클의 수
  