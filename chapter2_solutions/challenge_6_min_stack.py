# Time: O(1) per operation, Space: O(n).

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x) -> None:
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def get_min(self):
        if not self.min_stack:
            raise IndexError("minimum from empty stack")
        return self.min_stack[-1]


if __name__ == "__main__":
    s = MinStack()
    s.push(3)
    s.push(5)
    s.push(2)
    assert s.get_min() == 2
    assert s.pop() == 2
    assert s.get_min() == 3

    s = MinStack()
    s.push(-1)
    s.push(-5)
    assert s.get_min() == -5
    assert s.top() == -5

    s = MinStack()
    s.push(4)
    s.push(4)
    assert s.get_min() == 4
    s.pop()
    assert s.get_min() == 4

    print("Challenge 6: all tests passed")
