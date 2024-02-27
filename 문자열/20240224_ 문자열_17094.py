import sys
sys.stdin = open('input_17094.txt')
readl = sys.stdin.readline

n = int(readl()) #12


d = {2:0, 'e':0, 'yee':0}

for i in range(n): #12번 #222eee222eee
    if i == '2':
        d[2] += 1
    elif i == 'e':   
        d['e'] += 1
    else:   
        d['yee'] += 1
        
        
    
    if cnt_2 > int(cnt_e):
        print('2')
    if int(cnt_e) > cnt_2:
        print('e')
    if cnt_2 == int(cnt_e):
        print('yee')
        
