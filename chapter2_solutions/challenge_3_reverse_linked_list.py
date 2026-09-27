# Time: O(n), Space: O(1) for the iterative solution.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Node | None) -> Node | None:
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def to_list(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


def make_list(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


if __name__ == "__main__":
    assert to_list(reverse_list(make_list([1, 2, 3]))) == [3, 2, 1]
    assert reverse_list(None) is None
    assert to_list(reverse_list(make_list([5]))) == [5]
    print("Challenge 3: all tests passed")
