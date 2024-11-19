import sys
sys.stdin = open('input_1978.txt')
readl = sys.stdin.readline

n = int(readl())
arr = list(map(int, readl().split())) #[1 3 5 7 ] 
# 4
# 1 3 5 7


sosu = 0

for m in arr: #소수 1과 자기자신으로만 나눠지는수
    if m == 1:
        continue
    
    is_prime = True
    for i in range(2, m):
        if m % i == 0:         #하나라도 나눠지면 소수가 아니다.#[1 3 5 7 ] 
            is_prime = False    #소수가 아니면 false라서 break
            break
    if is_prime:               #만약 소수면 count
        sosu += 1
        
    # if  x % 2 ==0 and x % 3 == 0: #arr[0] % 1 ==0 1%1=1..0
        
print(sosu)    
        

