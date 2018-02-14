from example_tree import letter_tree
from utils import is_word


def depth_first_search(tree, target):
    """
    Exercise 1: Implement your depth first search algorithm here
    """
    if tree is None:
        return None
    print("DFS: Checking node with value '{}'".format(tree.value))
    if tree.value == target:
        return tree
    return depth_first_search(tree.left, target) \
        or depth_first_search(tree.right, target)

def breadth_first_search(tree, target):
    """
    Exercise 2: Implement your depth first search algorithm here
    """
    nodes = [tree]
    while nodes:
        node = nodes.pop(0)
        print("BFS: Checking node with value '{}'".format(node.value))
        if node.value == target:
            return node
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

def word_search(tree, string=''):
    """
    Exercise 2: Implement a word search using either DFS or BFS.
    Why did you choose one algorithm or the other?
    """
    if tree is None:
        return []

    string += tree.value

    results = []
    if is_word(string):
        results.append(string)

    results += word_search(tree.left, string)
    results += word_search(tree.right, string)

    return results


if __name__ == '__main__':
    dfs_result = depth_first_search(letter_tree, 'f')
    print('Depth first search result: {}'.format(dfs_result))

    bfs_result = breadth_first_search(letter_tree, 'l')
    print('Breadth first search result: {}'.format(bfs_result))

    word_results = word_search(letter_tree)
    print('Word search results: {}'.format(word_results))
