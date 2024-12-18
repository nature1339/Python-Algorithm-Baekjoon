import sys
sys.stdin = open("input_11536.txt")
readl = sys.stdin.readline

def increasing(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True # 끝까지 오면 decreasing안하고 increasing으로 와서 return true

def decreasing(lst):
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            return False
    return True

n = int(readl())
lst = [readl().rstrip() for _ in range(n)]
#  for i in range(n):
#     #     name = readl().rstrip()
# #     first.append(name)
# #     # ['JOE', 'BOB', 'ANDY', 'AL', 'ADAM']  
if increasing(lst):
    print("INCREASING")
elif decreasing(lst):
    print("DECREASING")
else:
    print("NEITHER")
============================
#  1 2 3  -> 2 -> range(2) ->0 1 
 
# n = int(readl())


# words = []
# for i in range(n):
#     name = readl().rstrip()
#     words.append(name)
#     # ['JOE', 'BOB', 'ANDY', 'AL', 'ADAM'] 

# # increasing ?
# incr = True
# for i in range(len(words)-1):
#     if words[i] > words[i+1]:
#         incr = False # 검사하다 false이면 검사중단
#         break
# if incr:
#     print("INCREASING")
#     sys.exit(0)

# desc = True
# for i in range(len(words)-1):
#     if words[i] < words[i+1]:
#         desc = False
#         break #반복문을 종료
# if desc:
#     print("DECREASING")
#     sys.exit(0) #decreasing출력하고 프로그램을 종료

# print("NEITHER")
# =================================
# for j in range(len(words)-1):  
#     for j in words:
#         if words[j] > words[j+1]:
#             print("DECREASING")
#             break  -> 각각 반복문이 아니라서 틀림
#     elif j in first:
#      words[j] < words[j+1]:
#         print("INCREASING")   
#         break
#     else:
#         print("NEITHER")
#         break
