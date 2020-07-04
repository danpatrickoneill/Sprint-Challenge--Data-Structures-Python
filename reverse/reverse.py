class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def __str__(self):
        # if self.next_node:
        #     return f"{self.value} --> {self.next_node.value}"
        # return f"{self.value} --> {self.next_node}"
        result = ""
        if self.next_node:
            result += f"{self.value} --> {self.next_node.value}"
        else:
            result += f"{self.value} --> None"
        return result

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += f"({current}),"
            current = current.get_next()
        return result

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        # TO BE COMPLETED
        if not self.head or not self.head.next_node:
            return self

        previous = None
        current = self.head
        new = current.next_node
        current.set_next(None)
        while new != None:
            # print(current, new, previous)
            previous = current
            current = new
            new = current.next_node
            print("Current: ", current, "Previous: ", previous, "New: ", new)
            # Next line not necessary anymore
            # current.set_next(previous)
            # I don't like this next line but it made things work
            self.add_to_head(current.value)

        return current


linked_list = LinkedList()

linked_list.add_to_head(1)
linked_list.add_to_head(2)
linked_list.add_to_head(3)
linked_list.add_to_head(4)
linked_list.add_to_head(5)

print("Original list: ", linked_list)

(linked_list.reverse_list())

print("Reversed list: ", linked_list)
