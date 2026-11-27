import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]
        dist = {}

        while heap:
            d, node = heapq.heappop(heap)
            if node in dist: continue
            dist[node] = d
            for nei, w in graph[node]:
                heapq.heappush(heap, (d + w, nei))

        if len(dist) != n: return -1
        return max(dist.values())