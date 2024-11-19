import sys
sys.stdin = open('input_5063.txt')
readl = sys.stdin.readline

n = int(input())


for i in range(n): #r,e,c   
    r, e, c = map(int, readl().split())
    if r < e-c:
        print ("advertise")
    elif r > e-c:
        print ("do not advertise")
    elif r == e-c:
        print ("does not matter")
    
    # r >< e-c
    
    #r>e print "do not advertise"                      
    # r=e print "do not ma
    # r광고를 하지 않았을 때 수익, 
    # e는 광고를 했을 때의 수익,
    # c는 광고 비용이다. 
    # 0 100 70   r<e print "advertise"
    #            r>e print "do not advertise"     
    #            r=e print "do not matter"    