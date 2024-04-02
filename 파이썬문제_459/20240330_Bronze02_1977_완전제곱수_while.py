import sys
sys.stdin = open('input_1977.txt')
readl = sys.stdin.readline

m = int(readl())
n = int(readl())

sum = min = 0

# 1 4 9 16 25 36 49  64 81 100 121 144 169 ...

x = 1
while (x**2) < m:  # 75 #m보다 크면 break
    x += 1
min = x ** 2

if min > n:  #m<= min <= n
    print(-1)
    sys.exit(0)
    
while (x**2) <= n:
    sum += x**2
    x += 1

print(sum)
print(min)


# for i in range(5):
#     print(i)

# i = 0
# while i < 5:
#     print(i)
#     i += 1