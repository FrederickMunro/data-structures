class SinglyLinkedList:
    def __init__(self, value = None):
        self.head = self.Node(value)

    def __repr__(self):
        pointer = self.head
        string = f'SinglyLinkedList({self.head.data})'
        while(pointer.next != None):
            pointer = pointer.next
            data = f'"{pointer.data}"' if isinstance(pointer.data, str) else f'{pointer.data}'
            string += f'\n  push({data})'
        return string

    # Returns a string representation of the list
    def __str__(self):
        pointer = self.head
        string = f'{self.head}'
        while (pointer.next != None):
            pointer = pointer.next
            string += f' > {pointer}'
        string += f' > {pointer}'
        return string

    # Appends an item to the end of the list
    def push(self, data):
        pointer = self.head
        while (pointer.next != None):
            pointer = pointer.next
        pointer.next = self.Node(data)

    # Returns the value of the last element of the list and removes it from the list
    def pop(self):
        pointer = self.head
        while(pointer.next.next != None):
            pointer = pointer.next
        popped = pointer.next.data
        pointer.next = None
        return popped

    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

        # Returns a initializable vesion of the object
        def __repr__(self):
            data = f'"{self.data}"' if isinstance(self.data, str) else f'{self.data}'
            next = f'"{self.next.data}"' if isinstance(self.next, str) else f'{self.next}'
            return f'Node({data}, {next})'

        def __str__(self):
            return f'{self.data}'

