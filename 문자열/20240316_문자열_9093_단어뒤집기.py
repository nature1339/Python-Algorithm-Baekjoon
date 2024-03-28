import sys
sys.stdin = open('input_6996.txt')
readl = sys.stdin.readline

# 3
# blather reblath
# maryland landam
# bizarre brazier

n = int(readl())

for _ in range(n): #3
    x, y = readl().split() # blather reblath
    # if x == y[::-1] : # blather reblath = h
    if x == reversed(x) : # blather reblath = h
        print(f'{x} & {y} are anagrams')
    
    