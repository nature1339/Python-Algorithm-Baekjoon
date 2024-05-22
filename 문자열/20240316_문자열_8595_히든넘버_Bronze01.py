import sys
sys.stdin = open('input_8595.txt')
readl = sys.stdin.readline
# 14
# ab13c9d07jeden
n = int(readl())  
line = readl().rstrip()    

cnt = 0
temp = 0
for ch in line: # ab13c9d07jeden2
    if ord('0') <= ord(ch) <= ord('9'): #ord(2)=50
        temp *= 10   #temp = 10
        temp += int(ch) # int(1) = 1 = temp = 1 , int(ch)=3, temp =13
    else: #문자가 나오면 , 숫자담긴 temp를 더하고 , temp= 0으로 비우는데,
          #문자가 안나오면 숫자담긴 temp를 못더하니, 밖에서 더한다.        
        cnt += temp # cnt = 13 + 9
        temp = 0 
    #처음에는 1일때, cnt = temp = 1 #13이 되야되는데 for문안에서 프린트하면 1이 프린트되서안됨    
cnt += temp  #temp   13 #if temp > 0 0은 숫자 더해도 그대로이니까 안씀  
     
print(cnt)
