import sys
sys.stdin = open('input_8958.txt')
readl = sys.stdin.readline

n = int(readl())


for i in range(n): 
    x = readl().rstrip() #OOXXOXXOOO
    con = sum = 0
    for ch in x:
        if ch == 'O':
            con += 1 # 연속된 0
            sum += con #sum은 연속된거 전부합
        else:
            con = 0            
    print(sum)            
        