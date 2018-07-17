#!/usr/bin/env python3

class Node:
    def __init__(self, left, right=0, subject=None):
        self.left = left
        self.right = right
        self.subject = subject

class Tree:
    def __init__(self):
        self.__root = 0
        self.__next_free_pos = 1
        self.__deleted = [False] * 31
        self.__subject_tree = [None]
        for i in range(1, 30):
            self.__subject_tree.append(Node(i + 1))
        self.__subject_tree.append(Node(0))

    def empty(self):
        return self.__root == 0

    def add_subject(self, subject):
        if self.empty():
            self.__root = self.__next_free_pos
        else:
            last_move = None
            cur_ptr = self.__root
            prev_ptr = None
            while cur_ptr != 0:
                prev_ptr = cur_ptr
                cur_node = self.__subject_tree[cur_ptr]
                if subject < cur_node.subject:
                    cur_ptr = cur_node.left
                    last_move = 'left'
                else:
                    cur_ptr = cur_node.right
                    last_move = 'right'

            prev_node = self.__subject_tree[prev_ptr]
            if last_move == 'left':
                prev_node.left = self.__next_free_pos
            elif last_move == 'right':
                prev_node.right = self.__next_free_pos

        node = self.__subject_tree[self.__next_free_pos]
        self.__next_free_pos = node.left
        node.left = 0
        node.subject = subject

    def display(self):
        print()
        print('Root:', self.__root)
        print('Next free position:', self.__next_free_pos)
        print()

        NODE_PRINT_FMT = '{:<5} {:<15} {:<5} {:<5}'
        print(NODE_PRINT_FMT.format('Index', 'Subject', 'Left', 'Right'))
        print('=' * 35)
        for i in range(1, len(self.__subject_tree)):
            node = self.__subject_tree[i]
            subject = '' if node.subject is None else node.subject
            print(NODE_PRINT_FMT.format(i, subject, node.left, node.right))

    def delete(self, subject):
        cur_ptr = self.__root
        prev_ptr = None
        found = False
        while not found and cur_ptr != 0:
            prev_ptr = cur_ptr
            cur_node = self.__subject_tree[cur_ptr]
            if subject > cur_node.subject:
                cur_ptr = cur_node.right
            elif subject < cur_node.subject:
                cur_ptr = cur_node.left
            else:
                self.__deleted[cur_ptr] = True
                found = True

        if found:
            new_tree = Tree()
            for i in range(1, self.__next_free_pos):
                if not self.__deleted[i]:
                    new_tree.add_subject(self.__subject_tree[i].subject)
        else:
            new_tree = self

        return new_tree

def build_tree():
    tree = Tree()
    with open('SUBJECT.txt') as file:
        for line in file:
            line = line.strip()
            tree.add_subject(line)
    return tree

def main():
    tree = build_tree()
    tree.display()
    tree = tree.delete('Chemistry')
    tree = tree.delete('History')
    tree.display()

main()
