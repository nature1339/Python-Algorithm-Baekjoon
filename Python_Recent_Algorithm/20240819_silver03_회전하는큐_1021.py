import sys
sys.stdin = open('20240819_silver03_회전하는큐_1021.txt')
readl = sys.stdin.readline

n = int(readl())
s = []

#정점(노드개수) 간선수(선) 시작점(

for i in range(1, n): #14
    command = readl().split() #n = 1일때  #push 1
                           #push X: 정수 X를 스택에 넣는 연산
    if command[0] == 'push': #push 1
       s.append(command[1])
    if command == 'top':   
       s.append('-1')
    print(s)
        
    