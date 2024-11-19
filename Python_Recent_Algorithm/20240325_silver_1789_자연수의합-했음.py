import sys
sys.stdin = open('input_1789.txt')
readl = sys.stdin.readline

#3, 1+3+2 최대값? s = 134
#자연수 n
s = int(input())
# x1 + x2 + x3 +... + x_n = s , s= 10의 최소 n = 1, 문제는 최대n개, 서로다른n개
# s = 10 = 1+2+3+4 n의 최대값 = 4
# s = 6 = 1+2+3    n=3
# s = 7 = 1+2+4    n=3
# s = 8 = 1+2+5    n=3
# s = 9 = 1+2+6    n=3

# s = 5 = 1+4   n = 2

l = []
# l[0], l[1], l[2] , s = l[0]+l[1]+l[2] 
# for i in range(n): #3
    
n = 1
while (n * (n+1) // 2) <= s:
    n += 1
print(n-1)
    