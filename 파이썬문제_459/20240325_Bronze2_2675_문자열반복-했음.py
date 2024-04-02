import sys
sys.stdin = open('input_2675.txt')
readl = sys.stdin.readline

n = int(readl())


# 2
# 3 ABC
# 5 /HTP
for i in range(n): # 
    s = [] #[A,A,A,BBBCCC] #다음줄에 갔을때 빈 리스트야해서
    it, string = readl().split() #line = [3, ABC], [5 ,/HTP]
                           #line = [[3, ABC],[5 ,/HTP] ] -> 이게 아님, 단순반복임
    # print(len(line[1]), int(line[0]))
    it = int(it)
    for ch in string: #ABC
        s.append(ch * it)
        # for j in range(it):
        #     s.append(ch)
    # for j in range(1, int(line[0])): #line = '3', 'ABC'
    #     s.append(line[1][j])
        #J = 0일때 line[1][0] #A  s = [A,
        #j = 1     line[1][1] #A  s = [A,A]
        #J = 2     line[1][2] #A  s =[A, A, A] 
    print(''.join(s))        #i=0일때 출력, ...