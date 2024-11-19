import sys
sys.stdin = open('input_1316.txt')
readl = sys.stdin.readline

n = readl()
prev = set('') #h a

for i in range(n):
    word = readl().rstrip() #happy
    for ch in word: #h a
        if ch == ch+1:
            prev = ch  #p == p
        else:
            
            
    