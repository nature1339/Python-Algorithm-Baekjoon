import sys
sys.stdin = open('input_2587.txt')
readl = sys.stdin.readline

sum = 0
mid = 0
avr = 0


# 10
# 40
# 30
# 60
# 30

# arr = [int(readl()) for _ in range(5)]

arr = []
for i in range(5):
    n = int(readl().rstrip()) #10
    arr.append(n)
    
    sum += n
    
# avg = sum(arr) // len(arr)

avr = sum // 5      # 10 40 30 60 30  avr
arr.sort()
mid = arr[2]
    
print(avr)
print(mid)
    # # sum += n    
# av = sum() // n    
# if av < mid < av + 1:      #5 4 3 2 1   2.5 <mid<3.5
#     print(av)
#     print(mid)