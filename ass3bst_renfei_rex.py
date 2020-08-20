#Assignment 3
#Algorithms and Data Structures 1 (1DL210)
#2019-10-18
#Author 1: Han, Renfei
#Author 2: Rex, Ruan

#This version is for Python3
#Description: A binary search tree is implemented
#             using class Node and BST
#Both inOrderWalkTree function and delete function are
#implemented as class method in BST
#OBS: The provided skeleton code is used in this file.

class Node():
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BST():
    '''it requires a list to initilize BST object'''
    def __init__(self, node_list):     #construct a binary search tree
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)

    def search(self, node, parent, data): #seach the node with data as key, return the node and its parents
        '''To search an integer as 'data' in the tree
        the output of the method returns
        whether the integer is in the tree, a node, and a parent'''
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)

    def insert(self, data):
        '''insert an integer 'data' into the tree'''
        flag, node, parent = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > parent.data:
                parent.rchild = new_node
            else:
                parent.lchild = new_node

    def delete(self, data):    #delete the node with data as its key from the tree
        '''delete an integer 'data' in the tree'''
        flag, node, parent = self.search(self.root, self.root, data)
        if flag is False:
            print("There is no such key in the tree !")
        else:
            if node.lchild is None:
                if node == self.root:  #n is the root
                    self.root = node.rchild
                else:
                    if node == parent.lchild:
                        parent.lchild = node.rchild
                    else:
                        parent.rchild = node.rchild
                del node
            elif node.rchild is None:
                if node == self.root:
                    self.root = node.lchild
                else:
                    if node == parent.lchild:
                        parent.lchild = node.lchild
                    else:
                        parent.rchild = node.lchild
                del node
            else:  # n has two children
                pre = node.rchild
                if pre.lchild is None:
                    node.data = pre.data
                    node.rchild = pre.rchild
                    del pre
                else:
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    node.data = next.data
                    pre.lchild = next.rchild
                    del next

    def inOrderWalk(self, node):
        '''to go through the subtree which has node as its root'''
        if node is not None:
            self.inOrderWalk(node.lchild)
            print(node.data)
            self.inOrderWalk(node.rchild)


