import sys
input = sys.stdin.readline

n = int(input()) #n =node = vertex
e = int(input()) #e = 간선 = edge

graph = [[] for _ in range(n + 1)]
'''
graph = [[], 0번 노드
         [2,3], 반복문 -> 1번노드의 [2,3]번봄. 1번 노드에 연결되어 있는 노드들의 리스트 2방문후 3 방문하는게 재귀
         [1],
         [],
         ... 7번 노드
           ]
'''
#graph변수는 graph정보를 갖고있는 자료구조인데 지금은 아무것도 없기때문에 간선정보를 입력받아서 (문제에서 입력받음)넣는다.

for i in range(e): #e는 간선개수만큼 입력받아서 반복
    a, b = map(int, input().split())
    graph[a].append(b) #인덱스1의 리스트
    graph[b].append(a)
    # 무방향 그래프이기 때문에 양쪽에서 모두 연결해줘야 함
    
visited = [0] * (n + 1) #0을 포함하기 때문에 n+1, 문제에서 1번컴퓨터부터 시작해서
# visited[1] -> 1번 노드의 방문 여부를 따짐. 0 : 방문하지 않음
# [0, 0, 0, 0, 0, 0, 0] 예를들어 7개컴퓨터있으면 n+1, 8번하면 직전까지라서
# visited와 v는 아예다름
# v: 시작하는 지점, graph: 그래프, visited: 방문 배열
def dfs(v, graph, visited): #visited는 방문했는지 체크하는배열
    #graph는 graph정보를 담고있는 인접리스트,v는 시작지점
    # graph[v]: v번 노드에 연결되어 있는 노드들의 리스트
    for i in graph[v]:
        # visited[i]: i번 노드의 방문 여부
        if visited[i] == 0: # i번 노드가 방문하지 않았다면
                       #visited[i]=1이면 참
                       #만약 방문하였으면 방문하면 안됨
            visited[i] = 1 # 방문을 해서 1로바꿔줘서 방문체크
            dfs(i, graph, visited)

# dfs(1번노드) -> dfs(2번노드) -> dfs(3번노드) -> dfs(5번 노드) -> dfs(6번노드)
# 3번 노드에선 길이 없기 때문에 2번노드로 돌아옴

# 1번노드부터 시작
visited[1] = 1
dfs(1, graph, visited)

# visited 배열에 1이 몇개 있는지 count
print(visited.count(1) - 1) # 1번 컴퓨터 제외