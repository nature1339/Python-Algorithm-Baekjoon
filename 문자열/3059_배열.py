n = int(input()) 
# m = input() #ABCDEFGHIJKLMNOPQRSTUVW
# n = input() #A
r = []
d = {}

for q in range(n):
    line = input().rstrip()
    # r.input() # ABCDEFGHIJKLMNOPQRSTUVW A
    # r.rstrip()  #ABCDEFGHIJKLMNOPQRSTUVWA
    
    arr = [False] * 26  # [False, False, ...]
    # A, B, C, D .. 
    
    # for ch in range(len(r)): 0 ~ len(r)-1 # r.key() = 
    for ch in line:
        arr[ord(ch) - ord('A')] = True

    s = 0
    # for i, k in enumerate(arr):
    for i in range(26):
        if arr[i] == False:
            s += i + ord('A')
    print(s)
