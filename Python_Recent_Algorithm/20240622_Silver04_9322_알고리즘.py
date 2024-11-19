import sys
sys.stdin = open('input_9322.txt')
readl = sys.stdin.readline

n = int(readl()) 
# print(n)

original = []

for i in range(n): #2
    m = int(readl().rstrip()) # 4   #int안하면 / 개행문자나옴
    # print(m)    
    n1 = readl().split()       # A B C D  제1공개 #원래 문자열이니까 map필요없음
    n2 = readl().split()       # D A B C  제2공개
                               # B A P C  평문
    password = readl().split() # C B A P  암호 # 문자열이라서 split하면 list필요없음
    
    # rule = [] # 1 2 3 0
    # for x in n1: # n1의 문자들이 n2에 몇번째 인덱스인지?
    #     rule.append(n2.index(x)) # n1의 A가 n2의 몇번째인지 A -> 1번째
    rule = [n2.index(x) for x in n1] #n1을 반복하면서 n2의 몇번째인지
    # print(rule)
    
    # origin = []
    # for idx in rule: # 1 2 3 0  #case2일때  rule = [2 1 0]
    #     origin.append(password[idx]) # C B A P  #password[1] = B -> origin[B,A,P,C]
                                       #case 2 일때 password[2] = we -> origin[we, attack,tommorow]
    origin = [password[idx] for idx in rule]
    print(' '.join(origin))
    # password[i] = password[i-1] #B A P C      
    # original = password
    # print(original)
