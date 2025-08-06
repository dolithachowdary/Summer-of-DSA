"""
Day 14 — Linked List Problems & Binary Trees
Includes function-level docstrings and inline comments for clarity.
"""

# =========================
# Linked List (Singly) Utils
# =========================

class LLNode:
    """Singly Linked List Node"""
    def __init__(self, data):
        self.data = data
        self.next = None


def construct_ll(arr):
    """Construct a linked list from a Python list and return the head."""
    head = None
    tail = None
    for x in arr:
        node = LLNode(x)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def print_ll(head):
    """Print a linked list as a -> chain."""
    cur = head
    while cur:
        print(f"{cur.data}->", end="")
        cur = cur.next
    print()


# -------------------------
# Cycle detection utilities
# -------------------------

def first_cycle_node(head):
    """
    Floyd's cycle algorithm: return the first node of the cycle if it exists, else None.
    """
    slow = fast = head
    # 1) Detect meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # 2) Move slow to head; then advance both 1 step; meeting point is cycle start
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow  # start of the loop
    return None


def length_of_loop(head):
    """
    Return the length of the loop (0 if no loop).
    After detection, keep one pointer fixed and move the other until meet again.
    """
    slow = fast = head
    # 1) Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # 2) Count loop length
            count = 1
            fast = fast.next
            while slow != fast:
                fast = fast.next
                count += 1
            return count
    return 0


# -------------------------
# Misc Linked List Problems
# -------------------------

def sort_ll_inplace_by_values(head):
    """
    Sort linked list by collecting values, sorting them, then writing them back.
    (Not stable on nodes; stable on values. O(n log n) time, O(n) extra space.)
    """
    vals = []
    cur = head
    while cur:
        vals.append(cur.data)
        cur = cur.next
    vals.sort()
    cur = head
    i = 0
    while cur:
        cur.data = vals[i]
        i += 1
        cur = cur.next
    return head


def is_palindrome_ll(head):
    """
    Check if a singly linked list is a palindrome.
    Method: Copy values to a list and compare with reversed. O(n) time, O(n) space.
    """
    vals = []
    cur = head
    while cur:
        vals.append(cur.data)
        cur = cur.next
    return vals == vals[::-1]


# =========================
# Binary Trees / BST
# =========================

class TreeNode:
    """Binary Tree / BST Node (uses 'val', 'left', 'right')."""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert_bst(root, val):
    """Insert a value into a BST (iterative). Return the (possibly new) root."""
    if root is None:
        return TreeNode(val)
    cur = root
    while True:
        if val < cur.val:
            if cur.left is None:
                cur.left = TreeNode(val)
                break
            cur = cur.left
        elif val > cur.val:
            if cur.right is None:
                cur.right = TreeNode(val)
                break
            cur = cur.right
        else:
            # Duplicate: do nothing (or handle as needed)
            break
    return root


def create_bst(arr):
    """Create a BST from an iterable of values."""
    root = None
    for x in arr:
        root = insert_bst(root, x)
    return root


# -------------------------
# Traversals
# -------------------------

def inorder(root):
    """Inorder (L, Root, R)."""
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def preorder(root):
    """Preorder (Root, L, R)."""
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    """Postorder (L, R, Root)."""
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")


def level_order(root):
    """
    Level-order traversal (BFS) returning list of levels.
    Uses a deque for O(1) pops from left.
    """
    from collections import deque
    if not root:
        return []
    q = deque([root])
    ans = []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    return ans


def tree_height(root):
    """
    Height of a binary tree = number of nodes on longest path from root to leaf.
    Returns 0 for empty tree.
    """
    if root is None:
        return 0
    # Height = 1 (current node) + max height of subtrees
    return 1 + max(tree_height(root.left), tree_height(root.right))


def zigzag_level_order(root):
    """
    Zigzag (spiral) level order: left->right then right->left alternately.
    Return list of levels.
    """
    levels = level_order(root)
    for i in range(len(levels)):
        if i % 2 == 1:
            levels[i].reverse()
    return levels


# -------------------------
# Binary Tree Notes (quick reference)
# -------------------------
"""
Full binary tree: each node has 0 or 2 children.
Complete binary tree: all levels completely filled except possibly the last,
which is filled from left to right.
Perfect binary tree: all leaves at the same level and every internal node has 2 children.
Balanced binary tree: |height(left) - height(right)| <= 1 for every node.
"""


# =========================
# Quick Demo / Sanity Tests
# (comment out when using as a library)
# =========================
if __name__ == "__main__":
    # ----- Linked List demos -----
    arr = [1, 2, 3, 4, 5]
    ll = construct_ll(arr)
    print("LL:", end=" ")
    print_ll(ll)  # 1->2->3->4->5->

    print("Is palindrome?:", is_palindrome_ll(ll))
    sort_ll_inplace_by_values(ll)
    print("Sorted LL:", end=" ")
    print_ll(ll)

    # Create a small cycle for testing first_cycle_node() and length_of_loop()
    # Make tail.next point to node with value 3
    tail = ll
    third = ll.next.next  # node with value 3
    while tail.next:
        tail = tail.next
    tail.next = third
    start = first_cycle_node(ll)
    print("Cycle start value:", start.data if start else None)
    print("Cycle length:", length_of_loop(ll))

    # Break the cycle for safety
    tail.next = None

    # ----- BST / Tree demos -----
    nums = [6, 2, 1, 3, 9, 8, 7]
    root = create_bst(nums)
    print("BST Inorder:", end=" ")
    inorder(root); print()
    print("BST Preorder:", end=" ")
    preorder(root); print()
    print("BST Postorder:", end=" ")
    postorder(root); print()
    print("Level order:", level_order(root))
    print("Zigzag order:", zigzag_level_order(root))
    print("Tree height:", tree_height(root))
