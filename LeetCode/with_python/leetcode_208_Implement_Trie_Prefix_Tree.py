class Node:
    def __init__(self, char=None, nex=(), is_end=False):
        self.char = char
        self.nex = {node.val: i for i, node in enumerate(nex)}
        self.is_end = is_end


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        for c in word:
            if c not in cur_node.nex:
                cur_node.nex[c] = Node(c)
            cur_node = cur_node.nex[c]
        cur_node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root
        for c in word:
            if c not in cur_node.nex:
                return False
            cur_node = cur_node.nex[c]
        return cur_node.nex[word[-1]].is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root
        for c in prefix:
            if c not in cur_node.nex:
                return False
            cur_node = cur_node.nex[c]
        return True


if __name__ == '__main__':
    ops = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    words = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

    trie = None
    for i, op in enumerate(ops):
        if op == "Trie":
            trie = Trie()
            pass
        elif op == "insert":
            print(trie.insert(words[i][0]))
            pass
        elif op == "search":
            print(trie.search(words[i][0]))
            pass
        elif op == "startsWith":
            print(trie.startsWith(words[i][0]))
            pass
        else:
            print("Wrong operation.")
