import sys
readl = sys.stdin.readline

while True:
    line = readl()[:-1] #한줄의 끝문자의 개행문자 제거
    
    if line == "***":
        break
    
    print(line[::-1])    


    
    