import sys
sys.stdin = open('input_11650.txt')
readl = sys.stdin.readline


n = int(readl())  #5

jum = [] #(3, 4), (1,1)#리스트안에 뭐가들어가든 상관없음. tuple
# arr = list(map(int(input()) for i in range(n))) #arr=[]

for i in range(n):
    x, y = map(int,readl().split())  #3 4    1 1
    jum.append((x,y))
    
jum.sort()
for x, y in jum:
    print(x, y)
# print('\n'.join(map(str,jum))) -> 괄호랑 ''가 출력됨




    
    