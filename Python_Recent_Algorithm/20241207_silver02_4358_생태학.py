import sys

sys.stdin = open("input_4358.txt")
readl = sys.stdin.readline

spices = {}
# total = [readl().rstrip() for i in range(n)]
# if tree[i] == tree[i+1]:


count = 0
while True:
    tree = readl().rstrip()
    if not tree:
        break

    if tree not in spices:  # 은행나무가 종에 없으면/나무가 나오면 종이됨
        spices[tree] = 1
    else:
        spices[tree] += 1
    count += 1


for tree in sorted(spices.keys()):  # 알파벳순서대로
    print(f"{tree} {(spices[tree] / count) * 100:.4f}")
    # 공백은 띄어쓰면됨  , spices[tree] => value

# for key, value in spices:
#     spices.key(i)
#     print("key",f{"spieces.dic[value] /count"})
#     # a.dic[value]= ...
