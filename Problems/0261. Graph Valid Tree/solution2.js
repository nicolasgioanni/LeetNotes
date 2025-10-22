// valid tree: n nodes labeled 0..n-1, edges as [[u,v], ...]
function validTree(n, edges) {
  // Necessary condition for a tree
  if (edges.length !== n - 1) return false;

  // Build undirected adjacency list
  const graph = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) {
    graph[u].push(v);
    graph[v].push(u);
  }

  const visited = new Array(n).fill(false);

  // DFS with parent tracking to detect cycles
  function hasCycle(node, parent) {
    if (visited[node]) return true; // revisit => cycle
    visited[node] = true;

    for (const nei of graph[node]) {
      if (nei === parent) continue; // skip the edge we came from
      if (hasCycle(nei, node)) return true;
    }
    return false;
  }

  if (hasCycle(0, -1)) return false;

  // Connectivity check: all nodes must be visited
  for (const v of visited) if (!v) return false;

  return true;
}
