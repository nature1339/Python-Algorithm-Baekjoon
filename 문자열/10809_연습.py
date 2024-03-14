import sys
sys.stdin = open("input_10809.txt")
readl = sys.stdin.readline

pos = [-1]*26  #[1,0,-1,-1,2]

line = readl().rstrip()

for i, ch in enumerate(line): #baekjoon
   #  a[i] = -1   #a[7] = []    
   if  pos[ord(ch)-ord('a')] != -1:  # pos[ord(ch)-ord('a')] = pos[2] != -1
         continue
   pos[ord(ch)-ord('a')] = i     #a[ord(b)-ord('a')]=0 a[98-97]=a[1]=0         
     #a[ord(b)-ord('a')] =a[98-97]=a[1] = 0
  
print(' '.join(map(str,pos)))   #a를 문자열로 공백을 기준으로 옆으로 출력                  
