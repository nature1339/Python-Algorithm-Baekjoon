import sys
sys.stdin = open('input_10908.txt')
readl = sys.stdin.readline

a = [0]*26  #[0 0 0 0 0]  a[2] a[i]

for i in readl:  #baekjoon -> 1 -1 -1
    line = readl().rstrip  #baekjoon  
    k = line[i]
    a[ord('k')-ord('a')] =+1   #line[0] = b , ord('b')-ord('a') =  98-97 = 1 
    #[1,0,2,...]
    if i not in line:
        print('-1')
print(' '.join(map(str,a)))        
    
    