import sys
sys.stdin = open('input_5218.txt')
readl = sys.stdin.readline

# 5
# AAAA ABCD
# ABCD AAAA
# DARK LOKI
# STRONG THANOS
# DEADLY ULTIMO

n = int(readl()) # 5

#  'A'=1, 'B' = 2, ..., 'Z' = 26. 
# A = ord(A) 97+i-96 ord(B)=97+i-96 = 97+1-96 =98-96=2
            #97+0-96=1 
            
d = 0       

x = 0
y = 0
for _ in range(n):
    l = [] #3,1,2,3
    before, after = readl().split()   #before =AAAA, after = ABCD
    for i in range(len(before)):   #AAAA ABCD
        # x(0)    y >= x = y - x
        
        x = ord(before[i])                
        y = ord(after[i])
        
        if y >= x:
            l.append(y-x)                       
        else: #y < x              
            l.append((y+26) - x)
    print("Distances:", " ".join(map(str, l)))  # {l[i]}+{l[i+1]}')    

    # print("Distances:", end=' ')#띄어쓰기로 연결해라
    # for d in l: #2 3 2 4
    #     print(d, end=' ')
    # print() #개행을 줘서 둘째줄에
    
   
        