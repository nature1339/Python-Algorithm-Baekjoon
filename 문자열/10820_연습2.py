import sys
sys.stdin = open('input_10820.txt')
readl = sys.stdin.readline

# This is String
# SPACE    1    SPACE
#  S a M p L e I n P u T     
# 0L1A2S3T4L5I6N7E8


l,u,n,s = 0,0,0,0

#알파벳 소문자, 대문자, 숫자, 공백

while True:
    line = readl()[:-1]   # This is String   SPACE    1    SPACE
    if line == '':
        break
    for ch in line:   #This is String
        #i=0, ch=T : T = ord('ch') = ord('T') = 100
        if ord('A') <= ord(ch) <= ord('Z'): #  84-65 = 19
            u += 1
        if ord('a') <= ord(ch) <= ord('z'): #  84-65 = 19
            l += 1
        if ord('0') <= ord(ch) <= ord('9'): #  84-65 = 19
            n += 1
        else:
            s += 1
    print(l,u,n,s)             
        
    
