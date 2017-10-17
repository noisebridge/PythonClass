# Implementing Algorithms in Python

Class outline:

- Data structures literals review
- Bubble Sort
- Topological Sort
- Graph search: breadth-first search (BFS) and depth-first search (DFS)

## Data structure literals review

### List: ordered, variable length

```python
>>> numbers = [1, 2, 3, 1]
>>> numbers[0]
1
```

### Dictionary (dict): unordered; maps key to value

```python
>>> color_codes = {
...    'red': '#ff0000',
...    'orange': '#ffa500',
...    'yellow': '#ffff00'
... }
>>> color_codes['red']
'#ff0000'
```

### Set: unordered, unique:


```python
>>> fruits = {'apple', 'banana'}
>>> fruits[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
>>> 'apple' in fruits
True
```


0. Warm Up: "Is Sorted"

```python
>>> def is_sorted(l):
...     max_comparison = len(l) - 1
...
...     for index in range(max_comparison):
...         if l[index] > l[index + 1]:
...             return False

...     return True

>>> is_sorted(numbers)
False
>>> is_sorted([])
True
```

1. [Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort)

This is an inefficient but easy to implement sorting algorithm.

Starting at the beginning of the list, we compare the first 2 elements.
If they are out of order, swap them.
When we get to the end of the list, if something was swapped, the list might not be sorted yet, so we repeat.
Once we make a pass through the list without anything being swapped, we are done.

```python
def bubble_sort(l):
    max_index = len(l)

    while True:
        swapped = False
        for index in range(max_index):
            if l[index] < l[index + 1]:
                l[index], l[index + 1] = l[index + 1], l[index]
                swapped = True

        if not swapped:
            break
```


Our implementation of Bubble Sort mutates the input list - by the end of the algorithm the list is sorted.
The unsorted list is no longer accessible!

We can copy the list before we sort it, but in practice the `sorted` builtin,
which we should really be using, returns a copy of the list.

2. [Topological Sort](https://en.wikipedia.org/wiki/Topological_sorting)

Finds an ordering that satisfies dependencies.
These are relatively common in real-world applications!

Let's pretend we're a laundry startup. Here's a dependency graph in English:

- Before you return the clothes, wash and dry them.
- Before you wash the clothes, add the detergent.
- Before you dry the clothes, wash them.

and in Python:

```python
graph = {
    'return': {'wash', 'dry'},
    'wash': {'detergent'},
    'detergent': set(),  # Note that {} would be an empty dict, not a set
    'dry': {'wash'}
}
```

The algorithm we'll implement, Kahn's algorithm, is efficient, yet easy to understand.

- Find anything without dependencies
- Until there are no more nodes without dependencies:
  - Add a node from this set to the solution
  - Remove any dependencies from the node from the graph

In the case of laundry, we start by noticing `'detergent'` can be the first in our solution as it has no dependencies.

Then, we remove `'detergent'` from any dependencies because it can now be considered complete. Our updated graph looks like this:

```python
solution = ['detergent']
graph = {
    'return': {'wash', 'dry'},
    'wash': set(),
    'detergent': set(),
    'dry': {'wash'}
}
```

At this point, `'wash'` has no dependencies and it is part of the solution.

```python
solution = ['detergent', 'wash']
graph = {
    'return': {'dry'},
    'wash': set(),
    'detergent': set(),
    'dry': set()
}
```

If we run out of nodes that have no dependencies, we raise an error as there is no way to satisfy the dependencies.

```python
>>> def toposort(g):
...      l = []
...      s = {n for n in g if not g[n]
...      while s:
...          n = s.pop()
...          l.append(n)
...          for m in {m for m in g if n in g[m]}:
...              g[m].remove(n)
...              if not g[m]:
...                  s.add(m)
...      if any(g.values())
...          raise ValueError('No solution')
...      return l
```

Again, this mutates the graph, so make a copy before calling this implementation.

There's no builtin for this algorithm, but you can find [toposort](https://pypi.python.org/pypi/toposort) on the Python Package Index (pypi).

3. Graph search: depth-first and breadth-first search

Let's use the US state borders as an example graph this time. We can get the bordering states from https://state.1keydata.com/bordering-states-list.php.


```python
>>> borders = """<paste>"""

>>> def build_graph():
...     graph = {}
...     lines = borders.split('\n')
...     for line in lines:
...         state, edges = line.split('\t')
...         graph[state] = {edge for edge in edges.split(', ') if '(water border)' not in edge}
...     return graph
>>> g = build_graph()
```

```python
>>> def dfs(start, g):
...     queue = [start]
...     seen = []
...     while queue:
...         node = queue.pop()
...
...            if node not in seen:
...                seen.append(node)
...                queue += g[node] - set(seen)
...     return seen
>>>
>>> def bfs(start, g):
...     queue = [start]
...     seen = []
...     while queue:
...         node = queue.pop()
...
...            if node not in seen:
...                seen.append(node)
...                queue += g[node] - set(seen)
...     return seen

>>> bfs('California', g))
```

Also see: http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

### Bonus: [networkx](https://github.com/networkx/networkx)

Provides a Graph class and just about every graph algorithm imaginable.

You can even make networkx draw your graph:

```python
>>> import matplotlib.pyplot as plt
>>> from networkx import nx
>>> G = nx.Graph(g)

nx.draw(G, with_labels=True)
plt.show()
```
