l = [] # 1 2 3 4 5 6 7 8 9 10
k = [] # 1 2 3 4 5 6 7 8 9 10


def peace():
    for j in range(len(k)-1):
        if k[i] == k[len(k)-1]:
            return False
    return True

count = 0
    
for i in range(10):
    l.append(int(input()))
    k.append(l[i]%42)    
    if peace():
        count +=1   
    
print(count)    
    
