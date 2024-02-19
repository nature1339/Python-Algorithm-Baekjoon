import sys
sys.stdin = open('input_2153.txt')
n = input()

# 알파벳 인풋
# 그 알파벳을 숫자화 (아스키코드)
# 그 합을 소수인지 판별
# 소수면 프린트, 아니면 프린트

#a=97-96   a = 1, b = 98-96 = 2 , A = 65-27 = 38
sum = 0


for i in n: #UFRN # range는 정수만들어가야 -> 문자열 리스트로
    small = ord(i) - 96 # 97+0-96 = 1 a = 1, 97+1
    large = ord(i) - 38 # 65-38 = 27 = A  A=1
    # x = ord(i)
    # if ord('a') <= x <= ord('z'):
    
    # elif ord('A') <= x <= ord('Z'):
        
    if small <= 26: #97-96 = 1
        sum =+ small         
    elif large >= 27:      
        sum =+ large
    
if sum // 2 == 0 and sum // 3 == 0:
    print('It is not a prime word.')
else:     
    print('It is a prime word.')     