# Time: O(1) amortized per operation, Space: O(n).

class QueueFromStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x) -> None:
        self.in_stack.append(x)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        if not self.out_stack:
            raise IndexError("dequeue from empty queue")

        return self.out_stack.pop()


if __name__ == "__main__":
    q = QueueFromStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3

    q = QueueFromStacks()
    q.enqueue("a")
    assert q.dequeue() == "a"

    q = QueueFromStacks()
    try:
        q.dequeue()
        assert False, "Expected IndexError"
    except IndexError:
        pass

    print("Challenge 4: all tests passed")
