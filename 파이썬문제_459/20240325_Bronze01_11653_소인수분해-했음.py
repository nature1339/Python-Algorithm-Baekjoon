import sys
sys.stdin = open('input_11653.txt')
readl = sys.stdin.readline

n = int(input()) #72
s = [] #약수(나누어 떨어지는것) 2,3
l = []
x = 0

for i in range(2, n+1):#72 를 나눈 약수(나누어떨어지는수),  중 소수만 모은것 ->소인수분해
    while n % i == 0: #나머지가 2,3,4,....72 나누어떨어지는것만, 2는 이미 해서 4는아님
        s.append(i)
        n //= i #몫  2//2 = 1  나누어떨어지는경우만
        
#     if n // i == 0:  # 72//2 * 36(6(2*3)*6(2*3)) = 2 * 2*3 * 2*3, 2*6*6=2*36
#         s.append(i) #인수중 소수 / 1과 자기자신만 이 아니면 remove
#     if s[i]//1 and s[i]//s[i]==0: #소수이면
#         l.append(i)  
# print(l)        
# print(s)
print('\n'.join(map(str, s))) #int -> 숫자형으로
        
    