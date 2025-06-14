class Node:
    """
    Represents a single node in the linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Manages the singly linked list.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Adds a new node with the given data at the end of the list.
        """
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def print_list(self):
        """
        Prints all the nodes in the list.
        """
        if not self.head:
            print("The list is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """
        Deletes the nth node (1-based index) from the list.
        """
        if not self.head:
            raise IndexError("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index must be a positive integer.")

        if n == 1:
            self.head = self.head.next
            return

        current = self.head
        count = 1
        prev = None

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError("Index out of range.")

        prev.next = current.next


# Sample Usage / Test Case 

if __name__ == "__main__":
    ll = LinkedList()

    # Adding elements
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    print("Original list:")
    ll.print_list()

    # Deleting 2nd node
    try:
        ll.delete_nth_node(2)
        print("After deleting 2nd node:")
        ll.print_list()
    except IndexError as e:
        print("Error:", e)

    # Deleting node out of range
    try:
        ll.delete_nth_node(10)
    except IndexError as e:
        print("Error:", e)

    # Deleting from empty list
    empty_ll = LinkedList()
    try:
        empty_ll.delete_nth_node(1)
    except IndexError as e:
        print("Error:", e)
