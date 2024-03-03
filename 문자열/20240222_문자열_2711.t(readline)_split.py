import sys
sys.stdin = open('input_2711.txt')
readl = sys.stdin.readline
# 4
# 4 MISSPELL
# 1 PROGRAMMING
# 7 CONTEST
# 3 BALLOON

n = int(readl()) #4
for _ in range(n): 
    x, line = readl().split() #공간을 기준으로 split 왼쪽은 x,오른쪽은 line에 담음
    x = int(x) #정수화 line의 x번째 4번째 x+1 = 
    
    print(line[:x-1] + line[x:])  #MI  SPELL 4-1번쨰 앞까지 :4-1 = :3 첨부터 2까지 + 4번째부터 끝까지
                                  #PROGRAMMING  x=1 line[:1-1]= line[:0] + line[1:]
