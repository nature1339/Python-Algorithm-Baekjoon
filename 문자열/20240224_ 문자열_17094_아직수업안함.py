import sys
sys.stdin = open('input_17094.txt')
readl = sys.stdin.readline

n = int(readl()) #12
# 12
# 222eee222eee

d = {2:0, 'e':0}
line = readl().rstrip()

for i in range(n): #12번 #222eee222eee
    if line[i] == '2':
        d[2] += 1
    else:  # elif line[i] == 'e':
        d['e'] += 1

if d[2] > d['e']:
    print(2)
elif d[2] < d['e']:
    print('e')
else:
    print('yee')    
    # list = d.values  #[0,0,0]
    # if i == '2':
    #     list[0] += 1
    # elif i == 'e':   
    #     list[1] += 1
    # else:   
    #     list[2] += 1
        
        
        
