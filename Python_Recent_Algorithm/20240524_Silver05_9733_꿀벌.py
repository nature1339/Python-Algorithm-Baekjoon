import sys
sys.stdin = open('input_9733.txt')
readl = sys.stdin.readline
# Re, Pt, Cc, Ea, Tb, Cm, Ex 
job = {'Re':0,'Pt':0,'Cc':0,'Ea':0,'Tb':0,'Cm':0,'Ex':0}

# x = list(map((input().split()))) #Cc Pt Pt Re Tb Re Cm Cm Re 


total = 0

#line = [Cc, Pt, Pt, Re Tb Re Cm Cm Re Pt Pt Re Ea Ea Pt Pt Pt Re Re Cb Cb Pt Pt Cb]
while True: #몇줄받을지 모를때 while true
    line = readl() #한줄씩 갖고옴 #첨에 문자열 str로 받음 int나 str로 바꿔주지않는이상
    if not line: #그줄에 아무내용이 없으면
        break
    
    line = line.split() #개행문자 없애면서 리스트화 한줄로 리스트됨
                        # 첫째줄 담겼다가 둘째줄 다겼다가 바뀜

    for i in line: #Cc Pt Pt Re Tb Re Cm Cm Re Pt Pt Re Ea Ea Pt Pt
        total += 1
        if i not in job:
            continue
        job[i] += 1

# print(job)
for name, cnt in job.items():
    print(f"{name} {cnt} {cnt/total:.2f}")
print(f"Total {total} 1.00")


    
    
      





