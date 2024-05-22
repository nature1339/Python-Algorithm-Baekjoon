import sys
sys.stdin = open('input_5565.txt')
readl = sys.stdin.readline


TotalPrice = int(readl().rstrip())

noPrice_Sum = 0

for i in range(9):
    noPrice = int(readl().rstrip())
    noPrice_Sum += noPrice
print(TotalPrice-noPrice_Sum)