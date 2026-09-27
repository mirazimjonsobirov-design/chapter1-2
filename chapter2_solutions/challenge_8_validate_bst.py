# Time: O(n), Space: O(h).
# This implementation uses strict BST ordering: duplicate values are not allowed.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Node | None) -> bool:
    def validate(node, low, high):
        if node is None:
            return True

        if not (low < node.val < high):
            return False

        return (
            validate(node.left, low, node.val)
            and validate(node.right, node.val, high)
        )

    return validate(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    root = Node(5, Node(1), Node(8))
    assert is_valid_bst(root) is True

    root = Node(5, Node(1), Node(8, Node(4), Node(9)))
    assert is_valid_bst(root) is False

    assert is_valid_bst(None) is True

    root = Node(5)
    assert is_valid_bst(root) is True

    print("Challenge 8: all tests passed")
