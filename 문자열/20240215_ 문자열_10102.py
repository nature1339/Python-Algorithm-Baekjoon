import sys
sys.stdin = open('input_10102.txt') 
lines = sys.stdin.readlines()

d = {'A': 0, 'B': 0}
line = lines[1].rstrip()
for j in line:#2번째줄 line(1) 반복 ABABB  

    # j <- character
    d[j] += 1  #-> value값 많아짐

if d['A'] > d['B']:
    print('A')
elif d['B'] > d['A']:
    print('B')    
else:
    print('Tie')    

# 첫째 줄에는 심사위원의 수 V (1 ≤  V ≤  15)가 주어지고,
# 둘째 줄 - 누구에게 투표했는지가 주어진다.
# A와 B는 각각 그 참가자를 나타낸다.

# for line in lines[1:]:
    


# 'A': 0, 'B': 0, ... , 'Y': 0, 'Z': 0
# d = {chr(ord('A')+i): 0 for i in range(26)}

# for i in range(26):
#     d[chr(ord('A')+i)] = 0

# A: 0 , B:0 ...
# A: 1
