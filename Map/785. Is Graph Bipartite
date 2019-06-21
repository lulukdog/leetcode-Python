class Solution:
    def isBipartite(self, graph):
        u = [i for i in range(len(graph))]

        def find(i):
            return i if u[i]==i else find(u[i])

        for i in range(len(graph)):
            if len(graph[i])==0:
                continue

            x = find(i)
            y = find(graph[i][0])
            if x==y: 
                return False
            for j in range(1,len(graph[i])):
                p = find(graph[i][j])
                if x==p: 
                    return False
                u[p] = y

        return True
