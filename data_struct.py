class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def build_link_list(nums):
    head = LinkNode("#")
    cur = head
    for num in nums:
        cur.next = LinkNode(num)
        cur = cur.next

    return head
