"""
1 solution
Greedy Algorithm

time O(nlogn) space O(1)
"""




"""
LeetCode Solution has a very nice explanation about GREEDY ALGORITHM:

Greedy problems usually look like "Find minimum number of something to do something" or "Find maximum number of something to fit in some conditions", and typically propose an unsorted input.

The idea of greedy algorithm is to pick the locally optimal move at each step, that will lead to the globally optimal solution.

The standard solution has \mathcal{O}(N \log N)O(NlogN) time complexity and consists of two parts:

1. Figure out how to sort the input data (\mathcal{O}(N \log N)O(NlogN) time). That could be done directly by a sorting or indirectly by a heap usage. Typically sort is better than the heap usage because of gain in space.

2. Parse the sorted input to have a solution (\mathcal{O}(N)O(N) time).
"""