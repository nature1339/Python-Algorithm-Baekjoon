import sys
sys.stdin = open('input_17094.txt')
readl = sys.stdin.readline()

line0 = readl[1] #222eee222eee  
line1 = [0,0] #2, e

for i in line0: #222eee222eee  
    if i == 2:
        line1[0] += 1
    elif i == 'e':        
        line1[1] += 1

for j in line1:
    if line1[0]>line1[1]:
        print('2')          
    elif line1[0]<line1[1]:
        print('e')     
    elif line1[0]==line1[1]:
        print('yee')  
            
        
        
             
            