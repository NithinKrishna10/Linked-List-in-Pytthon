class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# def reverse_list(head, prev=None):
#     if head is None:
#         return prev
#     next_node = head.next
#     head.next = prev
#     return reverse_list(next_node, head)

# # Example usage
# head = Node(1, Node(2, Node(3, Node(4, Node(5,Node(9,Node(10)))))))

# print("Before:")
# node = head
# while node:
#     print(node.data,end=" ")
#     node = node.next
# reversed_head = reverse_list(head)

# node = reversed_head
# # print("")
# print("\nAfter:")

# # while node:
# #     print(node.data,end=" ")
# #     node = node.next
    
    
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            print("LinkedList Is Not Empty")   
                     
    def printll(self):
        if self.head is None:
            print("\nLinkedList is Empty")
        else:
            current = self.head
            while current:
                print(current.data,end=" ")
                current = current.next
                
    
    def addbegin(self,data):
        if self.head is None:
            
            print("Is Not Empty")
        
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            
            
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            
                    
            
    # def add_end(self,data):
    #     new_node = Node(data)
    #     if self.head is None:
    #         print("Is Empty")
    #     else:
    #         current = self.head
    #         while current is not None:
    #             current = current.next 
    #             print(current)
    #         current.next = new_node
    #         # self.tail = new_node
    
    def add_beg_value (self,data,x):
        current = self.head
        while current:
            if current.next.data == x:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
    
    def del_duplicate(self):
        current=self.head
        while current:
            n = current.next
            while  n:
                if current.data == n.data:
                    print(n.data)              
                else:
                    n = n.next
            current = current.next
            
    def rever(self):
        current = self.head
        prev = None
        while current:
            next_node = current
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

def revers(head,prev):
    if head.next is None:
        return prev
    else:
        new_node = head.next
        head.next = prev
    return revers(new_node,head)




def recrev(head,prev=None):
    if head is None:
        return prev
    else:
        new_node = head.next
        head.next = prev
    return recrev(new_node,prev)

def rs(head):
    current = head
    prev =None
    while current:
        next_node = current.next
        current = prev
        prev = current
        current = current.next

def kfd(head,p):
    if head.next is None:
        return p
    ne = head.next 
    head.next = p
    
    return kfd(ne, head)
    
    
    
ll = LinkedList()

ll.empty(39)        
ll.addbegin(902)
ll.addbegin(904)
ll.add_end(65)
ll.add_end(68)
ll.add_end(65)
ll.add_end(60)
ll.del_duplicate()
ll.rever()
ll.printll()