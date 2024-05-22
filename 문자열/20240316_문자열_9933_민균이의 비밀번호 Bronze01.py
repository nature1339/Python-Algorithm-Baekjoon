import sys
sys.stdin = open('input_9933.txt')
readl = sys.stdin.readline

# 4
# las
# god
# psala
# sal

n = int(readl())
s = [] # s = [las, god,psala]

# for i in range(n): #4
#     line = readl().rstrip()  # las
#     s.append(line) # s = [las, god,psala, sal]
#     # 다 담으면 for 문 밖에서 실행

s = [readl().rstrip() for _ in range(n)] #s = [las, god,psala, sal]

for i in range(n):  # s = [las, god,psala,sal]
    for j in range(i, n):   #las, god,   las, psala
        if s[i]== s[j][::-1]: #las  s[0] ==s[1], s[0]==s[0+0+1], s[i=3]=s[j=3]
             #las 3//2  3/2 = 1.5
            print(len(s[i]), s[i][len(s[i])//2])    #lens[s[0]] 3 , a        #2<2.5<3
    
    
    # for j in line: # las
    #     if line == line[::-1]: #sal
    #         center = line//2
    #         print(line)
        