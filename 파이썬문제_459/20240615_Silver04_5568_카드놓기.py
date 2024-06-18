from itertools import permutations
# permutations(iterable, r)
import sys
sys.stdin = open('input_5568.txt')
readl = sys.stdin.readline

n = int(readl()) #1 2 12 1  -> k개 고르는 갯수 -> 2**n  k**n
k = int(readl()) #2개를 골라  
card = [] #1 12  -> 1 1 2,  1 2 1 , 2 1 1,  # 2 1  -> 1 2 , 2 1 -> 숫자개수
    #k개 고르는 갯수 -> 2**k * 숫자개수   -> 12 7 2
# 1
# 2
# 12
# 1
for i in range(n):
    num = readl().rstrip() #2   문자열로 입력 12 -> '12'  12 7 2
    card.append(num)

# card = [int(readl()) for _ in range(n)] # readl()을 int로 리스트안에 넣는데 n번반복해라
# card = [readl().rstrip() for _ in range(n)] # readl()을 그냥문자열로 리스트안에 넣는데 n번반복해라
# print(card)
# print(len(set(permutations(card, k))))
print(len(set(''.join(a) for a in permutations(card, k))))

# 12 7 2 => 1272
# 1 2 72 => 1272
# a = ['5', '3', '7']
# ' '.join(a) -> "5 3 7"
# ''.join(a) -> "537"
# print(int(2**k)    
    
    
    
    