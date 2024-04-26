
class node:
    def __init__(self,item,next=None):
        self.item=item
        self.next=next 
class SLL:
    def __init__(self,head=None):
        self.head=head
    def is_empty(self):
        return self.head==None
    def ins_at_start(self,data):
        n=node(data,self.head)
        self.head=n
    def ins_at_last(self,data):
        n=node(data)
        if not self.is_empty():
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.head=n
    def search(self,data):
        temp=self.head
        while temp.next is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None   
    def ins_item(self,temp,data):
        if temp is not None:
            n=node(data,temp.next)
            temp.next=n
    
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
    def delete_frst(self):
        if self.head is not None:
            self.head=self.head.next
    def delete_last(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def delete_item(self,data):
        if self.head is None:
            pass
        elif self.head.next is None:
            if self.head.item==data:
                self.head=None
        else:
            temp=self.head
            if temp.item==data:
                self.head==None
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                temp=temp.next
                    
#driver code
mylist=SLL()
mylist.ins_at_start(20) 
mylist.ins_at_start(10)
mylist.ins_at_last(40)
mylist.ins_at_last(50)
mylist.ins_item(mylist.search(20),30)
mylist.print_list()
print('\n')
mylist.delete_frst()
mylist.delete_last()
mylist.delete_item(30)

mylist.print_list()