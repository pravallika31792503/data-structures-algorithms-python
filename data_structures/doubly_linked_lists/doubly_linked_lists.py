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
    def get_length(self):
        if self.head=='None':
            print('Linked list is empty')
            return
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count
    def insert_at_begin(self,data):
        if self.head==None:
            node=Node(data,self.head,None)
            self.head=node
        node=Node(data,self.head,None)
        self.head.prev=node
        self.head=node
    def insert_at_end(self,data):
        if self.head==None:
            node=Node(data,self.head,None)
            self.head=node
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None,itr)
    def insert_values(self,list):
        self.head=None
        for data in list:
            self.insert_at_end(data)
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception('Invalid Index')
        if index==0:
            self.insert_at_begin(data)
        itr=self.head
        count=0
        while itr:
            if count+1==index:
                node=Node(data,itr.next,itr)
                if node.next:
                    node.next.prev=node
                itr.next=node
                break
            itr=itr.next
            count+=1
    def remove_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception('Invalid Index')
        if index==0:
            self.head=self.head.next
            self.head.prev=None
            return
        count=0
        itr=self.head
        while itr:
            if count==index:
                itr.prev.next=itr.next
                if itr.next:
                    itr.next.prev=itr.prev
                break
            itr=itr.next
            count+=1
if __name__ == '__main__':
    ll = Doublylinkedlist()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_farward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_farward()
    ll.insert_at(0,"jackfruit")
    ll.print_farward()
    ll.insert_at(6,"dates")
    ll.print_farward()
    ll.insert_at(2,"kiwi")
    ll.print_farward()









    
        
        


