import sys
sys.stdin = open('input_5363.txt')
readl = sys.stdin.readline

# 4
# I will go now to find the Wookiee
# Solo found the death star near planet Kessel
# I'll fight Darth Maul here and now
# Vader will find Luke before he can escape

n = int(readl()) # 4
l = []

for _ in range(n):      #문자열을 리스트화
    l = readl().strip()  # ['I', 'will', go now to find the Wookiee]
    l[0],l[1] = l[-2],l[-1]
    print(l)
        