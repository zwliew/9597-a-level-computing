class Node:
    def __init__(self, item, ptr = None):
        self.item = item
        self.ptr = ptr

class Queue:
    def __init__(self):
        self._size = 0
        self._head = None
        self._rear = None

    def __len__(self):
        return self._size

    def empty(self):
        return len(self) == 0

    def enqueue(self, item):
        node = Node(item)
        if self.empty():
            self._head = node
        else:
            self._rear.ptr = node
        self._rear = node
        self._size += 1

    def dequeue(self):
        if self.empty():
            raise Exception("Queue is empty!")

        item = self._head.item

        if self._head == self._rear:
            self._head = None
            self._rear = None
        else:
            self._head = self._head.ptr
        self._size -= 1

        return item

    def peek(self):
        if self.empty():
            raise Exception("Queue is empty!")

        return self._head.item

    def __str__(self):
        ret = ""
        cur = self._head

        while cur != None:
            ret += str(cur.item) + " "
            cur = cur.ptr

        return ret

def main():
    q = Queue()
    print ("Length:", len(q))
    print ("Empty:", q.empty())
    print ("Enqueue 1-10")
    for i in range(10):
        q.enqueue(i + 1)
    print ("Peeking:", q.peek())
    print ("Items (front to rear):", q)
    print ("Length:", len(q))
    print ("Empty:", q.empty())
    print ("Enqueue 11")
    try:
        q.enqueue(11)
    except Exception as e:
        print(e)
    print ("Dequeuing items (front to rear):", end = ' ')
    while not q.empty(): print (q.dequeue(), end = ' ')
    print ("\nLength:", len(q))
    print ("Empty:", q.empty())
    input('\nPlease press Enter or Return to quit the program.')

main()
