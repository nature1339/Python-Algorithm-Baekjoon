from collections import deque

# 정점, 간선수, 시작점을 입력받음
n, m, v = map(int, input().split())
# 초기값을 False로 만들어 그래프를 선언
graph = [[False] * (n + 1) for _ in range(n + 1)]

# 연결된 정점을 입력
for _ in range(m):# 간선이 5개라서 5번 반복
    x, y = map(int, input().split()) #key,value 개념 x,y가 1,2
    graph[x][y] = 1  # x, y가 1, 2 노드일때 1이 갈수있다는 개념 0은 못간다는의미
    graph[y][x] = 1

# 입력값
#4 5 1   정점(노드개수) 간선수(선) 시작점(시작노드:1번)

#여기부터 입력 쳐서함 import아님
# 1 2  x, y     간선수가 5라서 5줄이있음
# 1 3
# 1 4
# 2 4
# 3 4

# dfs와 bfs 그래프의 방문 여부를 담을 리스트

visited2 = [False] * (n + 1)

# dfs 알고리즘
def dfs(v): #4 5 1  에서 시작점이 1이라서 1부터 시작
    # 방문 처리 # false니까 함수로 들어와서 아래진행
    
    # 방문 후, 정점 출력
    print(v, end=" ")  #1번방문해서 출력, end는 줄바꿈
    # 방문기록이 없고, 인덱스에 값이 있다면(연결되어 있다면)
    for i in range(1, n + 1):
       if graph[v][i] == 1:
            #gragph[1][1]=1
            #gragph[1][2]=1
            #gragph[1][3]=1            
            #gragph[1][4]=1
            
            # if not visited1[1] = if not true = if false = 1번은 true인데 if false 즉 방문안했다는말은 틀림 1번은 볼필요가 없음. 반복문밖이라서
             #if  not visited[2] = if not true = if false = 2번은 방문안함(반복문안쪽이라서 false가됨)
             
             # graph[1][2] == 1  처음 입력값 1, 2 = x, y 
             # graph[x][y] = 1 이게 초기값
             #만족해서 
             #아래 dfs(2)를 호출
            # 방문한다. 재귀함수 활용
            # 호출될 때마다 visited는 1이 되고 재귀되어 v에 i가 들어간다
            dfs(i) # 처음으로 다시 def dfs(2)가 처음부터 실행
            
print()         

# # bfs 알고리즘
# def bfs(v):
#     # 방문할 곳을 순서대로 넣을 큐
#     q = deque([v])
#     # 방문 처리
#     visited2[v] = True
#     # 큐 안에 데이터가 없을 때까지 실행됨
#     while q:
#         # 큐 맨 앞에 있는 값을 꺼내서 출력한다
#         v = q.popleft()
#         print(v, end=" ")
#         for i in range(1, n + 1):
#             # 방문기록이 없고, 인덱스에 값이 있다면(연결되어 있다면)
#             if not visited2[i] and graph[v][i] == 1:
#                 q.append(i)  # 큐에 추가한다.
#                 visited2[i] = True

# dfs(v)
# print()
# bfs(v)
