l = []  #[10, 4, 5, 5, 7]
k = []  #[10, 4, 5, 5, 7]
count = 0

def check():
    for j in range(len(k)-1):
        if k[j] == k[len(k)-1]:
            return False
    return True
        
for i in range(10):    
    l.append(int(input()))
    k.append(l[i]%42)
    if check():
        count += 1    


print(count)    
    