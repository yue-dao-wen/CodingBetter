from typing import List

class Node:
    def __init__(self, char=None, nex=(), is_end=False):
        self.char = char
        self.nex = nex
        self.is_end = is_end

class Trie:
    def __init__(self):
        self.root = Node

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


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = []

        # TODO: 把谁装进树里面？
        trie = Trie()
        for root in dictionary:
            trie.insert(root)

        sentence = sentence.split(' ')
        for word in sentence:
            # TODO：还没整完
            pass





        ans = " ".join(ans)
        return ans




if __name__ == '__main__':
    sl = Solution()

    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(sl.replaceWords(dictionary, sentence))


