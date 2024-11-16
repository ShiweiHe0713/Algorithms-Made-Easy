# Graph

## Choice of BFS or DFS

### **BFS Problems**

1. **Shortest Path in Unweighted Graph**
   - **Problem**: [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
   - **Problem**: [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

2. **Minimum Steps or Distance**
   - **Problem**: [752. Open the Lock](https://leetcode.com/problems/open-the-lock/)
   - **Problem**: [127. Word Ladder](https://leetcode.com/problems/word-ladder/)

3. **Level-Order Traversal**
   - **Problem**: [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
   - **Problem**: [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

4. **Connected Components in Unweighted Graphs**
   - **Problem**: [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
   - **Problem**: [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)

### **DFS Problems**

1. **Detecting Cycles**
   - **Problem**: [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
   - **Problem**: [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)

2. **Topological Sorting**
   - **Problem**: [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

3. **Path Finding in Directed Graphs**
   - **Problem**: [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/)

4. **Backtracking Problems**
   - **Problem**: [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
   - **Problem**: [46. Permutations](https://leetcode.com/problems/permutations/)

5. **Finding Strongly Connected Components**
   - **Problem**: [1192. Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/)
   - **Problem**: [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

### **Either BFS or DFS Problems**

1. **Connected Component Counting (Undirected Graph)**
   - **Problem**: [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)

2. **Graph Traversal without Specific Path Constraints**
   - **Problem**: [733. Flood Fill](https://leetcode.com/problems/flood-fill/)

3. **Flood Fill Problems**
   - **Problem**: [733. Flood Fill](https://leetcode.com/problems/flood-fill/)
   - **Problem**: [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) (works well with either BFS or DFS)



## Dijkastra





## Connected component

1. Keep a visited set to keep track of the visited node
2. Whenever we visit a node that's not been visited before, we will increase number of components by 1, and use dfs to mark all the nodes in the component as visited. Thus, each component will only be visited once and correcly calculated.



## Topological sort

- A topological sort of a directed acyclic graph (DAG) is a linear ordering of its vertices such that for every directed edge `u -> v`, **`u` comes before `v` in the ordering.**
- Topological sort by dependencies, not by depth/absolute level of a tree/graph. For example, the node at depth 3 can appear before a node at node of depth 2.
  

- [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
  - we are running topo sort on each component to detect cycle.



## Bipartite





## DAG vs Non-DAG

We will come across DAG(like [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/)) or Non-DAG([200. Number of Islands](https://leetcode.com/problems/number-of-islands/description/)). The difference is we don't have to use a visited set on a DAG, but most the cases we will need a visited set on Non-DAG problem.

### DAG 

Typical questions like **all path** and **combinations**, backtracking is needed and visited set is not needed.



### Other graphs

**When we need a `visited` set:**

- **The graph has cycles**, and revisiting nodes could cause infinite loops.
- **Each node can only be visited once per path**, or there's a restriction that disallows revisiting nodes.



When using dfs to traverse a graph, we have to keep track of the visited node, so we don't fall into endless loop.

**[Walls and Gates](./286_walls_and_gates.py)**
We use bfs for this problem, and it's a multi-source bfs problem.



## Problems
In [130. Surrounded Regions](./130_surrounded_regions.py), we can spare the time and space complexity of a visited set by changing cells in-place, like marking them to 'E'.

In [399 Evaluate Division](./399_evaluate_division.py), 

In [785 Is graph bipartite](./785_is_graph_bipartite.py), we use a `color` as a visited set and also store the color for each node.

In [694 number of distinct islands](./694_number_of_distinct_islands.py), 