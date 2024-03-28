import sys
sys.stdin = open('input_10988.txt')
line = sys.stdin.readline().rstrip()

#level
#le  el

length = len(line)//2  #5//2 = 2

for i in range(length):  # 0 1
    if line[i] != line[-1-i]: # line[0] == line[-1] l == l 
                           # line[1] == line[-1-i] = line[1] == line[-2] e == e
        print('0')                           
        sys.exit(0)
        # 반복문이 종료 안되고 끝까지 실행됐으면 펠린드롬
print('1')