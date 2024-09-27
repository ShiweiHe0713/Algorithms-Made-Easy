# Graph
**table of contents**
- [Graph](#graph)
    - [DFS](#dfs)
    - [BFS](#bfs)
  - [Problems](#problems)

When using dfs to traverse a graph, we have to keep track of the visited node, so we don't fall into endless loop.

**[Walls and Gates](./286_walls_and_gates.py)**
We use bfs for this problem, and it's a multi-source bfs problem.


## Problems
In [130. Surrounded Regions](./130_surrounded_regions.py), we can spare the time and space complexity of a visited set by changing cells in-place, like marking them to 'E'.

In [399 Evaluate Division](./399_evaluate_division.py), 

In [785 Is graph bipartite](./785_is_graph_bipartite.py), we use a `color` as a visited set and also store the color for each node.

In [694 number of distinct islands](./694_number_of_distinct_islands.py), 