import sys
sys.stdin = open('input_11507.txt')
readl = sys.stdin.readline

card = readl().rstrip() #P01K02H03H04

# for i in card: #P01K02H03H04
group = {'P': set(), 'K': set(), 'H': set(), 'T': set()}
# groupP = set() #P01 K02 H03 H04
# groupK = set()
# groupH = set()
# groupT = set()

# range(start=0, stop, step=1)
# for i in range(5)   range(0, 5, 1)
for i in range(0, len(card), 3):  # range(start, stop, step)
    shape = card[i] #P, H, T, K
    num = int(card[i+1:i+3])
    if num in group[shape]: #P, H, T, K , group H: set(2)일때 group[H] 는 group H:set(2) 똑같으면 GRESKA
        print('GRESKA')
        sys.exit()
    
    group[shape].add(num)

for shape in 'PKHT':
    print(13 - len(group[shape]), end=' ')

    
#     if card[i:i+3] in group: #P01 
#         print('GRESKA')
#     else:
#         group.append(card[i:i+3])
# print(' '.join(group))
           
    




