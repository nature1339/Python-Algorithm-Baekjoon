import sys
sys.stdin = open('input_10809.txt')
readl = sys.stdin.readline

#baekjoon
line = readl().rstrip()  #baekjoon
pos = [-1]*26 #[-1, -1, -1]  [1,0,1...]

for i, ch in enumerate(line): #baekjoon 'b' # ch가 있으려면 enumerate가 있어야(range)
    if pos[ord(ch) - ord('a')] == -1: 
        pos[ord(ch) - ord('a')] = i  #pos[2] = 0  # i: line index, pos[x] - x: alphabet index            pos[2] = 0  [-1,0]
    # else:
    #     pass
   
   
print(' '.join(map(str,pos)))        
    
    

