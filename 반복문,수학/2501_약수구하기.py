n,k = map(int, input().split())

l = []

def yaksu():
    for i in range(1, n+1):
        if n % i == 0:
            l.append(i)

yaksu()
print(l[k-1])

          
            
            
            