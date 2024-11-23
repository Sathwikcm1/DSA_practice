#FIXME: Remvoing Duplicate values from the sorted DLL.
class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def remove_duplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            # Remove the duplicate node
            duplicate = curr.next
            curr.next = duplicate.next
            if duplicate.next:
                duplicate.next.prev = curr
        else:
            curr = curr.next
    return head

# Helper functions
def create_dll(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head

def print_dll(head):
    current = head
    while current:
        print(current.val, end=" <-> " if current.next else " -> None\n")
        current = current.next

# Test optimized solution
values = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6]
head = create_dll(values)
print("Original DLL:")
print_dll(head)

print("After Removing Duplicates:")
result = remove_duplicates(head)
print_dll(result)
