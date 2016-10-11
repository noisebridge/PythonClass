class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


letter_tree = \
  Node('a',
    Node('p',
      Node('p',
        Node('d',
          None,
          Node('f'),
        ),
        Node('l',
          None,
          Node('e'),
        ),
      ),
      Node('e',
        Node('f'),
        Node('r'),
      ),
    ),
    Node('b',
      Node('l',
        Node('e'),
        Node('k'),
      ),
    ),
  )
