import sys 
sys.stdin = open('input_10988.txt')
line = sys.stdin.readline().rstrip()

#0 1 2 n-1, n,   2n-1   

# length : 5
# 0 1 2 3 4
# 0 1   -2 -1
for i in range(len(line)//2):
    if line[i] != line[-1-i]:
        print(0)
        sys.exit(0)
# 반복문이 종료 안되고 끝까지 실행됐으면 펠린드롬
print(1)

    
    