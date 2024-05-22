import sys
sys.stdin = open('input_11531.txt')
readl = sys.stdin.readline

cnt = 0
total_m = 0

w_name = [] #A, A, A
right = {}  # 어떤 문제를 맞췄는지, 맞춘 시간 #a,200, c, 300
count = {}  # 어떤 문제를 몇 번 틀렸는지, # a:2 , c:1
for i in range(100):
    line = readl().rstrip()
    if line == '-1':
        break
    
    t, name, result = line.split() #3 E right
    t = int(t)
    if result == 'right':
        right[name] = t
    else:
        if name not in count:  # count.keys()
            count[name] = 1
        else:
            count[name] += 1
        
    #     cnt += 1 
    #     total_m += int(m)
    # w_name.append(name) #A, A, A
    
penalty = 0
for name, time in right.items():
    penalty += time 
    if name in count:
        penalty += count[name] * 20
print(len(right), penalty)





