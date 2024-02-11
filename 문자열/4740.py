
# 펠린드롬
# 입력 반복
# 한줄을 맨앞 맨뒤 순서바꾸고 출력
# 입력*** 이면 끝남

# import sys
# sys.stdin = open('4740.txt', 'r')
# lines = sys.stdin.readlines

# for i in line:   #line = AMBULANCE
#     if line[i] == len(line)-1
#     print(line)

# if line == ***:
        
import sys
readl = sys.stdin.readline 

while True:
    line = readl()[:-1]
    
    if line == '***':
        break

    print(line[::-1])        