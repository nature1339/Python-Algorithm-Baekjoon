import sys

sys.stdin = open("input_2002.txt")
readl = sys.stdin.readline

n = int(readl())

overpass = set()

car_in = [readl().rstrip() for i in range(n)]  # a,b,c,d

car_out = [readl().rstrip() for i in range(n)]  # a,b,c,d

i, j = 0, 0

while i <= n or j <= n:
    if car_in[i] in overpass:
        i += 1
        continue

    elif car_in[i] == car_out[j]:
        i += 1
        j += 1

    else:
        overpass.add(car_out)
        j += 1
print(len(overpass))
