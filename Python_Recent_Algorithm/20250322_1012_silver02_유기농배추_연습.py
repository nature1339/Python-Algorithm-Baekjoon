import sys
input = sys.stdin.readline




n = int(input()) #2

graph = [[] for i in range(n+1)]  #인접리스트, 리스트컴프리핸션   
#graph = [ [] [] [] [] ]
#graph = [[]]
#gpaph = [ [] []]

#v= [0,0,0,0]
for i in graph: #입력노드로 받음 그림이 문제에 있음
    if i not in graph:
        graph.append[i] # i번 노드에 방문하지 않았으면 graph[1]=1
        #역순어떻게 표현?

visted = []
#v = [0,0,0,0]
def dfs(1,graph,n+1): #
    for i in visted:
        if i not in v:
            v[i] = 1
    dfs()

visited[1]=1
dfs(1,v,n+1)
print(count(n+1)-1)



