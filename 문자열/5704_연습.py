import sys
sys.stdin = open('input_5704.txt')
readl = sys.stdin.readline

al = [False]*26 #a:False, b:False,.... true이면 알파벳에 있는것


while True: 
    line = [] #초기화
    line = readl().rstrip() #jackdawf loves my big quartz sphinx
    for i in line:
        if line[i] not in al:   # al 에 없으면 true         
            print('Y')
        else:
            print('N')    
    if line == "*":
        break