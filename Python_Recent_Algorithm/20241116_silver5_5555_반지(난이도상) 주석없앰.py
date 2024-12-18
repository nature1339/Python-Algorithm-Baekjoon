import sys
sys.stdin = open('input_5555.txt')
readl = sys.stdin.readline #readlines은 전부다 읽고끝남

find = readl().rstrip() #ABCD A,B,C,D
n = int(readl())
count = 0
for _ in range(n):
    word = readl().rstrip() #ABCDXXXXXX
    word = word + word # [:len(find)-1] #2
    for i in range(10) #10번째인Y부터3번째까지만
    :#ZAAAAAAAXYZAAAAAAAXY
        if word[i:i+len(find)] == find: #word[i:i+len(find)]
            count += 1
            break
print(count)
