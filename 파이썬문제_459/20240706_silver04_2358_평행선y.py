import sys
sys.stdin = open('input_2358.txt')
readl = sys.stdin.readline

n = int(readl())

 #x가 같거나 y가 같은 순서쌍 갯수찾기

# dot = [] #[(0, 0), (10, 10), (0, 10), (10, 0)]
# cnt = 0

x_dict = {}
y_dict = {}
for i in range(n):#4
    x, y = map(int, readl().split()) #0 0
          #set은 중복제거일때만 넣는다
    if x not in x_dict: # 1이 x_dict에 없으면 
        x_dict[x] = [y] # x_dict[1] = [1] {1:[1]}
    else:        # x in x_dict -> 1이 x_dict에 있으면
        x_dict[x].append(y) #1이 x에 있으면 y값을 dictionary추가
                #     x_dict = {1: [1]}
                # y_dict = {1: [1]}

                # x, y =1, 3
                # x_dict[1].append(3)
                # x_dict -> {1: [1, 3]}
     
#     x_dict -> {1: [1, 3]}

# y_dict -> {1: [1], 3: [1]} 
        
    if y not in y_dict: #1, 3  3이 ydict에 없으면
        y_dict[y] = [x]  #ydict[3] = [1] ->  y_dict -> {1: [1], 3: [1]}
    else:
        y_dict[y].append(x)
    # dot.append((x,y))

cnt = 0
for y_list in x_dict.values():
    if len(y_list) >= 2:
        cnt += 1
for x_list in y_dict.values():
    if len(x_list) >= 2:
        cnt += 1
print(cnt) 

# x = set()
# y = set()
# for x1, y1 in dot:  # 100,000 점의 갯수가 10만번이면, 10만번 * 10만번 해서 시간초과됨
#     for x2, y2 in dot:  # 100,000
#         if x1 == x2:
#             x.add(x1)
#         if y1 == y2:
#             y.add(y1)
# print(len(x) + len(y))
             