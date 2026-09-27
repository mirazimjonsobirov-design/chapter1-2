# Time: O(1) amortized append, O(1) get/set; resize is O(n).
# Space: O(capacity).

import ctypes


class DynamicArray:
    def __init__(self, initial_capacity=2):
        if initial_capacity < 1:
            raise ValueError("initial_capacity must be positive")

        self.capacity = initial_capacity
        self.size = 0
        self._data = (ctypes.py_object * self.capacity)()

    def _check_index(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("index out of range")

    def _grow(self):
        new_capacity = self.capacity * 2
        new_data = (ctypes.py_object * new_capacity)()

        for i in range(self.size):
            new_data[i] = self._data[i]

        self._data = new_data
        self.capacity = new_capacity

    def append(self, x) -> None:
        if self.size == self.capacity:
            self._grow()

        self._data[self.size] = x
        self.size += 1

    def get(self, i):
        self._check_index(i)
        return self._data[i]

    def set(self, i, x) -> None:
        self._check_index(i)
        self._data[i] = x


if __name__ == "__main__":
    a = DynamicArray(2)
    a.append(10)
    a.append(20)
    a.append(30)
    assert a.size == 3
    assert a.capacity == 4
    assert a.get(2) == 30

    a.set(1, 99)
    assert a.get(1) == 99

    a = DynamicArray(1)
    a.append("x")
    a.append("y")
    assert a.get(0) == "x"
    assert a.get(1) == "y"

    try:
        a.get(5)
        assert False, "Expected IndexError"
    except IndexError:
        pass

    print("Challenge 7: all tests passed")
