#### Tree Search Algorithms

## About Trees

Trees are an extremely common data-structure in software; they're very
useful for representing hierarchical relationships (like the folders or
directories on your hard disk, or a chart of a large organization's structure).

Most trees like those in the examples above contain no 'order' in the tree;
that is, if I asked you to find a file named 'test.py', it's hard to tell
just by looking at the folder names where that file will be; you would have
to open a few (or maybe all) of them to find it.  We're going to write code
to do this automatically - these are called 'tree search algorithms'.

Our tree search algorithms will _traverse_ the tree to find items we're
looking for.  The two most common algorithms for tree traversal are
Depth-First Search (DFS) and Breadth-First Search (BFS), and we'll look at
both.


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
