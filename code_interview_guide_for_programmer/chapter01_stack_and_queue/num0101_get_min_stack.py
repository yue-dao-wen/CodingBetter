class MinStack:
    def __init__(self):
        self.nums = []
        self.mins = []
        pass

    def pop(self):
        num = self.nums.pop()
        self.mins.pop()
        return num

    def push(self, num):
        # todo:
        self.nums.append(num)
        if not self.mins:
            self.mins.append(num)
            return

        if num <= self.mins[-1]:
            self.mins.append(num)
        else:
            self.mins.append(self.mins[-1])

    def get_min(self):
        return self.mins[-1]


def main():

    ops = ['push', 'push', 'pop', 'get_min']
    nums = [3, 4, 0, 0]
    # 数字越来越大
    # ops = ['push', 'get_min', 'push', 'get_min', 'push', 'get_min']
    # nums = [3, '', 4, '', 5, '']
    # 数字越来越小
    ops = ['push', 'get_min', 'push', 'get_min', 'push', 'get_min', 'pop', 'get_min']
    nums = [5, '', 4, '', 3, '', '', '']

    min_stack = MinStack()
    for i, op in enumerate(ops):
        if op == 'push':
            min_stack.push(nums[i])
        elif op == 'pop':
            print(min_stack.pop())
        elif op == 'get_min':
            print(min_stack.get_min())

    pass


if __name__ == '__main__':
    main()
