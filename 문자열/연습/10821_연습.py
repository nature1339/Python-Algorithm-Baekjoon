import sys
sys.stdin = open('input_10821.txt')
readl = sys.stdin.readline

# 10,20,30,50,100 문자열

line = readl().split(',')
print(len(line))
