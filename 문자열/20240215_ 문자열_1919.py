

# # input: 마지막 개행문자를 알아서 없애줌
# # sys.stdin.readline: 마지막 개행문자도 포함해서 입력
# input()  # slow
# sys.stdin.readline()  # fast

# # not recommended
# 입력을 전부 한번에 받아서 list에 넣음
# sys.stdin.readlines()

# aabbcc
# xxyybb

# line = [a,a,b,b,c,c]
# line = [x,x,y,y,b,b]

import sys
sys.stdin = open('input_1919.txt')
lines = sys.stdin.readlines()

# print(lines)

line0 = lines[0].rstrip()
line1 = lines[1].rstrip()

# abcccc
# cba
# aaaabbb
# aab

l = []   #bb   len(line[0])- len(l) = 4
        #bb   len(line[1])- len(m) = 4

# for line in lines:  #한줄씩 반복 [a,a,b,b,c,c] 

for i in line0: #[a,a,b,b,c,c] 의 요소가 다른 줄에 있으면
    if i in line1:  # line[0] = [a,a,b,b,c,c]
        l.append(i)    # line[1] = [xxyybb]

# aaab
# abbb

print(len(line0)- len(l)+len(line1)- len(l))
