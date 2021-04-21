# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/4/21 19:16
"""


class Queue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def add(self, num):
        self.stack_in.append(num)
        print(f"added: {num}")

    def pop(self):
        if self.is_empty():
            print("the queue is empty")
            return -1
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        res = self.stack_out.pop()
        return res

    def is_empty(self):
        res = not self.stack_in and not self.stack_out
        return res

    def head(self):
        if self.is_empty():
            print("the queue is empty")
            return -1
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        res = self.stack_out[-1]
        return res

    def tail(self):
        if self.is_empty():
            print("the queue is empty")
            return -1
        if self.stack_in:
            res = self.stack_in[-1]
        else:
            res = self.stack_out[0]
        return res


def main():
    q = Queue()
    q.add(1)
    q.add(2)
    print(q.pop())
    q.add(3)
    q.add(4)
    print(q.pop())
    print(q.pop())

    pass


if __name__ == "__main__":
    main()
