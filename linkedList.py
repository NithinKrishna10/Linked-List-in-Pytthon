class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)

class LinkedList:
    def __init__(self):
        self.head = None


    # PRINT LINKED LIST
    def print_LL(self):
        if self.head is None:
            print('ll is empty')
        else:
            n = self.head
            print("Linked List :")
            while n is not None:
                print(n.data, '---->', end=" ")
                n = n.next


    # INSERT IN EMPTY LINKED LIST
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("It's Not Empty")


    
    # ADD NODE AT THE BEGING OF LINKED LIST
    
    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # ADD NODE AT THE END OF LINKED LIST
    
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            
            
    # ADD NODE AT THE BEGING OF LINKED LIST
    
    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is empty")
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                if n.next.data == x:
                    break
                n = n.next
            if n.next is None:
                print("Node is not found")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node
                
                
     # ADD NODE AFETER LINKED LIST

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("node is not present in LL")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    #  DELETE THE FIRST NODE
    
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.next


    # DELETE LAST NODE
    
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if n.next.next is None:
                    break
                else:
                    n = n.next
            n.next = None

    
    # DELETE ANY NODE BY VALUE IN LINKED LIST
    
    def delete_val(self, x):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if n.next.data == x:
                    break
                else:
                    n = n.next
            if n.next is None:
                print("nothing")
            else:
                n.next = n.next.next

    
    # REVERSE THE LINKED LIST
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


    # ARRAY TO LINKED LIST
    
    def array_to_list(self, arr):
        for i in arr:
            new_node = Node(i)
            if self.head is None:
                self.head = new_node
            else:
                current_node = self.head
                while current_node.next:
                    current_node = current_node.next
                current_node.next = new_node
                
                
    # LINKED LIST TO ARRAY 

    def list_to_array(self):
        arr = []
        
        n = self.head
        while n is not None:
            arr.append(n.data)
            n = n.next
                
    # REMOVE DUPLICATES FROM LINKED LIST 

    def remove_duplicatess(self):
        current = self.head
        prev = None
        duplicate_values = set()
        while current:
            if current.data in duplicate_values:
                prev.next = current.next
            else:
                duplicate_values.add(current.data)
                prev = current
            current = prev.next

    # FIND MIDDLE OF THE LINKED LIST

    def mid_list(self):
        if self.head is None:
            print("LinkedList is Empty")
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print("jai",slow.data,"hai")
        return slow

    # def reverse_list(head):
    #     if head is None or head.next is None:
    #         return head
    #     reversed_list = reverse_list(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return reversed_list

    def reversehelper(self,head,prev):
        if head is None:
            head = prev


        




LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_begin(30)
LL1.add_begin(20)
LL1.add_after(500, 20)
LL1.add_end(700)
LL1.add_end(900)
LL1.add_end(800)
LL1.add_begin(30)
LL1.add_begin(340)
LL1.add_before(400, 700)
LL1.add_after(300, 700)

LL1.reverse()
LL1.print_LL()
LL1.remove_duplicatess()
# LL1.remov_dup()
LL1.reversehelper()
LL1.print_LL()
# LL1.mid_list()