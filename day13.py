#  linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def constructll(arr):
    head=None
    for data in arr:
        if (head==None):
            head=Node(data)
            temp=head
        else:
            temp.next=Node(data)
            temp=temp.next
    #printll(head)
    return head
arr=[1,2,3,4,5]

#to print linked list

def printll(head): 
    temp=head
    while temp:
        print(str(temp.data)+"->",end="")
        temp=temp.next

ll=constructll(arr)
printll(ll) #1->2->3->4->5->

#hare and tortoise algorithm to find middle element ***

def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

middle=find_middle(ll) #3

def print_middle_and_rest(middle):
    
    print("Rest of the linked list from middle:")
    while middle:
        print(middle.data, end="->")
        middle = middle.next
    
print_middle_and_rest(middle)
#delete middle node
def delete_middle(head):
    if head is None or head.next is None:
        return None  # If the list is empty or has only one node, return None
    prev = None
    slow = head
    fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next=slow.next
    slow.next=None
    return head
print()
printll(delete_middle(ll)) #1->2->4->5->

#insert at middle
def insert_middle(head, data):
    if head is None:
        return Node(data)
    len=0
    temp=head
    while temp:
        len+=1
        temp=temp.next
    if len%2==0:
        prev=None
        slow=head
        fast=head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        new_node = Node(data)
        prev.next = new_node
        new_node.next = slow
        return head
    else:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        front=slow.next
        new_node = Node(data)
        slow.next = new_node
        new_node.next = front
        return head
insert_middle(ll, 3)
print()
printll(ll) #1 2 3 4 5


#delete head
def delete_head(head):
    front=head.next
    head.next=None
    return front
print()
# printll(delete_head(ll))   #2 3 4 5 

#delete tail
def delete_tail(head):
    if head is None or head.next is None:
        return None  # If the list is empty or has only one node, return None
    temp = head
    while temp.next.next:
        temp = temp.next
    temp.next = None  # Remove the last node
    return head
print()
# printll(delete_tail(ll))  #2 3 4

#insert at beginning
def insert_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head
print()
# ll = insert_beginning(ll, 1)
printll(ll)  #1 2 3 4

#insert at end
def insert_end(head, data):
    if head is None:
        return Node(data)
    new_node = Node(data)
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head
print()
# ll = insert_end(ll, 5)
printll(ll)  #1 2 3 4 5

#reverse linked list
def reverse1(head):
    if head is None:
            return None
    temp=head
    arr=[]
    while(temp):
        arr.append(temp.data)
        temp=temp.next
    arr=arr[::-1]
    i=0
    temp=head
    while(temp):
        temp.data=arr[i]
        i+=1
        temp=temp.next
    return head
print()

# printll(reverse1(ll))  #5 4 3 2 1

def reverse2(head):
    prev = None
    temp=head
    while temp:
        front=temp.next 
        temp.next=prev
        prev=temp
        temp=front
    return prev
print()
printll(reverse2(ll))

#cycle detection , hare and tortoise algorithm
def has_cycle(head):
    
    if head is None or head.next is None:
        return False
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            return True
    return False
print(has_cycle(ll))


# double linked list
class Dnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev=None
def createdll(arr):
    head=None
    for data in arr:
        if(head==None):
            head=Dnode(data)
            temp=head
        else:
            new_node=Dnode(data)
            new_node.prev=new_node
            temp.next=new_node
            temp=temp.next
    return head

print("dll")
printll(createdll(arr))
