def dijsktra(dist, target_node, distances, prev, Q):
    while True:
        if not Q: break
        dist_in_q = {nod: dist[nod] for nod in Q}
        u = min(dist_in_q)
        if u == target_node:
            return dist, prev
        Q = tuple(node for node in Q if node != u)
        for v in Q:
            if v not in distances[u]: continue
            alt = dist[u] + distances[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev


def shortest_path(nodes, initial_node, target_node, distances, prev, Q, dist):
    dist, prev = dijsktra(dist, target_node, distances, prev, Q)
    current = target_node
    path = []
    if prev[target_node] is None:
        return 'No path'
    while current != initial_node:
        path = [current] + path
        current = prev[current]
    path = [initial_node] + path
    return path


nodes = ('a', 'b', 'c', 'd')
distances = {
    'a': {'b': 3, 'c': 5, 'd': 11},
    'b': {'a': 3, 'd': 2},
    'c': {'a': 5, 'b': 4, 'd': 7},
    'd': {'a': 11, 'b': 6, 'c': 7}

}
initial_node = 'a'
target_node = 'd'
unvisited = {node: None for node in nodes}
prev = {node: None for node in nodes}
dist = {node: float('inf') for node in nodes}
dist[initial_node] = 0
Q = nodes
shortest_path(nodes, initial_node, target_node, distances, prev, Q, dist)