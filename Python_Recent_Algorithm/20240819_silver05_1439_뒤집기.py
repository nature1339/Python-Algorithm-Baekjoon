import sys
sys.stdin = open('input_20240819_1439.txt')
readl = sys.stdin.readline

#11001100110011000001
s = readl()

count = 0
flag = 0
first = s[0]
for i in range(len(s)-1): #7 #0001100 # 0~6까지 i
    if first != s[i] and flag == 0:
        count += 1
        flag = 1
    if flag == 1 and first == s[i]:
        flag = 0
print(count)   


