class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        current = head
        if current == None:
            return
        while current.next != None:
            if current.data == current.next.data:
                new = current.next.next
                current.next = new
            else:
                current = current.next
        return head

    def myQueue(self, head):
        queue = []
        if head:
            queue.append(head.data)
            current = head
            while current:
                if current.next != None:
                    if current.next.data not in queue:
                        queue.append(current.next.data)
                current = current.next
        return queue

mylist= Solution()
T=int(input("Enter the number of nodes: "))
head=None
for i in range(T):
    data=int(input(f"Enter node {i+1}: "))
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 
print()
print(mylist.myQueue(head))
