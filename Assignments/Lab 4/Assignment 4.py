class Node:
    def __init__(self, v, n):
        self.value = v
        self.next = n


# Task 1
class ArrayStack:
    def __init__(self, size):
        self.stack = [0] * size
        self.pointer = -1

    def push(self, v):
        if (self.pointer == len(self.stack) - 1):
            raise IndexError("Push to full Stack")
        else:
            self.pointer += 1
            self.stack[self.pointer] = v

    def peek(self):
        if (self.pointer == -1):
            raise IndexError("Empty Stack")
        return self.stack[self.pointer]

    def pop(self):
        if (self.pointer == -1):
            raise IndexError("Pop from empty Stack")
        else:
            poppedItem = self.stack[self.pointer]
            self.stack[self.pointer] = 0
            self.pointer -= 1
            return poppedItem


def checkParenthesesWithArrayStack(expression):
    pbStack = ArrayStack(len(expression))
    openBrackets = "({["
    closedBrackets = ")}]"
    error = 0
    for i in range(len(expression)):

        if (expression[i] in openBrackets):
            try:
                pbStack.push([expression[i], i + 1])
            except:
                error += 1
                print("Stack Overflow! Use a large size stack")
                break

        elif (expression[i] in closedBrackets):
            try:
                pbStack.peek()
                v = pbStack.pop()
            except:
                v = 0
            if (v == 0):
                print("This expression is NOT correct.")
                print("Error at character # {}. '{}'- not opened".format(i + 1, expression[i]))
                error += 1
                break
            elif (v[0] == "(" and expression[i] != ")"):
                print("This expression is NOT correct.")
                print("Error at character # {}. '{}'- not closed".format(v[1], v[0]))
                error += 1
                break
            elif (v[0] == "{" and expression[i] != "}"):
                print("This expression is NOT correct.")
                print("Error at character # {}. '{}'- not closed".format(v[1], v[0]))
                error += 1
                break
            elif (v[0] == "[" and expression[i] != "]"):
                print("This expression is NOT correct.")
                print("Error at character # {}. '{}'- not closed".format(v[1], v[0]))
                error += 1
                break
    if (error == 0):
        try:
            p = pbStack.peek()
            print("This expression is NOT correct.")
            print("Error at character # {}. '{}'- not closed".format(p[1], p[0]))
        except:
            print("This expression is correct.")


print("....\ Task 1 Array Stack /....")
print('#1')
checkParenthesesWithArrayStack("1+2*(3/4)")
print('\n#2')
checkParenthesesWithArrayStack("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
print('\n#3')
checkParenthesesWithArrayStack("1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14")
print('\n#4')
checkParenthesesWithArrayStack("1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
print('\n#5')
checkParenthesesWithArrayStack("{}{}")

print()


# Task 2
class ListStack:
    def __init__(self):
        self.head = None

    def peek(self):
        if (self.head is None):
            raise IndexError("Empty Stack")
        return self.head.value

    def pop(self):

        if (self.head is None):
            raise IndexError("Pop from empty Stack")
        poppedItem = self.head
        self.head = self.head.next
        oldData = poppedItem.value
        poppedItem.value = poppedItem.next = None
        return oldData

    def push(self, v):
        newItem = Node(v, None)
        if (self.head is None):
            self.head = newItem
        else:
            newItem.next = self.head
            self.head = newItem


def checkParenthesesWithListStack(expression):
    pbStack = ListStack()
    openBrackets = "({["
    closedBrackets = ")}]"
    error = 0
    for i in range(len(expression)):

        if (expression[i] in openBrackets):
            pbStack.push([expression[i], i + 1])

        elif (expression[i] in closedBrackets):
            try:
                pbStack.peek()
                v = pbStack.pop()
            except:
                v = 0
            if (v == 0):
                print("This expression is NOT correct.")
                print("Error at character # {}. '{}'- not opened".format(i + 1, expression[i]))
                error += 1
                break
            elif (v[0] == "(" and expression[i] != ")"):
                print("This expression is NOT correct.")
                print("Error at character # {}. '{}'- not closed".format(v[1], v[0]))
                error += 1
                break
            elif (v[0] == "{" and expression[i] != "}"):
                print("This expression is NOT correct.")
                print("Error at character # {}. '{}'- not closed".format(v[1], v[0]))
                error += 1
                break
            elif (v[0] == "[" and expression[i] != "]"):
                print("This expression is NOT correct.")
                print("Error at character # {}. '{}'- not closed".format(v[1], v[0]))
                error += 1
                break
    if (error == 0):
        try:
            p = pbStack.peek()
            print("This expression is NOT correct.")
            print("Error at character # {}. '{}'- not closed".format(p[1], p[0]))
        except:
            print("This expression is correct.")


print("....\ Task 2 Linked list Stack/....")
print('#1')
checkParenthesesWithListStack("1+2*(3/4)")
print('\n#2')
checkParenthesesWithListStack("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
print('\n#3')
checkParenthesesWithListStack("1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14")
print('\n#4')
checkParenthesesWithListStack("1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
print('\n#5')
checkParenthesesWithListStack("{}{}")