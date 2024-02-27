import sys
sys.stdin = open('input_2495.txt')
readl = sys.stdin.readline

for _ in range(3):
    line = readl().rstrip()
    #[1 7 7 7 2 3 4 5]
    max_len = 1
    temp_len = 1
    for i in range(7):
        if line[i] != line[i+1]:
            max_len = max(max_len, temp_len)
            temp_len = 1
        else:
            temp_len += 1
    max_len = max(max_len, temp_len)
    print(max_len)
        
    
# 12345123
# 17772345
# 22233331  
# cnt_0 = [0] * 8 # [0 0 0 0 0 0 0 0]
#                  #[1 7 7 7 2 3 4 5]
                 
# l = []
                 
# for i in readl: # 12345123
#     if readl[i]:   #if 7
#         cnt_0[i] += 1 # cnt_0[0] = 1   cnt_0[1] = 1
#     if cnt_0[i+1] == cnt_0[i]:
#         l.append(cnt_0[i])
# print(len(l))                
    
