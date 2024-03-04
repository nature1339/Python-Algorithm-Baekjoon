import sys
sys.stdin = open('input_5704.txt')
readl = sys.stdin.readline




while True: 
    line = readl().rstrip() #jackdawf loves my big quartz sphinx
    if line == "*":
       break
    d = [False]*26 
    for ch in line:         
        d[ord(ch) - ord('a')] = True  #65-65
        
     
    if all(d):
        print('Y')
    else:
        print('N')    
    