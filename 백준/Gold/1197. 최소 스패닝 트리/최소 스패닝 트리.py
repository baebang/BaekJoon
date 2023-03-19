# 부모 노드를 찾는 함수
def getParent(parent , x):
    if(parent[x] == x):
        return x
    else: 
        return getParent(parent,parent[x])

#부모 노드를 합치는 함수
def unionParent(parent,a,b):
    a = getParent(parent,a)
    b = getParent(parent,b)
    if (a<b): parent[b] = a
    else: parent[a] = b

#부모를 가지는지 확인한다.
def findParent(parent,a,b):
    a = getParent(parent,a)
    b = getParent(parent,b)
    if a==b: return 1
    else: return 0
# 노드의 개수와 간선의 개수 입력 받기
v,e = map(int,input().split())
parent = [0] * (v+1) #부모의 테이블 초기화

#모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b,cost = map(int,input().split())
    #비용순으로 정렬하기 위해서 튜플의 첫번째 원소를 비용으로 설정
    edges.append((cost,a,b))

#간선을 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인하며
for edge in edges:
    cost ,a ,b = edge
    #사이클이 발생하지 않은 경우에만 포함
    if getParent(parent,a) != getParent(parent,b):
        unionParent(parent,a,b)
        result += cost

print(result)
