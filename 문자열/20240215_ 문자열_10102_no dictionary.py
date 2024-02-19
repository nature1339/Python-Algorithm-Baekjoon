import sys
sys.stdin = open('input_10102.txt')
lines = sys.stdin.readlines()

line = lines[1].rstrip()
cnt_a, cnt_b = 0, 0
for j in line:
    if j == 'A':
        cnt_a += 1
    else:
        cnt_b += 1
# cnt_a, cnt_b = line.count('A'), line.count('B')
# A의 갯수합이랑 B의 갯수의합 = cnt_a, cnt_b에 넣는다

if cnt_a > cnt_b:
    print("A")
elif cnt_b > cnt_a:
    print("B")
else:
    print("Tie")