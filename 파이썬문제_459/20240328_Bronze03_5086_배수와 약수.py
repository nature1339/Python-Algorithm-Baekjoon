import sys
sys.stdin = open('input_5086.txt')
readl = sys.stdin.readline

# def func(x):
#     return x + 3

while True:
    n, m = map(int, readl().split()) # readl().split()=['8', '16']
                                     # map(int, readl().split())= [int'8', int'16']
                                    #map(앞쪽 연산자(int), 뒤쪽은 연산받을것)
    # print(list(map(func, [n, m])))
    if n == 0 and m == 0:
        break  #종료조건이 input다음에 들어가야

    if m % n == 0:
        print("factor") 
    elif n % m == 0:
        print("multiple")        
    else:
        print("neither") 
           