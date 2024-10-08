**Recursion call with a return statement VS those don't**
- What is the difference between the dfs function that has a return with those that don't have a return in addition to the returns in the base cases?

In [Coin change brute force](../10_dp/322_coin_change.py), we can write use `nonlocal` to modify min_change in the dfs body or we can pass `coin_used` as a formal argument in the dfs function. For the former, we don't have to return anything in the recursive body since we merely modify the global variables. But for the latter we'll have to return in both base case and recurisve body.
```python
def coinChange_bf(self, coins: List[int], amount: int) -> int:

        def dfs(left_amount: int, coin_used: int) -> int:
            if left_amount < 0:
                return float('inf')
            if left_amount == 0:
                return coin_used
            
            min_change = float('inf')
            for coin in coins:
                min_change = min(min_change, dfs(left_amount - coin, coin_used + 1))
            return min_change

        min_change = dfs(amount, 0)

        return min_change if min_change != float('inf') else -1
```
The difference between a DFS (Depth-First Search) function that has a return statement in the recursive calls and those that only have return statements in the base cases lies in **how they handle control flow and how they propagate results back up the recursive call stack**. This difference can significantly affect the behavior and correctness of the algorithm.

### Two types of recursion
- **Return-Based recursion**: Suitable when results from subproblems need to be combined. It allows you to compute values like sums, maximums, or find paths based on conditions.
- **Non-Return-Based recursion**: Useful when the goal is to simply traverse the structure or when the results are maintained through side effects, not needing to pass results explicitly through recursive calls.

### Summary of Key Differences
**Control Flow:**
- Return-Based: Allows returning from the function early and passing results directly up the call stack.
- Non-Return-Based: Continues execution regardless of intermediate results, relying on external state changes.

**Result Propagation:**
- Return-Based: Results are propagated up the call stack and used to make further decisions.
- Non-Return-Based: Results are not explicitly passed; rather, they are accumulated through side effects.

**State Management:**
- Return-Based: State is managed through return values and local variables.
- Non-Return-Based: State is managed through external or global variables, which might introduce dependencies.