'''
import sys
sys.stdin = open('input_1371.txt', 'r')
readl = sys.stdin.readline

d = {}
for i in range(26):
    d[chr(ord('a') + i)] = 0

for i in range(50):
    line = readl().rstrip()

    for ch in line:
        if ch == ' ':
            continue

        d[ch] += 1

cnt_max = max(d.values())
for ch, cnt in d.items():
    if cnt == cnt_max:
        print(ch, end='')
print()
'''

import sys
sys.stdin = open('input_1371.txt', 'r')
lines = sys.stdin.readlines()

d = {}
for i in range(26):
    d[chr(ord('a') + i)] = 0

for line in lines:
    line = line.rstrip()

    for ch in line:
        if ch == ' ':
            continue

        d[ch] += 1

cnt_max = max(d.values())
for ch, cnt in d.items():
    if cnt == cnt_max:
        print(ch, end='')
print()

