import random
from linked_list import LinkedList


def mergeSort(linked_list):
    "sorts the list"
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head == None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = mergeSort(left_half)
    right = mergeSort(right_half)
    
    return merge(left, right)

def split(linked_list):
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid_node = size//2

        mid_node = linked_list.node_at_index(mid_node-1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    merged = LinkedList()

    merged.add(0)
    current = merged.head
    left_head = left.head
    right_head = right.head


    while left_head or right_head:
        if left_head == None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head == None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node

    head = merged.head.next_node
    merged.head = head

    return merged

l = LinkedList()
for i in range(10):
    l.add(random.randint(0, 100))    
print(l)

sll = mergeSort(l)
print(sll)

def verifySorted(ll):
    n = ll.size()
    if n == 0 or n == 1:
        return True
    
    for i in range(sll.size()):

        print(ll.node_at_index(i).data < ll.node_at_index(i+1).data)

        if i < ll.size()-1:
            break

verifySorted(sll)