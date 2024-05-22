import sys
sys.stdin = open('input_25593.txt')
readl = sys.stdin.readline

num = int(readl())

# - - - - - pangyo puang
# - - - - - sally boss
# - - - - - leonard brown
# - - - - - edward edward
# times = [4, 6, 4, 10]

work = {} #edword: 1

for i in range(num):
    # for k in range(4):
    #     time = times[k]
    for time in [4, 6, 4, 10]:
        line = readl().split() #- - - - - pangyo puang
        for name in line:
            if name == '-':
                continue
            if name not in work:
                work[name] = time
            else:
                work[name] += time   #work[edword] = 1
if (len(work) == 0) or (max(work.values()) - min(work.values()) <= 12):
# if fair <= 12:
    print('Yes')
else:
    print('No')