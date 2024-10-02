import sys
sys.stdin = open('input_20240819_1439.txt')
readl = sys.stdin.readline

#11001100110011000001
s = readl()

count = 0
flag = 0
first = s[0] #0001100 s[0] = 0, s[1] = 0 s[2] = 0 s[3] = 1 s[4]=1  s[5]=0 s[6]=0
for i in range(len(s)-1): #7 #0001100 # 0~6까지 i
    if first != s[i] and flag == 0:  #if s[0] != s[0] and flag == 0: -> false
                        
        count += 1 
        flag = 1   #true이면 flag = 1
    if flag == 1 and first == s[i]:  # if flag == 1 이고 s[0] = s[0] 이면 flag = 0
        flag = 0
print(count)   

#s = 0
#if s[0] != s[0] and flag == 0: -> flase
#false 더이상 진행안함

#s = 1
# if s[0] ! = s[1] and flag == 0: --> true
# count += 1
# flag = 1
# if flag == 1 and first == s[0] == s[1]:
# flag = 0
# false

# s = 2
# if first = s[0] != s[2] and flag==0 : true
# count += 1
# flag = 1
# if flag == 1 and first==s[0]== 0 == s[2] = 0 
# flag = 0

