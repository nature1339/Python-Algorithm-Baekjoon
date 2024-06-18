import sys
sys.stdin = open('input_26069.txt')
readl = sys.stdin.readline

n = int(readl())
dance = set(['ChongChong']) # 총총이를 집합에 일단 넣어놓고 append로 반복문으로 추가함



for i in range(n):
    # d1, d2 = map(readl().split())  #jthis ChongChong   map은 문자열일때 굳이안써도split으로가능
    d1, d2 = readl().split()  #jthis ChongChong   
    if d1 in dance:
        dance.add(d2)
    if d2 in dance:
        dance.add(d1)

print(len(dance))