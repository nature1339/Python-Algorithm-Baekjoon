import sys
sys.stdin = open('input_10833.txt')
readl = sys.stdin.readline

n = int(readl().rstrip()) #학교수
# 5
# 24 52
# 13 22
# 5 53
# 23 10
# 7 70


total_left = 0
# left_list = []

for i in range(n): #5 학교수
    # total_left = 0
    st, ap = map(int, readl().split())   #학생 수, 배정된 사과 개수 ->24 52
    
    # left = ap % st
    left = ap
    for i in range(1, ap+1):
        if st * i <= ap: #24*2 <= 52
                                #  ap st*i 
            left = ap - (st*i)  #52-24*2 = 52-48=4
            # print(st, ap, i, left)           #22-13*1 = 22-13=9
                                # 53-5*10=3 
    # left_list.append(left)
    # print(st, ap, left)
    total_left += left     
    
print(total_left)    
# print(left_list)    

