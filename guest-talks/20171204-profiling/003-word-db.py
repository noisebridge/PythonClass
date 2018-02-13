import sys



class Trie(object):

    class Node(object):

        def __init__(self):
            self.children = {}
            self.terminal = False

    def __init__(self):
        self.root = Trie.Node()

    def _traverse(self, string, create_missing=False):
        """
        Navigate through the trie one character at a time
        until we find a matching node.  If create_missing
        is set, then we will also create new node entries
        where items were missing
        """
        if not string:
            return

        # Start at the root node, and split the input string
        node = self.root
        head, tail = string[0:1], string[1:]

        while node and head:

            # Create any missing child entries
            if head not in node.children and create_missing:
                node.children[head] = Trie.Node()

            # Try to find a matching child node
            match = None
            for key in node.children:
                if key == head:
                    match = node.children[key]
            node = match

            # Move to the next character in the string
            head, tail = tail[0:1], tail[1:]

        return node


    def insert(self, string):
        node = self._traverse(string, create_missing=True)
        node.terminal = True

    def contains(self, string):
        node = self._traverse(string)
        return node is not None and node.terminal


class WordDatabase(object):

    def __init__(self):
        self.trie = Trie()

    def load(self, filename):
        for line in open(filename).readlines():
            word = line.strip()
            self.trie.insert(word)

    def query(self):
        while True:
            try:
                line = raw_input()
            except EOFError:
                return
            for word in line.split(' '):
                print self.trie.contains(word)



word_file = sys.argv[1]
word_database = WordDatabase()
word_database.load(word_file)
word_database.query()
