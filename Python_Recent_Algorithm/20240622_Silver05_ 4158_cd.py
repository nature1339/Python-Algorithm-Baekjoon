import sys
sys.stdin = open('input_4158.txt')
readl = sys.stdin.readline

while True:
    n, m = map(int,readl().split()) # 3 3
    if n == 0 and m == 0:
        break
    sg = set([int(readl()) for _ in range(n)]) #n을 반복하면서 int(readl())를 한줄씩 입력받음
                                              #set([1 2 3])
    sy = set([int(readl()) for _ in range(m)]) #set([1 2 4])
    print(len(sg&sy)) # len(1 2) # if num in sg: #sg 가 10^6가 set으로 한번에 처리함
                      #sg,sy의 교집합의 길이

    # sg = []
    # sy = []
    # same = []

    # for i in range(n):
    #     num = int(readl().rstrip())
    #     # print(num)
    #     sg.append(num)
    # for j in range(m):    #10^6 을 각각 반복하면서 10^6승이라서 10^12승
    #     num = int(readl().rstrip())
    #     # print(num)
    #     if num in sg: #sg 가 10^6
    #         same.append(num)
    # print(len(same))        

    

