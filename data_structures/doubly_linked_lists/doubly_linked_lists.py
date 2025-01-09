class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
class Doublylinkedlist:
    def __init__(self):
        self.head=None
    def print_farward(self):
        if self.head==None:
            print('linkedlist is empty')
            return
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)
    def get_last_node(self):
        itr=self.head
        while itr.next:
            itr=itr.next
        return itr
    def print_backward(self):
        if self.head==None:
            print('Linkedlist is empty')
            return
        last_node=self.get_last_node()
        llstr=''
        itr=last_node
        while itr:
            llstr+=str(itr.data)+'--->'
            itr=itr.prev
        print(llstr)
        
        
        


