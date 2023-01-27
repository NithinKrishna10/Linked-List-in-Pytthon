class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


node1 = Node(10)

# print(node1)


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print('ll is empty')
        else:
            n = self.head
            print("Linked List :")
            while n is not None:
                print(n.data,'---->',end=" ")
                n = n.ref
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("It's Not Empty")

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty")
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                if n.ref.data == x:
                    break
                n=n.ref
            if n.ref is None:
                print("Node is not found")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.ref
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if n.ref.ref is None:
                    break
                else:
                    n = n.ref
            n.ref = None

    def delete_val(self,x):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if n.ref.data == x:
                    break
                else:
                    n = n.ref
            if n.ref is None:
                print("nothing")
            else:
                n.ref = n.ref.ref

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.ref
            current.ref = prev
            prev = current
            current = next_node
        self.head = prev
    
    def remove_duplicates(self):
        current_node = self.head
        while current_node.ref:
            if current_node.data == current_node.ref.data:
                current_node.ref = current_node.ref.ref
            else:
                current_node = current_node.ref

    def array_to_list(self,arr):
        for i in arr:
            new_node = Node(i)
            if self.head is None:
                self.head = new_node
            else:
                current_node = self.head
                while current_node.ref:
                    current_node = current_node.ref
                current_node.ref = new_node


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_begin(30)
LL1.add_after(500,20)
LL1.add_end(700)
LL1.add_before(400,700)
LL1.add_after(300,700)
# LL1.reverse()
LL1.print_LL()
LL1.remove_duplicates()
LL1.print_LL()

