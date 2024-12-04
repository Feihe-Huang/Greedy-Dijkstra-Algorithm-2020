# define the function named dijkstra() to get the shortest path between any two vertices
# I learned this algorithm from https://gist.github.com/kachayev/5990802
import sys
from collections import defaultdict
from heapq import *

def get_route(edges, f, t):  # this code is used to define the function using the dijkstra algorithm
	g = defaultdict(list)
	for l, r, c in edges:
		g[l].append((c, r))
	q, seen, mins = [(0, f, [])], set(), {f: 0}
	while q:
		(cost, v1, path) = heappop(q)
		if v1 not in seen:
			seen.add(v1)
			path = [v1] + path
			if v1 == t:
				return (cost, path)

			for c, v2 in g.get(v1, ()):
				if v2 in seen:
					continue
				prev = mins.get(v2, None)
				next = cost + c
				if prev is None or next < prev:
					mins[v2] = next
					heappush(q, (next, v2, path))
	return (float("inf"), [])
