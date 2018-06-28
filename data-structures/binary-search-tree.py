class Node:
    def __init__(self, left):
        self.LeftP = left
        self.RightP = 0
        self.Data = ''

class BinaryTree:
    SIZE = 20

    def __init__(self):
        self.Root = 0
        self.NextFreePosition = 1

        self.ThisTree = [None] * (BinaryTree.SIZE + 1)
        for i in range(1, BinaryTree.SIZE):
            self.ThisTree[i] = Node(i + 1)
        self.ThisTree[BinaryTree.SIZE] = Node(0)

    def IsFull(self):
        return self.NextFreePosition == 0

    def AddItemToBinaryTree(self, NewTreeItem):
        if self.IsFull():
            print('Binary tree is full!')
            return

        if self.Root == 0:
            self.Root = self.NextFreePosition
        else:
            CurrentPosition = self.Root
            LastMove = 'X'
            while CurrentPosition != 0:
                PreviousPosition = CurrentPosition
                if NewTreeItem < self.ThisTree[CurrentPosition].Data:
                    LastMove = 'L'
                    CurrentPosition = self.ThisTree[CurrentPosition].LeftP
                else:
                    LastMove = 'R'
                    CurrentPosition = self.ThisTree[CurrentPosition].RightP

            if LastMove == 'R':
                self.ThisTree[PreviousPosition].RightP = self.NextFreePosition
            else:
                self.ThisTree[PreviousPosition].LeftP = self.NextFreePosition

        NewNextFreePosition = self.ThisTree[self.NextFreePosition].LeftP
        self.ThisTree[self.NextFreePosition].LeftP = 0
        self.ThisTree[self.NextFreePosition].Data = NewTreeItem
        self.NextFreePosition = NewNextFreePosition

    def OutputData(self):
        print('Root: ' + str(self.Root))
        print('NextFreePosition: ' + str(self.NextFreePosition))
        print('Tree:')
        for i in range(1, 21):
            CurNode = self.ThisTree[i]
            print(str(i) + ': ' + str(CurNode.Data))

    def InOrderTraversal(self, index):
        if self.Root == 0:
            return 'Binary Tree is empty!'

        if index != 0:
            self.InOrderTraversal(self.ThisTree[index].LeftP)
            print(self.ThisTree[index].Data)
            self.InOrderTraversal(self.ThisTree[index].RightP)

def main():
    tree = BinaryTree()

    NewItem = input('Enter a new item:')
    while NewItem != 'XXX':
        tree.AddItemToBinaryTree(NewItem)
        NewItem = input('Enter a new item: ')

    tree.OutputData()

main()
