import sys
sys.stdin = open('input_9933.txt')
readl = sys.stdin.readline

n = int(readl()) #4
# las
# god
# psala
# sal
cntr = 0

for i in range(n):
    pw = list(readl().rstrip()) #las = sal, [l,a,s][psala]]
    pw_reverse = pw.reverse #[s,a,l]  pw[cntr]
    cntr = len(pw)//2+1  #las 1.5 lsala 2.5     
    if pw == pw_reverse:
        print(len(pw), pw[cntr])    
        
