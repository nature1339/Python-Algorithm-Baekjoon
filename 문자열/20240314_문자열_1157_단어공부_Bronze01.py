import sys
sys.stdin = open('input_1157.txt')
readl = sys.stdin.readline

u = [0]*26   # u = [0,3,0,1,0]
line = readl().rstrip() #Mississipi

for ch in line.upper(): #MISSISSIPI
    u[ord(ch)-ord('A')] += 1 #u[M] +=1

ans = '?'
max_cnt = 0
for i in range(26):
    if u[i] > max_cnt: #3 > 0
        max_cnt = u[i] # max_cnt = 3
        ans = chr(ord('A') + i) #= Z
# print(max(u))  chr(u[1]) chr(3)
    
    
#     if ord('A') <= ord(ch) <= ord('Z'):  # ord('M') = 77-65= 12
#         u[ord('M')-ord('A')] += 1   #u[2]=u[2]+1
# if max(u)>=2:
#     print('?')
# else:
#     print(max(u))    

        
        