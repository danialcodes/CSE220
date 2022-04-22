#!/usr/bin/env python
# coding: utf-8

# In[128]:


#Task 1
class Node:
    def __init__(self,data,p,n):
        self.data = data
        self.prev = p
        self.next = n


# In[129]:


class DoublyList:
    def __init__(self,a):
        self.head = Node(None,None,None)
        tail = self.head.next = self.head.prev = self.head
        
        for item in a:
            n = Node(item,None,None)
            n.prev = tail
            tail.next = n
            tail = n
        tail.next = self.head
        tail.next.prev = tail
#   Task 2.2
    def showList(self):
        if(self.head.next is self.head):
            print("Empty list")
        else:
            itr = self.head.next
            while(itr is not self.head):
                if(itr.next is self.head):
                    print(itr.data)
                else:
                    print(itr.data,end=" ")
                itr = itr.next
#   Self made method to reduce code rewritting
    def findIndex(self,element):
        itr = self.head.next
        count = 0
        while (itr is not self.head):
            if (itr.data == element):
                return count
            itr = itr.next
            count+=1
        return False
#   Self made method to reduce code rewritting
    def size(self):
        itr = self.head.next
        count = 0
        while(itr is not self.head):
            count+=1
            itr = itr.next
        return count
#   Self made method to reduce code rewritting
    def nodeAt(self,index):
        if(index>=0 and index<self.size()):
            itr = self.head.next
            count = 0
            while(count<index):
                itr = itr.next
                count+=1
            return itr
#   Task 2.3 - 2.4
    def insert(self, newElement,index=None):
        size = self.size()
        if (self.findIndex(newElement)):
                print("key {} already exists!".format(newElement))
                return
        elif(index == None or index==size):
            tail = Node(newElement,self.head.prev,self.head)
            self.head.prev.next = tail
            self.head.prev = tail
        else:
            if (index>=0 and index<=size):
                indexNode = self.nodeAt(index)
                newNode = Node(newElement,indexNode.prev,indexNode)
                indexNode.prev.next = newNode
                indexNode.prev = newNode
            else:
                print("Invalid Index")
#                 raise IndexError("Valid index is 0 - {}. 
#                                  But {} is given".format(size,index))
#   Task 2.5
    def remove(self, index):
        size = self.size()
        if (index>=0 and index<size):
            indexNode = self.nodeAt(index)
            indexNode.prev.next = indexNode.next
            indexNode.next.prev = indexNode.prev
            indexNode.data = indexNode.prev =  indexNode.next = None
        else:
            print("Invalid Index")
#   Task 2.6
    def removeKey(self, deletekey):
        removeIndex = self.findIndex(deletekey)
        
        if(removeIndex==False and type(removeIndex)==type(False)):
            return "Key not found"
        else:
            self.remove(removeIndex)
            return deletekey


# In[130]:


#Task-2.1, 2.2 -- Constructor & showList
print("\n//=======Task 2.1, 2.2 -- Constructor & showList=======//")
a = [10, 20, 30, 40, 50, 60]
l1 = DoublyList(a)
l1.showList() #Should print: 10->20->30->40->50->60


# In[131]:


#Task-2.3, 2.4 -- Insert
print("\n//=======Task 2.3, 2.4 -- Insert=======//")
c = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l3 = DoublyList(c)
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90
l3.insert(100)
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100
l3.insert(0, 0)
l3.showList() #Should print: 0->10->20->30->40->50->60->70->80->90->100
l3.insert(110, 5)
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100
l3.insert(120, 12)
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
l3.insert(50) #Should print: Key 50 already exists


# In[132]:


#Task-2.5 -- Remove index
print("\n//=======Task-2.5 -- Remove index=======//")
d = [0, 10, 20, 30 ,40 ,110 ,50 ,60 ,70, 80 ,90, 100, 120]
l4 = DoublyList(d)
print("Before Removing: ", end='')
l4.showList() #Should print: 0 10 20 30 40 110 50 60 70 80 90 100 120
l4.remove(5)
print("After Removing:  ", end='')
l4.showList() #Should print: 0 10 20 30 40 50 60 70 80 90 100 120
l4.remove(0)
print("After Removing:  ", end='')
l4.showList()


# In[133]:


#Task-2.6 -- Remove Key
print("\n//=======Task 2.6 -- Remove Key=======//")
l4.showList() #Should print: 10 20 30 40 50 60 70 80 90 100 120
print(l4.removeKey(0))
l4.showList() #Should print: Key not found
print(l4.removeKey(100))
l4.showList() #Should print: 110 20 30 40 50 60 70 80 90 120
print(l4.removeKey(120))
l4.showList() #Should print: 110 20 30 40 50 60 70 80 90 120
print(l4.removeKey(10)) #Should print: Key not found
l4.showList()


# In[ ]:





# In[ ]:




