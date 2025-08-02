# Day 13: Linked List Operations (with inline comments)

# Singly Linked List Node class
default
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Construct linked list from array
def constructll(arr):
    head = None
    for data in arr:
        if head is None:
            head = Node(data)
            temp = head
        else:
            temp.next = Node(data)
            temp = temp.next
    return head

# Function to print linked list
def printll(head): 
    temp = head
    while temp:
        print(str(temp.data) + "->", end="")
        temp = temp.next

arr = [1, 2, 3, 4, 5]
ll = constructll(arr)
printll(ll)  # Output: 1->2->3->4->5->

# Find middle using Hare and Tortoise algorithm
def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

middle = find_middle(ll)

# Print linked list starting from middle node
def print_middle_and_rest(middle):
    print("\nRest of the linked list from middle:")
    while middle:
        print(middle.data, end="->")
        middle = middle.next

print_middle_and_rest(middle)

# Delete the middle node from the list
def delete_middle(head):
    if head is None or head.next is None:
        return None
    prev = None
    slow = head
    fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    slow.next = None
    return head

print("\n")
printll(delete_middle(ll))  # Output: 1->2->4->5->

# Insert a node at the middle of the list
def insert_middle(head, data):
    if head is None:
        return Node(data)

    # Count the length
    length = 0
    temp = head
    while temp:
        length += 1
        temp = temp.next

    if length % 2 == 0:
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        new_node = Node(data)
        prev.next = new_node
        new_node.next = slow
    else:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        front = slow.next
        new_node = Node(data)
        slow.next = new_node
        new_node.next = front
    return head

insert_middle(ll, 3)
print("\n")
printll(ll)

# Delete head node
def delete_head(head):
    front = head.next
    head.next = None
    return front

# Delete tail node
def delete_tail(head):
    if head is None or head.next is None:
        return None
    temp = head
    while temp.next.next:
        temp = temp.next
    temp.next = None
    return head

# Insert at the beginning
def insert_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

# Insert at the end
def insert_end(head, data):
    if head is None:
        return Node(data)
    new_node = Node(data)
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head

# Reverse linked list (method 1 - using array)
def reverse1(head):
    if head is None:
        return None
    temp = head
    arr = []
    while temp:
        arr.append(temp.data)
        temp = temp.next
    arr.reverse()
    temp = head
    for val in arr:
        temp.data = val
        temp = temp.next
    return head

# Reverse linked list (method 2 - in-place)
def reverse2(head):
    prev = None
    temp = head
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev

print("\n")
printll(reverse2(ll))

# Cycle detection using Floyd’s Cycle-Finding Algorithm
def has_cycle(head):
    if head is None or head.next is None:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

print("\nCycle detected:", has_cycle(ll))

# Doubly Linked List Node class
class Dnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Create doubly linked list from array
def createdll(arr):
    head = None
    temp = None
    for data in arr:
        new_node = Dnode(data)
        if head is None:
            head = new_node
            temp = new_node
        else:
            temp.next = new_node
            new_node.prev = temp
            temp = temp.next
    return head

print("\nDoubly Linked List:")
dll = createdll(arr)
printll(dll)
