import sys
sys.stdin = open('input_1408.txt')
readl = sys.stdin.readline

crr_h,crr_m,crr_s = map(int,readl().split(':')) #13:52:30 현재시간, [13,52,30]
start_h,start_m,start_s = map(int,readl().split(':'))  #14:00:00 임무를 시작한시간 , [14,00,00]
                                    #남은시간은 00:07:30 
                                    
# left_h = []
# left_m = []
# left_s = []
#-1  -1  60
#14:00:00 start (end)
#13:52:30 crr

if start_s < crr_s:
    left_s = (start_s + 60) - crr_s
    carry_m = 1
else:
    left_s = start_s - crr_s
    carry_m = 0

if (start_m - carry_m) < crr_m:
    left_m = (start_m - carry_m + 60) - crr_m
    carry_h = 1
else:
    left_m = (start_m - carry_m) - crr_m
    carry_h = 0
    
if (start_h - carry_h) < crr_h:
    left_h = (start_h - carry_h + 24) - crr_h
else:
    left_h = (start_h - carry_h) - crr_h
    

# if start_h < crr_h:
#     start_h += 24

# left_h = start_h-1-crr_h
# left_m = start_m+60-1-crr_m
# left_s = start_s+60-crr_s

# left_h.append(start_h-1-crr_h) #
# left_m.append(start_m+60-1-crr_m)
# left_s.append(start_s+60-crr_s)
print(f'{left_h:02d}:{left_m:02d}:{left_s:02d}')
#14:00:00
#13:52:30
#00  8 30
    



