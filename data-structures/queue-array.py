class Queue:
    def __init__(self, capacity):
        self._items = [None] * capacity
        self._rear = -1
        self._head = 0
        self._size = 0
        self._capacity = capacity

    def __len__(self):
        return self._size

    def full(self):
        return len(self) == self._capacity

    def empty(self):
        return len(self) == 0

    def enqueue(self, item):
        if self.full():
            raise Exception("Queue is full!")

        if self._rear == self._capacity - 1:
            self._rear = 0
        else:
            self._rear += 1

        self._size += 1
        self._items[self._rear] = item

    def dequeue(self):
        if self.empty():
            raise Exception("Queue is empty!")

        self._size -= 1
        item = self._items[self._head]
        self._items[self._head] = None

        if self._head == self._capacity - 1:
            self._head = 0
        else:
            self._head += 1

        return item

    def peek(self):
        if self.empty():
            raise Exception("Queue is empty!")

        return self._items[self._head]

    def __str__(self):
        ret = ""
        temp = self._head
        for i in range(len(self)):
            ret += str(self._items[temp]) + " "
            if temp == self._capacity - 1:
                temp = 0
            else:
                temp += 1
        return ret

def main():
    q = Queue(10)
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
