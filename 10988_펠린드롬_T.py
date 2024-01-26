
n = input()  # level 0~4
list = []  # level
# print(list[0])

      #l,e,v,e,l
# print(len(n))
for i in range(len(n)):
    list.append(n[i])

# print(list)
    


def pelindrom():
    for i in range(len(n)//2):
        if list[i] == list[len(n)-i-1]:
            continue
        else:
            return 0 
    
    return 1
    
len(n)  # 5
pelindrom()

print(pelindrom())