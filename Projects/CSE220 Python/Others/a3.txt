class Node:
    def __init__(self,v,p,n):
        self.value = v
        self.prev = p
        self.next = n
class DoublyList:

    def __init__(self, a = None):
        if isinstance(a, list):
            self.head = Node(None, None, None)
            self.head.next = self.head.prev = self.head
            
            self.head.next = None
            tail = None
            for item in a:
                newNode = Node(item, None, None)
                if self.head.next == None:
                    self.head.next = newNode
                    self.head.prev = newNode
                    newNode.prev = self.head
                    newNode.next = self.head
                    
                    tail = newNode
                    
                else:
                    newNode.next = self.head
                    newNode.prev = tail
                    tail.next = newNode
                    self.head.prev = newNode
                    
                    tail = newNode
                    
    def showList(self):
        if self.head.next == None: 
            print("Empty List")
        else:
            node = self.head.next
            while node is not self.head:
                print(node.value, end = " ")
                node = node.next
        print()
        
    def insert(self, newElement, index = None):
        newNode = Node(newElement, None, None)
        if (index == None) or (self.head.next == self.head):
            lastNode = self.head.prev
            if lastNode.value == newNode.value: 
                print("Value exists!")
                return self.head
            newNode.next = self.head
            newNode.prev = lastNode
            lastNode.next = newNode
            self.head.prev = newNode
            
        else:
            length = 0
            end = self.head.next
            while end is not self.head:
                length += 1
                end = end.next

            if index >= length or index < 0:
                print("Invalid index!")
                return self.head
            count = 0
            tail = self.head.next
            while tail is not self.head:
                curr = tail
                tail = tail.next
                if count == index:
                    if curr.value == newNode.value: 
                        print("Invalid input!")
                        return self.head
                    break
                count += 1

            pred = curr.prev
            newNode.next = curr
            newNode.prev = pred
            curr.prev = newNode
            pred.next = newNode
                
    def remove(self, index):
        if self.head.next == self.head:
                print("List empty!")
            
        else:
                length = 0
                end = self.head.next
                while end is not self.head:
                    length += 1
                    end = end.next
                    
                if index >= length or index < 0:
                    print("Invalid index!")
                count = 0
                tail = self.head.next
                while tail is not self.head:
                    curr = tail
                    tail = tail.next
                    if count == index:
                        break
                    count += 1
                    

                pred = curr.prev
                after = curr.next
                pred.next = after
                after.prev = pred
                curr.next = None
                curr.prev = None
                
    def removeKey(self, deleteKey):
        if self.head.next == self.head:
                return "Empty List"
        else:
            tail = self.head.next
            while tail is not self.head:
                curr = tail
                tail = tail.next
                if curr.value == deleteKey:
                    break

            if curr.value != deleteKey: 
                return "Can't find the key!"
            else:
                pred = curr.prev
                after = curr.next
                pred.next = after
                after.prev = pred
                curr.next = None
                curr.pred = None
            
        return curr.value

a = [10, 20, 30, 40, 50, 60]
l1 = DoublyList(a)
l1.showList()
c = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l3 = DoublyList(c)
l3.showList()
l3.insert(100)
l3.showList()
l3.insert(0, 0)
d = [0, 10, 20, 30 ,40 ,110 ,50 ,60 ,70, 80 ,90, 100, 120]
l4 = DoublyList(d)
l4.showList()
l4.remove(5)
l4.showList()
l4.remove(0)
l4.showList()
l4.showList()
print(l4.removeKey(0))
l4.showList() 
print(l4.removeKey(100))
l4.showList() 