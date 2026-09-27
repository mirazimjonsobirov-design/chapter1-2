# Time: O(n) average, Space: O(n).

def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen = {}

    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return seen[complement], i
        seen[x] = i

    raise ValueError("No valid pair found")


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([-3, 4, 0, 7], 4) == (1, 2)
    assert two_sum([3, 3], 6) == (0, 1)
    print("Challenge 2: all tests passed")
