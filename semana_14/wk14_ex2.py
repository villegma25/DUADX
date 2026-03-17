class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None   # points to left
        self.next = None   # points to right       

class Deque:
    def __init__(self):
        self.head = None   # front
        self.tail = None  # back

    def push_left(self, data):
        new_node = Node(data)
        if self.head is None:  # empty deque
            self.head = self.tail = new_node
        else:
            new_node.next = self.head   # link forward
            self.head.prev = new_node   # link backward
            self.head = new_node        # update left
        print(f"push {data} to the LEFT of the deque.")

    def push_right(self, data):
        new_node = Node(data)
        if self.tail is None:  # empty deque
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print(f"Pushed {data} to the RIGHT of the queue")

    def pop_left(self):
        if self.head is None:
            print(f"Error: Can not pop from LEFT, queue is empty.")
            return None
        value = self.head.data
        self.head = self.head.next
        if self.head is not None:  # deque is now empty
            self.head.prev = None
        else:
            self.tail.prev = None
            print(f"popped { value} from the LEFT of the queue.")
        return value
       
    def pop_right(self):
        if self.tail is None:
            print(f"Error: Can not pop from the RIGHT, queue is empty.")
            return None
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:  # deque is now empty
            self.tail.next = None
        else:
            self.head = None
            print(f"Popped {value} from the RIGHT of the queue.")
        return value

    def print_structure(self):
        if self.head is None:
           print("Deque is empty.")
           return
        current = self.head
        print("Deque (left -> right): ", end="")
        while current is not None:
            print(current.data, end="<->" if current.next else"")
            current = current.next
        print()


if __name__ == "__main__":
    dq = Deque()
    dq.print_structure()
    dq.push_left("A")
    dq.push_right("B")
    dq.push_left("C")
    dq.print_structure()
    dq.pop_left()
    dq.print_structure()
    dq.pop_right()
    dq.print_structure()
    dq.pop_left()
    dq.print_structure()
    dq.pop_right()