import sys
sys.stdin = open('input_25305.txt')
readl = sys.stdin.readline

n, k = list(map(int, readl().split())) #5 2 


candidate = list(map(int, readl().split())) #100 76 85 93 98
candidate.sort(reverse=True) # true이면 내림차순, 기본값이 오름차순
        
print(candidate[k-1])




    
    