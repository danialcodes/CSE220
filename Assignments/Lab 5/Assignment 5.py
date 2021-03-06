# Task 1.a
def findFacto(n):
    if(n<0):
        raise ValueError("No factorial for negetive number")
    if(n==0):
        return 1
    return n * findFacto(n-1)

# Task 1.b
def findFibo(n,f=0,s=1): # I considered 1st element 0 and second element 1
    if(n<0):
        raise ValueError()
    if(n==1):
        return f
    if(n==2):
        return s
    temp = s
    s=f+temp
    f=temp
    return findFibo(n-1,f,s)

# Task 1.c
def print_arr(arr,i=0):
    if(len(arr)!=i):
        print(arr[i])
        return print_arr(arr,i+1)

# Task 1.d
def powerN(n,p):
    if(p==1):
        return n
    return n * powerN(n,p-1)

print("\n//=======Task 1.a -- Factorial of n=======//")
print("Factorial of 9 is:",findFacto(9))
print("Factorial of 20 is:",findFacto(20))

print("\n//=======Task 1.b -- nth Fibonacci=======//")
print("I considered 1st is 0 and 2nd is 1")
print("5th Fibonacci number is:",findFibo(5))
print("10th Fibonacci number is:",findFibo(10))

print("\n//=======Task 1.c -- Print all elements of an Array=======//")
arr = [10,20,30,40,50,60]
print("Initial array ->",arr)
print_arr(arr)
print("\n//=======Task 1.d -- Power of n=======//")
print("3 to the power 2 is:",powerN(3,2))
print("5 to the power 2 is:",powerN(5,2))



# Task 2.a
def decimalToBinary(d,b=''):
    if(d==0):
        if(b!=""):
            return b[::-1]
        return 0
    b+=str(d%2)
    return decimalToBinary(d//2,b)

print("\n//=======Task 2.a -- Decimal To Binary=======//")
print("Binary of 27 is:",decimalToBinary(27))
print("Binary of 99 is:",decimalToBinary(99))


# In[3]:


# Non- Dummy headed Singly linear linked list
class Node:
    def __init__(self,v,n=None):
        self.value = v
        self.next = n
class LL:
    head = None
    
    def __init__(self,itr):
        
        for i in itr:
            nN = Node(i)
            if(self.head is None):
                self.head = nN
                fst = self.head
            else:
                fst.next = nN
                fst = nN
a = [10,20,30,40,50]
x = LL(a)

# Task 2.b
def SumofLLItems(head):
    if(head is None):
        return 0
    return head.value + SumofLLItems(head.next)

print("\n//=======Task 2.b -- Sum of all numbers of a Non Dummy headed Singly Linked Linear List=======//")
print(SumofLLItems(x.head))

# Task 2.c
def reverse_print(head):
    if(head.next is None):
        print(head.value)
        return
    reverse_print(head.next)
    print(head.value)

print("\n//=======Task 2.c -- Reverse Print a Non Dummy headed Singly Linked Linear List=======//")
reverse_print(x.head)



# Task 3
def hocBuilder(height):
    if(height==0):
        return 0
    if(height == 1):
        return 8
    return 5 + hocBuilder(height-1)

print("\n//=======Task 3 -- Calculate cards needed to build House of Cards=======//")
print("For height 1 we need:",hocBuilder(1),"cards")
print("For height 2 we need:",hocBuilder(2),"cards")
print("For height 0 we need:",hocBuilder(0),"cards")
print("For height 5 we need:",hocBuilder(5),"cards")




#Task 4.a
def pattern(n):
    if(n==0):
        return
    pattern(n-1)
    row(n)
    print()
def row(n):
    if(n==0):
        return
    
    row(n-1)
    print(n,end=" ")
    
print("\n//=======Task 4.a -- Print the following pattern for the given input=======//")
pattern(5)

# Task 4.b
def patternTwo(n,num=1):
    if(n==0):
        return
    col_sp(n-1)
    col_num(num)
    print()
    patternTwo(n-1,num+1)
def col_num(n):
    if(n==0):
        return
    col_num(n-1)
    print(n,end=" ")
def col_sp(n):
    if(n==0):
        return
    col_sp(n-1)
    print(" ",end=" ")
    
print("\n//=======Task 4.b -- Print the following pattern for the given input=======//")
patternTwo(5)



# Task 5
class FinalQ: 
    def print(self,array,idx): 
        if(idx<len(array)): 
            profit = self.calcProfit(array[idx])
            print("{}. Investment: {}; Profit: {}".format(idx+1,array[idx],profit))
            self.print(array,idx+1)
    def calcProfit(self,investment):
        if(investment<=25000):
            return 0
        elif(investment<=100000):
            investment = investment-25000
            return investment/(1/0.045)
        investment = investment-100000
        return (investment/(1/0.08)) + self.calcProfit(100000)
        
print("\n//=======Task 5 -- Calculate Profit=======//")
array=[25000,100000,250000,350000] 
f = FinalQ() 
f.print(array,0)




