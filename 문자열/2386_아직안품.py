import sys
sys.stdin = open('input_2386.txt')
line = sys.stdin.readline().rstrip


# g Programming Contest
# n New Zealand
# x This is quite a simple problem.
# #
# if g가 반복문해서 count 출력 count 첫글자 line[0]

count = 0

for i in line:  # g Programming Contest    
    first = ord(line[0]) # 아스키코드값
    if first == ord(line[i+2]):
        count += 1
    if "#":
        break
    print(line[0]+""+ count)    
    
    
    