import sys
sys.stdin = open('input_17219.txt')
readl = sys.stdin.readline

n, m = map(int,readl().split())
password = {} #{acmicpc.net: UAENA,startlink.io: THEKINGOD }

for i in range(n):
    address, pw = readl().split() #noj.am, IU
    password[address] = pw  #dictionary 추가하는방법 password[key] = value
    

for j in range(m):
    #if address == password.keys(): , 반드시 이미 저장된 사이트 주소가 입력된다이러서 안써도됨
    site = readl().rstrip() #입력 또 받아야함
     #startlink.io
    # print(password.values())
    print(password[site])
 
    


        