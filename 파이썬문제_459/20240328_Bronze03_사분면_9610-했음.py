import sys
sys.stdin = open('input_9610.txt')
readl = sys.stdin.readline

n = int(readl())
Q1_cnt,Q2_cnt,Q3_cnt,Q4_cnt,AXIS_cnt = 0, 0, 0, 0, 0

for i in range(n):
    x, y = map(int, readl().split())
    
    if x > 0 and y > 0:        
        Q1_cnt += 1
    elif x < 0 and y > 0:        
        Q2_cnt += 1
    elif x < 0 and y < 0:        
        Q3_cnt += 1
    elif x > 0 and y < 0:        
        Q4_cnt += 1
    elif x == 0 or y == 0:        
        AXIS_cnt += 1
print(f'Q1: {Q1_cnt}')
print(f'Q2: {Q2_cnt}')
print(f'Q3: {Q3_cnt}')
print(f'Q4: {Q4_cnt}')
print(f'AXIS: {AXIS_cnt}')

    # line = readl().split() #0, 0
    # x, y, z = readl().split()
    # # 1 @ # % @ # ...
    # x, *op = readl().split()