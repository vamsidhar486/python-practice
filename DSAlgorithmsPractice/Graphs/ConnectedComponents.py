def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        graph = {i: set() for i in range(n)}

        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)

        seen = set()
        count = 0

        def bfs(node):
            queue = [node]
            for n in queue:
                for nei in graph[n]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)

        for i in range(n):
            if i not in seen:
                bfs(i)
                count += 1

        return count