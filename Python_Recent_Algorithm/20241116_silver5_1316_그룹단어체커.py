import sys
sys.stdin = open('input_1316.txt')
readl = sys.stdin.readline

# 3
# happy
# new
# year

n = int(readl())
count = n

for i in range(n): #a a #직전문자랑 같냐
    word = readl().rstrip() #ccazzzzbb #split은 한줄에 여러 단어있을때
    
    temp = set() #a 
    prev = ''
    for ch in word: #문자니까 #ccazzzzbb
        
        if ch != prev: # ab            
            if ch not in temp:
                temp.add(ch)                
            else:
                count -= 1
                break                 
        prev = ch
print(count)