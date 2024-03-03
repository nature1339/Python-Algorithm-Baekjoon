import sys
sys.stdin = open('input_11098.txt')
readl = sys.stdin.readline
# 2

# 3
# 10 Iversen
# 1000000 Nannskog
# 2000000 Ronaldinho

# 2
# 1000000 Maradona
# 999999 Batistuta
n = int(readl()) # 2

for i in range(n): #2
    
    k = int(readl()) # 3
    
    max_price = -1
    max_name = ''
    for j in range(k): #
        # line = readl().rstrip  #1000000 Nannskog
        temp, name = readl().split()  #x  #line
        temp = int(temp) #1000000
        
        if temp > max_price:
            max_price = temp
            max_name = name
    print(max_name)        
    

