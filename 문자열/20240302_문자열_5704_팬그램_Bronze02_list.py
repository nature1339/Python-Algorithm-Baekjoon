import sys
sys.stdin = open('input_5704.txt')
readl = sys.stdin.readline

 #jackdawf loves my big quartz sphinx  


 
while True:
    line = readl().rstrip() #jackdawf loves my big quartz sphinx
    if line == '*':
        break
    d = [False] * 26
    for ch in line: #[j,a,c,
        d[ord(ch) - ord('a')] = True  #65-65
        #d에 있으면 True
    
    if all(d): #all은 d가 모두 true인지 검사
        print('Y')
    else:
        print('N')        
        