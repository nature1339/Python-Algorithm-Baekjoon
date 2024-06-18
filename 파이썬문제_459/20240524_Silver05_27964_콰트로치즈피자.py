import sys
sys.stdin = open('input_27964.txt')
readl = sys.stdin.readline

n = int(readl())

arr = readl().split()   #CheddarCheese 
                                          #MozzarellaCheese GoudaCheese GranaPadanoCheese
#하나씩 치즈를 받아서 4개면 콰트로 => yummy
arr = set(arr)

cheese = []
for toping in arr:
    if toping.endswith('Cheese'): # cheese로 끝나면
        cheese.append(toping)  #cheese 배열에 넣는다.

# quatre = []

# for i in arr:    #MozzarellaCheese MozzarellaCheese MozzarellaCheese MozzarellaCheese
#     if arr[i] != arr[i+1]: #list indices must be integers or slices, not str
#                            #arr[i] => i는 문자라서 에러남
#         quatre.append[arr[i]] 

if len(cheese) >= 4: #재료가 4개이상이면 쿼트로4개치즈를 고를수 있음.
    print("yummy") 
else:              #4개 미만이라서 4개치즈 고를수 없음
    print("sad")    




