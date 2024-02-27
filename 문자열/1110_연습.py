import sys
sys.stdin = open('input_1110.txt')
readl = sys.stdin.readline

#26  처음수(prev) n
#2+6 = 18    sum 십의자리수 *10 + 1의 자리수   일의자리*10 + 새로운수   
#68         new 새로운수 new = 
#6+8 = 14 

n = int(readl())
prev = n
cycle = 0

while True:
    sum = prev // 10 + prev % 10 # 18 = 18//10 = 몫 = 1 + 나머지 8  = 9
    new = (prev % 10)*10 + sum % 10
    prev = new
    cycle += 1
    
    if new == n:
        break
print(cycle)

