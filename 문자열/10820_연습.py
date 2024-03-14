import sys
sys.stdin = open('input_10820.txt')
readl = sys.stdin.readline


# This is String
# SPACE    1    SPACE
#  S a M p L e I n P u T     
# 0L1A2S3T4L5I6N7E8




# for i in range(len(line)): #4
      #i = 0   This is String
while True: 
    l, u, n, s = 0, 0, 0, 0
    line = readl().rstrip('\n')  #rstrip()하면 공백을 모두다 지우니 개행만 지우게함
    if line == '':
        break
    for ch in line:# This is String
        if ord('a') <= ord(ch) <= ord('z'):  #97  ord(T)   130
            l += 1
        elif ord('A') <= ord(ch) <= ord('Z'):    
            u += 1
        elif ord('0') <= ord(ch) <= ord('9'):  #int('49')      
            n += 1
        else:
            s += 1
             
    print(l, u, n, s)            
        