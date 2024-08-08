# Graph

When using dfs to traverse a graph, we have to keep track of the visited node, so we don't fall into endless loop.

**[Walls and Gates](./286_walls_and_gates.py)**
We can both use dfs or bfs. 

### DFS
- Its principle of recursion is using stack. 
- It suits find the longest path in a graph.

### BFS
- Its principle of traverse level by level is using queue.
- It suits find the shortest path in an unweighted grah.
  - Picture BFS traverse the graph by waves, so it's outward propagation natural that the shortest path will be found first.