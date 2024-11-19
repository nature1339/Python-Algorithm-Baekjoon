import sys
sys.stdin = open('input_7785.txt')
readl = sys.stdin.readline

n = int(readl())
company = {} #{Baha: leave, Askar:enter, Artem: enter}
stay = []

for i in range(n):
    name, inout = readl().split() #Baha leave
    company[name] = inout
   
for name, inout  in company.items():
    if inout == "enter":
        stay.append(name)
print('\n'.join(sorted(stay, reverse=True)))
