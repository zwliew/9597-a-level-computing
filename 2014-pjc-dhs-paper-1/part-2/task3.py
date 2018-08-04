#!/usr/bin/env python3

class Node:
    def __init__(self, name='', time=-1, next=None):
        self.name = name
        self.time = time
        self.next = next

class LinkedList:
    def __init__(self, max_size):
        self.__first = None
        self.__max_size = max_size
        self.__size = 0

    def Display(self):
        cur = self.__first
        print('{:10}{:10}{}'.format('Name', 'Time', 'Next name'))
        print('=' * 30)
        while cur is not None:
            if cur.next is not None:
                next_name = cur.next.name
            else:
                next_name = ''
            print('{:<10}{:<10}{:<10}'.format(cur.name, cur.time, next_name))
            cur = cur.next
        print()

    def AddFirst(self, node):
        if self.Full():
            print('Linked list is full. Failed to add node.')
            return

        node.next = self.__first
        self.__first = node
        self.__size += 1

    def RemoveFirst(self):
        if self.Empty():
            print('Linked list is empty. Failed to remove node.')
            return

        node = self.__first
        self.__first = self.__first.next

        return node

    def AddLast(self, node):
        if self.Full():
            print('Linked list is full. Failed to add node.')
            return

        if self.Empty():
            self.__first = node
        else:
            prev = None
            cur = self.__first
            while cur is not None:
                prev = cur
                cur = cur.next
            prev.next = node

        self.__size += 1

    def AddInOrder(self, node):
        if self.Full():
            print('Linked list is full. Failed to add node.')
            return

        prev = None
        cur = self.__first
        while cur is not None and cur.time <= node.time:
            prev = cur
            cur = cur.next

        if prev is None:
            self.AddFirst(node)
        else:
            node.next = prev.next
            prev.next = node

        self.__size += 1

    def RemoveLast(self):
        if self.Empty():
            print('Linked list is empty. Failed to remove node.')
            return

        prev = None
        cur = self.__first
        while cur.next is not None:
            prev = cur
            cur = cur.next

        node = prev.next
        prev.next = None
        self.__size -= 1

        return node

    def RemoveNode(self, name):
        if self.Empty():
            print('Linked list is empty. Failed to remove node.')
            return

        cur = self.__first
        prev = None
        while cur is not None and cur.name != name:
            prev = cur
            cur = cur.next

        if cur is None:
            return

        node = prev.next
        prev.next = cur.next
        self.__size -= 1

        return node

    def Empty(self):
        return self.__first is None

    def Full(self):
        return self.__size == self.__max_size

def main():
    RaceList = LinkedList(20)
    FreeList = LinkedList(20)
    for i in range(20):
        FreeList.AddLast(Node())

    print('Initial state of each list:')
    print('RaceList:')
    RaceList.Display()
    print('FreeList:')
    FreeList.Display()

    node = FreeList.RemoveFirst()
    node.name = 'Barry'
    node.time = 50.17
    RaceList.AddInOrder(node)

    node = FreeList.RemoveFirst()
    node.name = 'Gani'
    node.time = 49.56
    RaceList.AddInOrder(node)

    node = FreeList.RemoveFirst()
    node.name = 'Hong'
    node.time = 49.88
    RaceList.AddInOrder(node)

    node = FreeList.RemoveFirst()
    node.name = 'Ken'
    node.time = 49.32
    RaceList.AddInOrder(node)

    print('State of each list after adding the data:')
    print('RaceList:')
    RaceList.Display()
    print('FreeList:')
    FreeList.Display()

    RaceList.RemoveNode('Gani')

    print('State of each list after removal of Gani:')
    print('RaceList:')
    RaceList.Display()
    print('FreeList:')
    FreeList.Display()

main()
