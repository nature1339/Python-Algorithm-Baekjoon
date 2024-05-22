import sys
sys.stdin = open('input_11531.txt')
readl = sys.stdin.readline

# 총걸린시간 total_m
subj_right = {} #{'E':100, 'A':200, 'D':150} # 문제맞춘 시간 , sbject: time
submit_time = {} #{'E':1, 'A':3, 'C':2, 'D':1 } 
#틀린횟수 제출횟수아님
#subject: submit  wrong 2번이상일수도
                 #문제 제출횟수,  총시간
total_time = 0
#3 E right
for i in range(100):
    line = readl().split() #3 E right
    # # if line == '-1':  # ['-1'] #time, subj, result = line value하나만 있어서 오류
    #     break
    if line[0] == '-1':  # ['-1'] #time, subj, result = line value하나만 있어서 오류
        break
    # else:
    #     continue  //continue면 밑에를 실행안하고 다시 위 for문으로 돌아감
    time, subj, result = line #[3, E, right]
    time = int(time)
    if result == 'right':
        subj_right[subj] = time # 'E':맞춘시간
                                #없을때는 교체안되고 들어감
    else:
        if subj not in submit_time:
            submit_time[subj] = 1
        else:
            submit_time[subj] += 1   #틀린횟수가 penalty에 영향을 줘서 틀린횟수 증가

    
    
for s, t in subj_right.items():
    penalty = t   #t 는 맞춘시간 subj_right의 value값
    if s in submit_time: # 한번이라도 틀렸을경우
        penalty += submit_time[s]*20 #맞은과목의 제출횟수를 갖어옴
    total_time += penalty 

print( len(subj_right), total_time) #문제맞춘수, total time    
    
    

    