import sys
sys.stdin = open('input_2789.txt')
readl = sys.stdin.readline

c = ['C','A','M','B','R','I','D','G','E']

line = list(readl().rstrip())
for i, ch in enumerate(line):  # (0, L), (1, O), (2, V), (3, A)
    if ch in c:    #(3, A) ch = A in c
        line[i] = ''   #line[0] = ''  line = [L,O,V]
print(''.join(line)) #list 요소를 합침

    # line = readl().rstrip #LOVA
    # line.replace(line[i],'')
    # print(line)
        
        