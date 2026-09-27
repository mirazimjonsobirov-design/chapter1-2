# Time: O(n), Space: O(1).

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Node | None) -> bool:
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next, b.next, c.next = b, c, None
    assert has_cycle(a) is False

    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next, b.next, c.next = b, c, b
    assert has_cycle(a) is True

    a = Node(1)
    a.next = a
    assert has_cycle(a) is True

    assert has_cycle(None) is False
    print("Challenge 5: all tests passed")
