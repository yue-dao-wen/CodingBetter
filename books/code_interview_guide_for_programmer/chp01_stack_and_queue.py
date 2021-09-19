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

from collections import deque


class Pet:
    def __init__(self, type):
        self.type = type

    def get_pet_type(self):
        return self.type


class Dog(Pet):
    def __init__(self):
        Pet.__init__(self, 'dog')


class Cat(Pet):
    def __init__(self):
        Pet.__init__(self, "cat")


class PetWithTime:
    def __init__(self, pet, time):
        self.pet = pet
        self.time = time

    def get_time(self):
        return self.time


class PetQueue():
    def __init__(self):
        self.count = 0
        self.dog_que = deque([])
        self.cat_que = deque([])

    def add(self, type):
        if type == 'cat':
            self.count += 1
            new_cat = Cat()
            cat_t = PetWithTime(new_cat, self.count)
            self.cat_que.append(cat_t)

        elif type == 'dog':
            self.count += 1
            new_dog = Dog()
            dog_t = PetWithTime(new_dog, self.count)
            self.dog_que.append(dog_t)

        else:
            print("Unknown type.")

    def poll_all(self):
        if self.cat_que and self.dog_que:
            if not self.cat_que:
                # 弹出所有dog
                self.poll_dog()

            elif not self.dog_que:
                # 弹出所有cat
                self.poll_cat()

            else:
                # 按时间戳弹出
                while self.dog_que and self.cat_que:
                    dog_t = self.dog_que[0]
                    cat_t = self.cat_que[0]
                    if dog_t.time <= cat_t.time:
                        dog_t = self.dog_que.popleft()
                        print(f"{dog_t.pet.get_pet_type()}, {dog_t.time}")
                    else:
                        cat_t = self.cat_que.popleft()
                        print(f"{cat_t.pet.get_pet_type()}, {cat_t.time}")
                if self.dog_que:
                    self.poll_dog()
                if self.cat_que:
                    self.poll_cat()

    def poll_dog(self):
        while self.dog_que:
            dog = self.dog_que.popleft()
            print(f"{dog.pet.get_pet_type()}, {dog.time}")

    def poll_cat(self):
        while self.cat_que:
            cat = self.cat_que.popleft()
            print(f"{cat.pet.get_pet_type()}, {cat.time}")


def run_cat_and_dog_queue():
    pets_type = ["cat", "dog", "cat", "cat", "dog", "dog", "dog", "cat"]
    pet_q = PetQueue()
    for pet_type in pets_type:
        pet_q.add(pet_type)

    pet_q.poll_all()
    pet_q.poll_dog()
    pet_q.poll_cat()


def run_min_stack():

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
