import sys
sys.stdin = open('input_14425.txt')
readl = sys.stdin.readline


s = set()

n, m = map(int, readl().split()) #map은 split할때만 가능


for i in range(n):
    t = readl().rstrip()  #총 N개의 문자열로 이루어진 집합 S가 주어진다.
    s.add(t) #집합에 추가할때는 add
 
# for j in range(n+1, n+m+1): #그밑에줄 반복시 굳이 안해도됨
cnt = 0
for j in range(m):    #그밑에줄 반복시 그냥 m만 반복해도됨         
    ins = readl().rstrip()                   
    if ins in s: # if starlink in s:
        cnt += 1
print(cnt)    
    # break --> 반복하다 중간에 답찾으면 멈출때 사용
        
    # if j in s:
    #     l.append(j)
    #     print(len(l))
    # break    
            
    
    
    
    

    

