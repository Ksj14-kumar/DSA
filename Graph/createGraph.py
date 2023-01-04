
class PQueue:
    def __init__(self) -> None:
        self.queue=[]


    def add_item(self,d):
        if(len(self.queue)==0):
            self.queue.append(d)
        else:

            self.queue.append(d)
            for i in range((len(self.queue)//2)-1,-1,-1):
                self.hepify(self.queue,len(self.queue),i)

    def hepify(self,a,size,i):
        largest= i
        right= 2*i+1
        left= 2*i+2

        if(right<size and a[right]<a[largest]):
            largest= right
        if(left<size and a[left]<a[largest]):
            largest= left
        if(largest !=i):
            a[largest],a[i]= a[i],a[largest]
            self.hepify(a,size,largest)

    def remove_item(self):
        value= self.queue.pop(0)
        for i in range((len(self.queue)//2)-1,-1,-1):
            self.hepify(self.queue,len(self.queue),i)
        return value


    def show(self):
        print(self.queue)



        
            


class Graph:
    "Undirected Graph"
    def __init__(self,n):
        self.graph= {}
        self.n= n
        for i in range(n):
            self.graph[i]=[]
    def add_edge(self,v1,v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def add_edges_for_directed_graph(self,v1,v2):
        self.graph[v1].append(v2)
    def print_graph(self):
        print(self.graph)
    
        



    "leet Code Solution"
    def getPathFromNodeToAnotherNode(self,src,des):
        self.visited=[False]*self.n
        def dfs(src,des):
            print(src,end=" ")

            if(src==des):
                return True
            self.visited[src]= True
            for j in self.graph[src]:
                if(self.visited[j]==False):
                    value= dfs(j,des)
                    if(value):
                        return True
            return False
        return dfs(src,des)



    def traversal(self,src,des):
        q=[]
        q.append(src)
        visited= [False]*self.n
        visited[src]= True
        while len(q)>0:
            rm= q.pop(0)
            print(rm,end=" ")
            for next in self.graph[rm]:
                if(visited[next]== False):
                    q.append(next)
                    visited[next]= True


    def All_Path_in_undirected_graph(self,src,des):
        self.visited= [False]*self.n
        def dfs(src,des,path,paths):
            if(src==des):
                path.append(src)
                paths.append(path.copy())
                path.pop()
                return 
            self.visited[src]= True
            path.append(src)
            for j in self.graph[src]:
                if(self.visited[j]==False):
                    dfs(j,des,path,paths)
            self.visited[src]= False
            path.pop()
            return
        path,paths=[],[]
        dfs(src,des,path,paths)
        return paths

    def all_paths_in_directed_graph(self,src,des):
        self.visited= [False]*self.n
        def dfs(src,des,path,paths):
            if(src==des):
                path.append(src)
                paths.append(path.copy())
                path.pop()
                return
            self.visited[src]= True
            path.append(src)
            for j in self.graph[src]:
                if(self.visited[j]==False):
                    dfs(j,des,path,paths)
            self.visited[src]=False
            path.pop()
            return
        path,paths= [],[]
        dfs(src,des,path,paths)
        return paths

    def centerOfGraph(self):
        d={}
        for u,v in self.graph:
            d[u]= d.get(u,0)+1
            d[v]= d.get(v,0)+1
        maxValue= max(d.values())
        for k in d.keys():
            if(d[k]==maxValue):
                return k

    def minimumNumberofVerticeToReachAllNodes(self,edges):
        res= []
        uni= set({})
        for u,v in edges:
            uni.add(v)
        for j in range(len(edges)):
            if(j not in uni):
                res.append(j)
        return res
    def canVisitAllRooms(self):
        self.visited= [False]*len(self.graph)
        def dfs(src):
            self.visited[src]= True
            for child in self.graph[src]:
                if(self.visited[child]== False):
                    dfs(child)
        dfs(0)
        return all(self.visited)

    def dijkstra_Algorithm(self,graph,s,n):
        d={}
        for i in range(n):
            d[i]= []
        for u,v,w in graph:
            d[u].append((v,w))
            d[v].append((u,w))
        pq=PQueue()
        parent={}
        visited=set({})
        visited.add(s)
        dis=[float("inf")]*n
        dis[s]=0
        # pq=[]
        # heap.heappush(pq,(0,s))
        pq.add_item((0,s))
        while len(pq.queue)>0:
            # w1,node= heap.heappop(pq)
            w1,node= pq.remove_item()
            visited.add(node)
            for adj,w2 in d[node]:
                if(adj in visited):
                    continue
                if(adj not in visited):
                    newCost= dis[node]+w2
                    if(dis[adj]>newCost):
                        parent[adj]=node
                        # print(parent)
                        dis[adj]= newCost
                        # heap.heappush(pq,(newCost,adj))
                        pq.add_item((newCost,adj))

    def network_delay(self,graph,source,n):
        d={}
        for i in range(n):
            d[i]=[]
        for u,v,w in graph:
            d[u].append((v,w)) # underected graph
        distance=[float("inf")]*n+1
        distance[source]=0
        visited=set({})
        pq=PQueue()
        pq.add_item((0,source))
        time= float("-inf")
        parent= {} # add node for shortest path
        while len(pq.queue)>0:
            curr_weight,curr_node=pq.remove_item() # min-heap
            if(curr_node in visited):
                continue
            visited.add(curr_node)
            time= max(time,curr_weight)
            for next_node, next_weight in d[curr_node]:
                if(next_node in visited):
                    continue
                if(next_node not in visited):
                    update_dis= distance[curr_node]+next_weight
                    if(distance[next_node]>update_dis):
                        parent[next_node]= curr_node 
                        distance[next_node]= update_dis
                        pq.add_item((update_dis,next_node))
        return time if(len(visited)==n) else -1

    def topological(self,graph,n):
        d={}
        for i in range(n+1):
            d[i]= []
        for u,v in graph:
            d[u].append(v)
        print(d)

        def drawTree(g,i,visited,path):
            visited[i]= True
            for next_node in g[i]:
                if(visited[next_node] ==False):
                    drawTree(g,next_node,visited,path)
            path.append(i)
        visited= [False]*(n+1)
        path=[]
        for i in range(n):
            if(visited[i]==False):
                drawTree(d,i,visited,path)
    def detect_cycil_in_directed_graph(self,graph,n):
        def dfs(curr,visited,d,meet):
            visited[curr]= True
            meet[curr]= True
            for j in d[curr]:
                if(not visited[j]):
                    value= dfs(j,visited,d,meet)
                    if(value):
                        return True
                if(meet[j]):
                    return True
            meet[i]= False
            return False
        d={i:[] for i in range(n)}
        for u,v in graph:
            d[u].append(v)
        visited=[False]*n
        again_meet= [False]*n
        for i in range(n):
            if(not visited[i]):
                value= dfs(i,visited,d,again_meet)
                if(value):
                    return True
        return False
    def detect_cyil_in_undirected_graph(self,graph,n):
        def dfs(curr,visited,d,parent):
            visited[curr]= True
            for j in d[curr]:
                if not visited[j]:
                    value= dfs(j,visited,d,curr)
                    if(value):
                        return True
                if(parent !=j):
                    return True
            return False

        d={i:[] for i in range(n)}
        for u,v in graph:
            d[u].append(v)
            d[v].append(u)
        visited= [False]
        for i in range(n):
            if(not visited[i]):
                value= dfs(i,visited,d,-1)
                if(value):
                    return True
        return False

    def kahn_algorithm(self,graph,n):
        indeg= [0]*n
        d={i:[] for i in range(n)}
        for u,v in graph:
            d[u].append(v)
        # indegree of each node
        for i in range(n):
            for j in range(len(d[i])):
                indeg[d[i][j]]+=1
        q=[]
        for i in range(n):
            if(indeg[i]==0):
                q.append(i)
        ans=[]
        while len(q):
            rm= q.pop(0)
            ans.append(rm)
            for next_element in d[rm]:
                indeg[next_element]-=1
                if(indeg[next_element]==0):
                    q.append(next_element)
        print(ans)
        return ans
    # def 
    def bfs(self,graph,n):
        d= {i:[] for i in range(n)}
        for u,v in graph:
            d[u].append(v)
            # d[v].append(u)
        print(d)

        q=[]
        for i in d:
            if(len(d[i]) !=0):
                q.append(i)
                break
        stack=[]
        visited=set({})
        while len(q)>0:
            rm= q.pop(0)
            if(rm in visited): # not add duplicate items
                continue
            visited.add(rm)
            stack.append(rm)
            for j in d[rm]:
                if(j not in visited):
                    q.append(j)

        print(stack)
    def dfs(self,graph,n):
        d= {i:[] for i in range(n)}
        for u,v in graph:
            d[u].append(v)
            # d[v].append(u)
        
        def dfs_traversal(d,i,visited,stack):
            visited[i]= True
            stack.append(i)
            for edge in d[i]:
                if not visited[edge]:
                    dfs_traversal(d,edge,visited,stack)
        stack=[]
        visited= [False]*n
        dfs_traversal(d,0,visited,stack)
        print(stack)

    def search_element_in_graph(self,graph,n,value):
        d= {i:[] for i in range(n)}
        for u,v in graph:
            d[u].append(v)
            d[v].append(u)
        def search_in_dfs(d,i,visited,stack,value):
            visited[i]= True
            if(i==value):
                return True
            stack.append(i)
            for edge in d[i]:
                if not visited[edge]:
                    value=search_in_dfs(d,edge,visited,stack,value)
                    if(value):
                        return True
            return False
        stack=[]
        visited=[False]*n
        res= search_in_dfs(d,0,visited,stack,value)
        return res

    def bfs_in_undirected_graph(self,graph,n):
        d={i:[] for i in range(n)}
        for u,v in graph:
            d[u].append(v)
        s1=[]
        def bfs(i,visited,d,path):
            q=[]
            q.append(i)
            visited=set({})
            while len(q)>0:
                rm= q.pop(0)
                if(rm in visited):
                    continue
                visited.add(rm)
                for edge in d[rm]:
                    if(edge not in visited):
                        q.append(edge)
            path.append(visited)
            return visited
        visited=[False]*n
        stack=[]
        for i in range(n):
            if(not visited[i]):
                path=[]
                value=bfs(i,visited,d,path)
                stack.append(value)
        print(stack)

    def dfs_in_undirected_graph(self,graph,n):
        d={i:[] for i in range(n)}
        for u,v in graph:
            d[u].append(v)
        stack=[]
        def dfs(i,visited):
            visited[i]= True
            stack.append(i)
            for edge in d[i]:
                if(not visited[edge]):
                    dfs(edge,visited)
        visited=[False]*n
        for i in range(n):
            if(not visited[i]):
                dfs(i,visited)
        print(stack)

    def cycil_in_graph(self,graph):
        def isCyclic(i,visited,graph):
            visited[i]=True
            for u in graph[i]:
                pass
        n= len(graph)
        visited=[False]*n
        for i in range(n):
            if(isCyclic(i,graph)):
                return True
        return False

    def get_ancesters_directed_graph(self,graph,n):
        d={i:[] for i in range(n)}
        ans=[[] for i in range(n)]
        for u,v in graph:
            d[u].append(v)
        def dfs(i,ancester, visited,d,ans):
            visited.add(i)
            for u in d[i]:
                if(u not in visited):
                    ans[u].append(ancester)
                    dfs(u,ancester,visited,ans)
        
        for i in range(n):
            dfs(i,i,set(),d,ans)
        return ans






        




        
        




        

            

            






        

            

 
        

            
            


g= Graph(5)
# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(1,2)
# g.add_edge(2,3)
# g.add_edge(3,4)
# g.add_edge(3,1)
# g.add_edge(1,4)
# g.print_graph()
# print(g.getPathFromNodeToAnotherNode(0,4))
# g.traversal(0,4)
g.add_edges_for_directed_graph(1,2)
g.add_edges_for_directed_graph(1,3)
g.add_edges_for_directed_graph(3,4)
g.add_edges_for_directed_graph(2,4)
# print(g.print_graph())
# print(g.all_paths_in_directed_graph(1,4))
# g.dijkstra_Algorithm([[0,1,10],[0,2,20],[1,3,30],[2,3,40]],0,4)
# g.dijkstra_Algorithm([[0,1,2],[0,2,1],[1,4,8],[1,5,4],[1,2,7],[2,5,3],[2,3,7],[3,4,8],[5,4,5],[5,3,4]],0,6)
# g.topological([[0,1],[0,3],[1,2],[2,3],[4,3],[4,5],[4,6],[5,6]],6)
# g.kahn_algorithm([[0,1],[2,0],[1,3],[3,2]],4)
# g.bfs([[0,1],[3,0],[2,3],[2,1],[4,1],[4,5],[5,6],[4,6]],7)
# g.dfs([[0,1],[0,2],[1,3],[2,4],[3,4],[3,5]],6)
# g.dfs([[0,1],[3,0],[2,3],[2,1],[4,1],[4,5],[5,6],[4,6]],7)
g.bfs_in_undirected_graph([[0,1],[3,0],[2,3],[2,1],[4,1],[4,5],[5,6],[4,6]],7)
g.dfs_in_undirected_graph([[0,1],[3,0],[2,3],[2,1],[4,1],[4,5],[5,6],[4,6]],7)
# g.search_element_in_graph([[0,1],[0,2],[1,3],[2,4],[3,4],[3,5]],6,400)


    



a=[1,2,3,4,5,7]
# print(a)
# for i in range(len(a)):
#     a[i]-=1
# print(a)

# def f1(value):
#     return value&1==0
# a= [1,2,3,4,5,6]
# print(list(map(f1,a)))

# def solve(self, A, B):
#     n= len(A)-1
#     sum=0
#     j=0
#     for a,b in zip(A,B):
#         sum +=(a* j+ b*n-j )
#         j+=1
#         # print(sum)
#     return sum

# print()