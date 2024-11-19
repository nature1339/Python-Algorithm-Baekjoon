import sys
sys.stdin = open('input_9575.txt')
readl = sys.stdin.readline

n = int(readl())

# group = [] #[set(100 1 10 100 1 1), set(3 53 53 53 53 53 53)
# #1588591를 10으로 나눈 몫은 158859 , 나머지는 1

# 158859  ... 1  몫,, 나머지
# 58
def lucky(num):
    while num != 0:
        num, r = divmod(num, 10) #10으로 나눈몫, 나머지
        # r = num % 10
        # num = num // 10
        if r != 5 and r != 8: # 나머지가 5나 8이 아니면 false
            return False #함수가 끝나고 밑에 count안하고 다음숫자로 넘어감
    return True # 몫이나 나머지가 5나 8이면 밑에 count + 1

for i in range(n):#2
    plus = set()
    
    n1 = int(readl())
    A = list(map(int, readl().split()))
    
    n2 = int(readl())
    B = list(map(int, readl().split()))
    
    n3 = int(readl())
    C = list(map(int, readl().split()))
    
    for i in A:
        for j in B:
            for k in C:
                plus.add(i + j + k)
    
    cnt = 0
    # print(plus)
    for num in plus:
        if lucky(num): #lucky가 true일때만
            cnt += 1
    
    print(cnt)