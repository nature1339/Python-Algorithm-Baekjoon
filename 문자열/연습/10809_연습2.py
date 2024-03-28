import sys
sys.stdin = open('input_10809.txt')
readl = sys.stdin.readline


# baekjoon
line = readl().rstrip()
pos = [-1] * 26   #[-1,0 ,-1,..]

for i, ch in enumerate(line): # baekjoon
    #i = 0, ch = b    #알파벳 위치
    if pos[ord(ch)-ord('a')] == -1:
        pos[ord(ch)-ord('a')] = i #pos[2]= i
    # pos[ord]
    # pos[ord(ch)-ord('a')] += 1  # pos[98-97] = pos[1] += 1
                #--> 알파뱃 갯수
    
   # pos[ord(b) - ord(a)] = pos[98-97]=pos[1]=+1
# print(''.join().pos(str,','))    
print(pos)
    
