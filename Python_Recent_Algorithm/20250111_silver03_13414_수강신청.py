import sys

sys.stdin = open("input_13414.txt")
readl = sys.stdin.readline


success, waiting_number = map(int, readl().split())  # 3 8

waiting_list = {}
# waiting_list["name"] = "value" name의 key의 value를 넣는다

for i in range(waiting_number):  # i : 0 ~ waiting_number - 1
    call = readl().rstrip()  # key a: 1  key value
    waiting_list[call] = i + 1

    # waiting_list[call] #이거는 call의 value가 있다고 가정하고 접근
    # waiting_list.get(call) #있는지 없는지에 따라 value 출력, 없으면 none

    # if waiting_list.get(call) != None:  # call의 value가 none이 아니면(즉, 중복클릭이면)
    #     waiting_list[call] = i + 1  # 현재상태 다음번으로 순서가 현재상태의 맨뒤로감
    # else:  # 중복이 아니고 처음들어와도 맨뒤
    #     waiting_list[call] = i + 1
waiting_list  # {c: 3, d: 4, b: 6, a: 7}
waiting_list.items()  # [[a, 7], [b, 6], [c, 3], [d, 4]]
li = sorted(
    waiting_list.items(), key=lambda x: x[1]
)  # [[c, 3], [d, 4], [b, 6], [a, 7]]

for i in range(success):
    if i >= len(li):
        break
    print(li[i][0])
