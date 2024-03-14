import sys
sys.stdin = open('input_5218.txt')
readl = sys.stdin.readline

# 5
# AAAA ABCD
# ABCD AAAA
# DARK LOKI
# STRONG THANOS
# DEADLY ULTIMO
n = int(readl())

# d = [] #2,4,3,2



for i in range(n):  # AAAA 
 
    d = [] #1,2,3,4
    before, after = readl().split() # AAAA ABCD
     
    for j in range(len(before)): #A,A,A,A,
        x = ord(before[j])
        y = ord(after[j]) 
        if y >= x:
            d.append(y-x)
        else:
            d.append((y+26)-x)            
        
    print(f'Distance: {d}' ,end='')# {d[i]}+{d[i+1]}')    
