import sys
sys.stdin = open('input_1181.txt')
readl = sys.stdin.readline

n = int(readl()) #알파벳 소문자 -> 문자열

# 1: []
# 2: []
# 3: []...
# ...
# 50
words_by_len = [set() for _ in range(51)]
for _ in range(n):
    word = readl().rstrip()
    s = len(word)
    words_by_len[s].add(word)

# for s in words_by_len:
#     print(s)
for words in words_by_len:
    if not words:
        continue
    print('\n'.join(sorted(words)))



# line = [readl().rstrip() for _ in range(n)] 


#                 # [but, i, wont,...n] 0 1 2  n-1, 
# for i in range(n-1):  #l[0], l[1],  l[1], l[1+1]
    
#     for j in range(1, n): # but, j  1 , but wont j 2 , n-1, n
#         if len(l[i]) > len(l[j+1]): # len(l[0]) > len(l[0+1]), 3 > 1
#             l[j] = l[j+1]  #i, but   #len(l[0]) > len(l[1+1])
#                                       #len(l[1]) > len(l[1+1])
#                                       # len(l[n-1]) > len(l(n))