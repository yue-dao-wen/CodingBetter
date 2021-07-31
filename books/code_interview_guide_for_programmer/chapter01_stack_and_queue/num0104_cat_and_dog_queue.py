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


def main():
    pets_type = ["cat", "dog", "cat", "cat", "dog", "dog", "dog", "cat"]
    pet_q = PetQueue()
    for pet_type in pets_type:
        pet_q.add(pet_type)

    pet_q.poll_all()
    pet_q.poll_dog()
    pet_q.poll_cat()


if __name__ == '__main__':
    main()
