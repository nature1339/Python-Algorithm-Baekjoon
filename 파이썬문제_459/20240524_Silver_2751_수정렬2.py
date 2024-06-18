import sys
sys.stdin = open('input_2751.txt')
readl = sys.stdin.readline


n = int(readl().rstrip()) # 5

arr = [] #5 4 3 2 1  

for i in range(n): 
    num = int(readl().rstrip()) #5
    arr.append(num)
    
# arr = [int(readl()) for _ in range(n)]
# arr = [int(readl()) for _ in range(5)]

arr.sort() #1 2 3 4 5
print("\n".join(map(str, arr)))
    

    
    