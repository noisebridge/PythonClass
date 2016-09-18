from example_tree import letter_tree
from utils import is_word


def depth_first_search(tree, target):
    """
    Exercise 1: Implement your depth first search algorithm here

    The 'tree' parameter contains 'tree.left' and 'tree.right'
    child elements - they may be unset (None) if the node does
    not have left or right children.
    """
    return None

def breadth_first_search(tree, target):
    """
    Exercise 2: Implement your depth first search algorithm here

    Breadth-first search should check the root node first, then each of
    the items at the first level in the tree, then each item at the second
    level, and so on.
    """
    return None

def word_search(tree):
    """
    Exercise 2: Implement a word search using either DFS or BFS.
    Why did you choose one algorithm or the other?
    """
    return None


if __name__ == '__main__':
    dfs_result = depth_first_search(letter_tree, 'f')
    print('Depth first search result: {}'.format(dfs_result))

    bfs_result = breadth_first_search(letter_tree, 'l')
    print('Breadth first search result: {}'.format(bfs_result))

    word_results = word_search(letter_tree)
    print('Word search results: {}'.format(word_results))
