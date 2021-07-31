from data_struct import build_link_list


def print_common_node(l1, l2):
    res = []
    n1, n2 = l1, l2
    while n1 and n2:
        if n1.val == n2.val:
            res.append(str(n1.val))
            n1, n2 = n1.next, n2.next
        elif n1.val < n2.val:
            n1 = n1.next
        elif n1.val > n2.val:
            n2 = n2.next

    print(" ".join(res))

    pass


if __name__ == '__main__':
    # l1 = [1, 2, 3]
    # l2 = [2, 3, 4, 5]

    # l1 = []
    # l2 = [1, 2, 3]

    # l1 = [1, 2, 3]
    # l2 = []

    l1 = [5, 6, 7]
    l2 = [1, 2, 3]

    l1 = build_link_list(l1)
    l2 = build_link_list(l2)

    print_common_node(l1, l2)
