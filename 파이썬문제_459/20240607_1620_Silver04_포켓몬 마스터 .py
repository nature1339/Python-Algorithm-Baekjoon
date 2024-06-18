import sys
sys.stdin = open('input_1620.txt')
readl = sys.stdin.readline

n, m = map(int(readl()))  #26 5
pocket = {} #1: 'Bulbasaur',   2:'Ivysaur'

for i in range(n): #26
    name = list(map(readl().rstrip())) #Bulbasaur, Ivysaur, ....
    for j in range(i): #list[i]   list[0] = Bulbasaur
        pocket[j] = name[i]  #1: Bulbasaur,   2:Ivysaur  #{i}:{name}


for i in pocket.keys:
    if name == type(number):
        print(pocket.value)
    elif name == type(str):
        print(pocket.key)        

# for i, j in pocket:
#     if i == type(number):
#         print(pocket[i])
#     elif i == type(str):
#         print(pocket[i])
                
   
    
    
