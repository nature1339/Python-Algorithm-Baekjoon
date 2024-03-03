import sys
sys.stdin = open('input_5704.txt')
readl = sys.stdin.readline

 #jackdawf loves my big quartz sphinx  


 
while True:
    line = readl().rstrip() #jackdawf loves my big quartz sphinx
    if line == '*':
        break
    # d = [False] * 26
    d = {chr(i+ord('a')): False for i in range(26)}
    # d = {'a': False, 'b': False,...}
    for ch in line: #[j,a,c,
        # d[ord(ch) - ord('a')] = True
        d[ch] = True #d['a'] = true
    
    if all(d.values()):
        print('Y')
    else:
        print('N')

# while True:
#     line = readl().rstrip() #jackdawf loves my big quartz sphinx
#     if line == '*':
#         break
#     d = [False] * 26
#     for ch in line: #[j,a,c,
#         d[ord(ch) - ord('a')] = True
    
#     if all(d):
#         print('Y')
#     else:
#         print('N')        
#-------------------------------------
        
    #     alphabet.append(97+i) #[97,98,0..]
    #     if alphabet[i] + alphabet[i+1] = z
    #        print(Y)
            
    # if line == '*':
    #     break
    
    
 
# line = list(readl().rstrip().split()) 

# for i in line:   #jackdawf loves my big quartz sphinx  
    
        