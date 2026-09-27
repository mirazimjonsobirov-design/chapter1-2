# Time: O(log n), Space: O(1).

def search_range(nums: list[int], target: int) -> tuple[int, int]:
    def find_first():
        left, right = 0, len(nums) - 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                answer = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return answer

    def find_last():
        left, right = 0, len(nums) - 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                answer = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return answer

    return find_first(), find_last()


if __name__ == "__main__":
    assert search_range([5, 7, 7, 8, 8, 8, 10], 8) == (3, 5)
    assert search_range([5, 7, 7, 8, 8, 8, 10], 6) == (-1, -1)
    assert search_range([1, 2, 3], 2) == (1, 1)
    assert search_range([], 1) == (-1, -1)
    print("Challenge 9: all tests passed")
