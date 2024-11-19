import sys
sys.stdin = open('input_2750.txt')
readl = sys.stdin.readline

n = int(readl().rstrip())


arr = []


for i in range(n):
    a = int(readl().rstrip())  #5
    arr.append(a)
arr.sort()    
print("\n".join(map(str, arr)))
    # print(a.reverse()) 
    # a.sort()
    # print(a)
    
    