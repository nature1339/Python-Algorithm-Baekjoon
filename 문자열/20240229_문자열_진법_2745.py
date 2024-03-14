import sys
sys.stdin = open('input_2745.txt')
readl = sys.stdin.readline

n, b = readl().split()
b = int(b)

decimal = 0
for ch in n: #ZZZZZ  99999 16
    decimal *= b  #한칸 왼쪽으로 간다.
    if ord('0') <= ord(ch) <= ord('9'):  # ch.isdigit() == True: 숫자일때
        decimal += int(ch) #  오른쪽 새로들어온걸 +한다.
    else:  # 알파벳일 때
        decimal += 10 + ord(ch)-ord('A')
print(decimal)

# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
#ZZZZZ 36
# N     B
# N은 B진법수
# l = [35, 35, 35, 35, 35] #lenl = 5
# # A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
# sum = 0
# alphabet = [0]*26  #[0,0,0]
# for i in range(26):
#     alphabet[i] += 10+i #10+0, 10+1
    
# for i in range(len(readl)): #ZZZZZ  l = [35, 35, 35, 35, 35]
#   sum += 35**10**(len(readl)-1-i)  
#   print(sum)