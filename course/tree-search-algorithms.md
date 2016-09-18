#### Tree Search Algorithms

## About Trees

Trees are an extremely common data-structure in software; they're very
useful for representing hierarchical relationships (like the folders or
directories on your hard disk, or a chart of a large organization's structure).

If we are lucky, then a tree can be 'ordered' - binary trees are a common
example.  For these, we can determine where to find or place any item by
comparing it to the root node, and if it's smaller, looking down to the 'left'
of the tree, or if it's larger, to the 'right'.

This class will focus on trees without order, where we need to /traverse/ the
tree to find items we're looking for.  The two most common algorithms for
tree traversal are Depth-First Search (DFS) and Breadth-First Search (BFS).


## Depth-First Search

A depth-first search traversal navigates all the way to the leaf nodes of our
tree.  This is a perfect fit for a recursive function:

* Is the current node the one we are looking for?
* If so, return the current node
* If not, repeat on both the left and then the right children

Let's try to code this up in Python using the file 'exercise.py' which
has placeholders for our code:

```
virtualenv venv
source venv/bin/activate
pip install pyenchant
python exercise.py
```
