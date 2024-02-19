import sys
sys.stdin = open('input_2153.txt')

# 에라토스테네스의 체
N = 52 * 20
chk = [True] * (N+1)
for i in range(2, 33):
    if chk[i] == True:
        j = i + i
        while j <= N:
            chk[j] = False
            j += i

n = input()

# 알파벳 인풋
# 그 알파벳을 숫자화 (아스키코드)
# 그 합을 소수인지 판별
# 소수면 프린트, 아니면 프린트

#a=97-96   a = 1, b = 98-96 = 2 , A = 65-27 = 38
sum = 0


for i in n: #UFRN # range는 정수만들어가야 -> 문자열 리스트로
    # small = ord('i') - 96 # 97+0-96 = 1 a = 1, 97+1
    # large = ord('i') - 38 # 65-38 = 27 = A  A=1
    x = ord(i)
    if ord('a') <= x <= ord('z'):
        sum += x - ord('a') + 1  #97+1 = 98,  x = ord(a) = 97  , 97-ord('a')=97  , 97-97 = 0+1 , 1 , a일때 sum = 1  => 소문자의 합구하려는것
    elif ord('A') <= x <= ord('Z'):
        sum += x - ord('A') + 27    #=> 대문자의합

    
if chk[sum]:
   print('It is a prime word.')
   
# if sum // 2 == 0 and sum // 3 == 0:  #5%2 ==2 #소수가아닐
#     print('It is not a prime word.')
else:     
    print('It is not a prime word.')   