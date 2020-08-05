class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        new_node = Node(data)

        if head == None:    
            return new_node
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = new_node
            return head
    #Complete this method

mylist= Solution()
T=int(input("Enter the number of nodes: "))
head=None
for i in range(T):
    data=int(input("Enter node data: "))
    head=mylist.insert(head,data)    
mylist.display(head); 	 