import sys
sys.stdin = open('input_5355.txt')
readl = sys.stdin.readline

n = int(readl()) #3

# x == '@': # *3
# y == '%': # + 5
# z == '#': # -7
result = 1
    
for i in range(n): #3
    line = readl().split() # '3','@', '%'
    num = float(line[0])
    for ch in line[1:]: # '3','@', '%'    3*3+5
        if ch == '@':
            num *= 3
        elif ch == '%':
            num += 5
        elif ch == '#':
            num -= 7
        # result *= line[j]  #3*3+5  j[i]j[i+1]j[i+2]
    print(f'{num:.2f}')
   