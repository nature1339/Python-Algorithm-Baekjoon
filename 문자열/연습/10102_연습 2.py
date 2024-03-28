import sys
sys.stdin = open('input_10102.txt')
line = sys.stdin.readline().rstrip()



cnt_a , cnt_b = 0,0

for ch in line:
    if ch == 'A':
        cnt_a += 1
    else:
        cnt_b += 1    

if cnt_a > cnt_b:
    print("A")
elif cnt_b > cnt_a:
    print("B")
else:
    print("Tie")        