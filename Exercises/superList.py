class SuperList(list):
    def __init__(self, iterable):
        super().__init__(iterable)

    def __len__(self):
        return 1000

test_list = [1, 2, 3, 4, 5, 6, 7]
super_list1 = SuperList(test_list)

super_list1.append(1)
print(super_list1)
print(len(super_list1))