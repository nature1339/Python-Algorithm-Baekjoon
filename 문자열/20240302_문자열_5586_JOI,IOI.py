import sys
sys.stdin = open('input_5586.txt')
readl = sys.stdin.readline

#JOIJOI
#JOIOIOIOI
#cnt = 0 
# c = ['JOI', 'IOI']
line = readl().rstrip()  #JOIJOI len(line) = 6-2 = 4
cnt_joi, cnt_ioi = 0, 0
# c = readl().split('JOI,IOI') #c = JOI, IOI

# ABCDEFG
# ---
#  ---
#   --- 

for i in range(len(line)-2): #4
    if line[i:i+3] == 'JOI':
        cnt_joi += 1
    elif line[i:i+3] == 'IOI':
        cnt_ioi += 1
print(cnt_joi)    
print(cnt_ioi)     
    
# while True: #line= JOIJOI  #어디있는지 안알려주고 반복 #첨만 반복시작 첨 세글자만
#     ch = 'JOI'
#     if ch in line:
#         cnt_joi += 1
#     print(cnt, end'')        
        
        