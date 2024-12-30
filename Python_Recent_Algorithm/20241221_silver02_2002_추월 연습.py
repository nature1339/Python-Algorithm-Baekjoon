import sys

sys.stdin = open("input_2002.txt")
readl = sys.stdin.readline

n = int(readl())

overpass = set()    

car_in = [readl().rstrip(), for i in range(n)]  # a,b,c,d

car_out = [readl().rstrip(), for i in range(n)] # a,b,c,d

while i<=n or j<=n  :
    if car_in[i] == car_out[j]:
        car_in[i] += 1
        car_out[j] += 1
    elif car_in[i] < car_out[j]: #a < c
        overpass.add(car_out)
    else:
        car_in[i] > car_out[j]:
            
    
    





