import sys
sys.stdin = open('20240821_1021_SILVER03.txt')
readl = sys.stdin.readline

n, m = map(int,readl().split()) #n개의 원소 10

s = [for i in range(n)]   #1 2 3 4 5 6 7 8 9 10
cnt = 0

왼족으로 미는 함수 구현하기
오른족으로 미는 함수 구현하기
첫번재 원소가 내가 원하는 원소이면 pop하는 함수 구현하기

예시

def push_left (arr):
    **구현**
    return arr
def push_right (arr):
    **구현**
    return arr
    
def is_first (arr, num):
    **구현**

for i in range(n): #1 2 3 4 5 6 7 8 9 10
      x = readl().rstrip() #2 9 5 x= [2,9,5]
      x[i] #2를 호출하면, 
      if x[i] == s[0]:   
          continue
      elif x[i] != s[0]:              
        cnt += 1