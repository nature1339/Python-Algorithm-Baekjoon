import sys
sys.stdin = open('input_16499.txt')
readl = sys.stdin.readline

n = int(readl())
# s = set([readl().rstrip() for _ in range(n)]) #{'tca', 'cat', 'dog', 'god'}


# group = list[set(tac), set(dog)] set(set) set안에 set은 안됨
# t a c
# d o g

#list[set(tac, dog)]

group = []

# for i in range(n): #4
#     word = set(readl().rstrip()) #tca
#     if word not in group:
#         group.append(word)
# print(len(group))        


group = set() # act  #알파벳순 
for i in range(n):
    word = readl().rstrip()
    group.add(''.join(sorted(word)))  # tac -> act, cta -> act
print(len(group))
 


