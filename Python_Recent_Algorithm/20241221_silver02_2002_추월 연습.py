import sys

sys.stdin = open("input_2002.txt")
readl = sys.stdin.readline

n = int(readl())

overpass = set()    

car_in = [readl().rstrip(), for i in range(n)]  # a,b,c,d

car_out = [readl().rstrip(), for i in range(n)] # a,b,c,d
if car_in < car_out: #a < c
    overpass.add(car_out)
else:
    
    





