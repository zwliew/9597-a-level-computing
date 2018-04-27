""" Implementation of the Stack ADT using an array """
class Node():
    # The private storage class for creating stack nodes
    def __init__(self, item, link):
        self.item = item
        self.next = link

class Stack():
    # Array-based stack implementation

    # Creates an empty stack
    def __init__(self):
        self._top = None
        self._size = 0

    # Returns True if the stack is empty or False otherwise
    def isEmpty(self):
        return len(self) == 0

    # Returns the number of items in the stack
    def __len__(self):
        return self._size

    # Returns the top item on the stack without removing it
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty. Abort operation!!")

        return self._top.item

    # Removes and returns the top item on the stack
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty. Abort operation!")

        popped = self._top.item
        self._top = self._top.next
        self._size -= 1
        return popped

    # Push an item onto the top of the stack
    def push(self, item):
        self._top = Node(item, self._top)
        self._size += 1

def main():
    s = Stack()

    print ("Length:", len(s))
    print ("Empty:", s.isEmpty())
    print ("Popping items (top to bottom):", end = ' ')
    try:
        print (s.pop())
    except Exception:
        print("Empty array!")

    print ('--------------------------------------')
    print ("Push 1-10")
    for i in range(10):
        s.push(i + 1)
    print ("Peeking:", s.peek()) 
    print ("Length:", len(s))
    print ("Empty:", s.isEmpty())
    
    print ('--------------------------------------')
    print ("Push 11")
    try:
        s.push(11)
    except Exception:
        print("Full array!")

    print ("Popping items (top to bottom):", end = ' ')
    while not s.isEmpty():
        print (s.pop(), end = ' ')
    print ("\nLength:", len(s))
    print ("Empty:", s.isEmpty())    

main()
