import sys

sys.stdin = open("input_13414.txt")
readl = sys.stdin.readline


success, waiting_number = int(readl().split())  # 3 8

waiting_list = set()

for i in range(waiting_number):
    call = readl().rstrip()
    if call in waiting_list:
        continue
    else:
        waiting_list.add(call)


print(waiting_list)
