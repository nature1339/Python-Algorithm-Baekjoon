import sys
sys.stdin = open('input_1356.txt')
readl = sys.stdin.readline

line = readl().rstrip()  # "4567"
l = [] # 
k = []

ans = 'NO'
for i in range(1, len(line)): #5 6 7
    # line[:i]  # "4"
    # line[i:]  # "567"
    
    result1 = 1
    for x in line[:i]: #4
        result1 *= int(x)
    
    result2 = 1
    for y in line[i:]:  # "567"
        result2 *= int(y) #5*6*7
    
    if result1 == result2:
        ans = 'YES'
        break
print(ans)

# for i in line//2: #12 2.5 345
#     line[i] * line[i+1:]# line[0] line[:1]
#                           #line[1]
    
    
# for i in line:
#     k.append(l[i][0]*l[i][1]) #l[0]
#     if k[i] == k[i+1]:
#         print('Yes')
#     else:
#         print('No')        