import sys
sys.stdin = open('input_1373.txt')
readl = sys.stdin.readline

x = int(readl(), 2)  # 11001100 -> 11001100 204
print(f'{x:o}')

 


# 11001100   len(readl) = 8
# sum = 0

# for i in readl: #11001100
#     sum += 8 ** (len(readl)-1)  #1  len(realdl) = 8-1 = 8**7   314
# print(sum)
