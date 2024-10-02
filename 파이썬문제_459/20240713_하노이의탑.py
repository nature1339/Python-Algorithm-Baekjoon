a = [3, 2, 1]
b = []
c = []
cnt = 0

def hanoi(n, a, b, c):
    print(f"hanoi({n}, ...) 호출!")
    global cnt
    cnt += 1
    
    if n > 0:
        hanoi(n-1, a, c, b)
        # a -> b
        b.append(a.pop())
        hanoi(n-1, c, b, a)
        
        # c = n-1
        # n = b
        # b = n-1

hanoi(3, a, b, c)
print(a)
print(b)
print(c)

print(f"total cnt: {cnt}")