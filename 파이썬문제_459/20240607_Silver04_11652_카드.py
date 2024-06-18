import sys
sys.stdin = open('input_11652.txt')
readl = sys.stdin.readline


n = int(readl())

card = {}  # 1:3, 3:5, 2:5
           # 1:3, 2:5, 3:5
# 1:3, 2:4
# 1, 2 

for i in range(n):
    # card.key = list(map(int, readl().split())) # 입력이 1 2 4 4 이렇게 한줄로 받을때 list
    card_number = int(readl().rstrip()) #여러줄일때
    # card.append(card_number)  -->  #dictonary는 append없음   
    if card_number in card:
        card[card_number] += 1
    else:
        card[card_number] = 1
   
top = max(card.values()) #max = 하나만 나옴
for k in sorted(card.keys()):
    if card[k] == top: # value가 max이면
        print(k)  #sort된 가장 작은 key출력
        break     #가장많은 정수를 출력하면 끝나는 문제라서

# for k, v in card.items():
#     if v == top:
#         print(v)  #--> values() 괄호 붙여야, keys()
#         break
    
    