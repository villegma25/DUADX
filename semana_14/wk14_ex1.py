# Node class represents a single element in the stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # points to the node below it


# Stack implemented using Nodes (no lists/dicts/tuples)
class Stack:
    def __init__(self):
        self.top = None   # top of the stack

    def is_empty(self):
        return self.top is None

    def push(self, data):
        """Insert a new node at the top of the stack"""
        new_node = Node(data)
        new_node.next = self.top  # link new node to the old top
        self.top = new_node       # update top
        print(f"Pushed '{data}' onto the stack.")

    def pop(self):
        """Remove the top node and return its value"""
        if self.is_empty():
            print("The stack is empty. Cannot perform pop().")
            return None
        value = self.top.data
        self.top = self.top.next  # move top down
        print(f"Popped '{value}' from the stack.")
        return value

    def print_structure(self):
        """Print the stack from top to bottom"""
        if self.is_empty():
            print("The stack is empty.")
            return
        current = self.top
        print("Stack (top -> bottom):", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    stack = Stack()

    print("=== Test: push ===")
    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack.print_structure()   # Expect: C B A

    print("\n=== Test: pop ===")
    stack.pop()               # Removes C
    stack.print_structure()   # Expect: B A

    print("\n=== Test: pop on empty ===")
    stack.pop()
    stack.pop()
    stack.pop()               # Should show warning message
