import sys
readl = sys.stdin.readline

line0 = readl().rstrip()  # input()
line1 = readl().rstrip()  # input()

# n = int(readl())  # 5
# for _ in range(n):
#     line = readl().rstrip()  # input()

cnt_0 = [0] * 26  #[1, 1, ...]
cnt_1 = [0] * 26
for ch in line0:
    cnt_0[ord(ch)-ord('a')] += 1
    # cnt_0[1]  += 1
for ch in line1:
    cnt_1[ord(ch)-ord('a')] += 1

sum = 0
for i in range(26):
    sum += abs(cnt_0[i] - cnt_1[i])

print(sum)
