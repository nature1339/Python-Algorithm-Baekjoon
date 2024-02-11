
import sys
sys.stdin = open('input_4458.txt', 'r')
lines = sys.stdin.readlines()


for line in lines[1:]:
    line = line.rstrip()                               
    if ord(line[0])>= 65+32:  # 소문자인 경우            
        print(chr(ord(line[0]) - 32), end='')
        # P(커서)
        # print(chr(ord(line[0]) - 32))
        # P
        # end=''없으면(다음줄에 커서)
        print(line[1:])
    else:  # 소문자가 아닌 경우 (대문자인 경우)
        print(line)
    