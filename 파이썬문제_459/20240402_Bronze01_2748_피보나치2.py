import sys
sys.stdin = open('input_2748.txt')
readl = sys.stdin.readline


n = int(readl()) #10

fn = [0] * (n+1) # fn[0] ~ fn[n]  1~9 9개+0 = 10개
fn[0] = 0
fn[1] = 1
# 0 0 0 0 0 ....
# 0 1 
#     1 2 
for i in range(2, n+1):
    fn[i] = fn[i-1] + fn[i-2]

print(fn[n])

# fn[2] = fn[1] + fn[0]
# fn[3] = fn[2] + fn[1]
# fn[4] = fn[3] + fn[2]
# ...

# fn = [1,2,3]
# fn[5] = 5

# print(fn[n])
# fn = [0] * 90
# fn[0] = 0
# fn[1] = 1
# while n <= 90:
#     for i in range(n+1):           #0 1 1 2 3
#         fn[i+2] = fn[i+0]+fn[i+1] # f[2] = f[0]+f[1] = f[0+0]+f[0+1] = f[0]+f[1] = 0 +1
#                                 #f[3]=f[2]+f[1]= 2+ 1 , f[3] = 1+1=2
#         fn.append(fn[i]) 
        
# print(n)