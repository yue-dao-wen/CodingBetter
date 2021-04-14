class Node:
    def __init__(self, char=None, val=0, nex=(), is_end=False):
        self.char = char
        # TODO: is_end 和val 是不是能整合到一个变量里面？
        self.val = val
        self.nex = {node.val: i for i, node in enumerate(nex)}
        self.is_end = is_end


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, key: str, val: int) -> None:
        cur_node = self.root
        for c in key:
            if c not in cur_node.nex:
                cur_node.nex[c] = Node(c)
            cur_node = cur_node.nex[c]
        cur_node.is_end = True
        cur_node.val = val
        pass

    def sum(self, prefix: str) -> int:
        ans = 0
        len_prefix = len(prefix)
        cur_node = self.root

        # def dfs(node, idx):
        #     if idx == len_prefix - 1:
        for c in prefix:
            if c not in cur_node.nex:
                return ans
            cur_node = cur_node.nex[c]

        stack = [cur_node]
        while stack:
            node = stack.pop()
            ans += node.val if node.is_end else 0
            stack.extend(list(node.nex.values()))

        return ans


if __name__ == '__main__':

    ops = ["MapSum", "insert", "sum", "insert", "sum"]
    key_val_pairs = [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]

    map_sum = None
    for i, op in enumerate(ops):
        if op == "MapSum":
            map_sum = MapSum()
        elif op == "insert":
            print(map_sum.insert(key_val_pairs[i][0], key_val_pairs[i][1]))
        elif op == "sum":
            print(map_sum.sum(key_val_pairs[i][0]))
        else:
            print("Wrong operation.")
