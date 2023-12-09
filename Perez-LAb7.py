class Node:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next_node = nxt

class LinkedList:
    def __init__(self):
        self.head_node = None

    def add_node(self, val):
        new_node = Node(val)
        if not self.head_node:
            self.head_node = new_node
        else:
            current_node = self.head_node
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def display_list(self):
        current_node = self.head_node
        while current_node:
            print(current_node.val, end="")
            if current_node.next_node:
                print("->", end="")
            current_node = current_node.next_node
        print()

def merge_sorted_lists(list_a, list_b):
    dummy_node = Node()  # Dummy node to simplify the code
    current_node = dummy_node

    while list_a is not None and list_b is not None:
        if list_a.val < list_b.val:
            current_node.next_node = list_a
            list_a = list_a.next_node
        else:
            current_node.next_node = list_b
            list_b = list_b.next_node

        current_node = current_node.next_node

    # If one of the lists is not exhausted, append the remaining nodes
    if list_a is not None:
        current_node.next_node = list_a
    elif list_b is not None:
        current_node.next_node = list_b

    result_list = LinkedList()
    result_list.head_node = dummy_node.next_node  # Skip the dummy node in the final result
    return result_list

# Example usage with different variable names:
linked_list_a = LinkedList()
linked_list_a.add_node(1)
linked_list_a.add_node(2)
linked_list_a.add_node(4)

linked_list_b = LinkedList()
linked_list_b.add_node(1)
linked_list_b.add_node(3)
linked_list_b.add_node(4)

merged_result = merge_sorted_lists(linked_list_a.head_node, linked_list_b.head_node)
print("Merged Result:", end=" ")
merged_result.display_list()
