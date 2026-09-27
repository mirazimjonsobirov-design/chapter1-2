# Time: O(n), Space: O(n).

def is_balanced(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False

    return not stack


if __name__ == "__main__":
    assert is_balanced("(a[b]{c})") is True
    assert is_balanced("([)]") is False
    assert is_balanced("") is True
    assert is_balanced(")") is False
    print("Challenge 1: all tests passed")
