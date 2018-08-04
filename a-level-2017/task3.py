#!/usr/bin/env python3

class ConnectionNode:
    def __init__(self, data_value=None, right_child=0, left_child):
        self.data_value = data_value
        self.right_child = right_child
        self.left_child = left_child

class NodeList:
    def __init__(self):
        self.__root = 0
        self.__next_free_child = 1
        self.__robot_data = [None]
        for i in range(1, 24):
            self.__robot_data.append(ConnectionNode(i + 1))
        self.__robot_data.append(ConnectionNode(0))

def main():
    node_list = NodeList()

main()
