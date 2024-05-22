import sys
sys.stdin = open("input_output.txt")

n = int(input())
for _ in range(n):
    x = input()
    print(x)


print()

sys.stdin = open("input_output2.txt")

while True:
    x = input().rstrip()
    if x == 'EOI':
        break
    print(x)
