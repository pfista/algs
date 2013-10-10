#!/usr/bin/python2.7
""" Create an LCA Matrix representing node ancestors """

import argparse
import Queue
from sets import Set

class Node():
    """ Represents a node in a binary tree, when can have a left and right child
    as well as a parent """
    def __init__(self, left, right, parent, value):
        self.left = left
        self.right = right
        self.parent = parent
        self.children = []
        self.value = value

def descending_depth_list(nodes, root):
    """ Generate a list of the nodes descending based on their depth """ 
    q = Queue.Queue()
    level_order = Queue.LifoQueue()
    s = Set()
    q.put(root)
    s.add(root)
    while not q.empty():
        current = nodes[q.get()]
        level_order.put(current)
        if current.left is not None and current.left not in s:
            q.put(current.left)
            s.add(current.left)
        if current.right is not None and current.right not in s:
            q.put(current.right)
            s.add(current.right)
    return level_order

def main():
    """ Parse file input, assemble a dictionary, assemble a 2d matrix which
    provides O(1) lookup time for LCA of two keys in the dicitonary """
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', metavar='f', help='input file', nargs='+')
    args = parser.parse_args()

    # Open the input file to read
    lines = open(args.input_file[0], "r")
    nodes = dict()

    # Create a dictionary of nodes for each line from the input file
    for line in lines:
        info = line.split()
        children = info[1].split(',')
        try:
            key = int(info[0])
        except ValueError:
            print "malformed input, should be of format 'n (v,w) (p)'"
            break
        # Handle improper input by setting as None
        try:
            left = int(children[0][1:])
        except ValueError:
            left = None
        except IndexError:
            left = None
        try:
            right = int(children[1][:1])
        except ValueError:
            right = None
        except IndexError:
            right = None
        try:
            parent = int(info[2][1:-1])
        except ValueError:
            root = key
            parent = None

        nodes[key] = Node(left, right, parent, key)

    # Store LCA matrix here
    lca = [[0 for j in range(len(nodes))]for x in xrange(len(nodes))]

    # Do a breadth first search to determine the depth of each node, get a list
    # in descending order of depth
    level_order = descending_depth_list(nodes, root)

    # Visit each node from the bottom up, generate the lists at each node and
    # fill in the LCA Matrix as well
    while not level_order.empty():
        node = level_order.get()
        lca[node.value-1][node.value-1] = node.value
        if node.left is not None and node.right is not None:
            left = nodes[node.left].children
            right = nodes[node.right].children
            # Compare every child in the left subtree with every child from the
            # right subtree and fill in LCA accordingly for this node
            for i in range(len(left)):
                for j in range(len(right)):
                    # Matrix is symmetric but fill it in anyways
                    lca[left[i]-1][right[j]-1] = node.value
                    lca[right[j]-1][left[i]-1] = node.value
                    lca[node.value-1][left[i]-1] = node.value
                    lca[left[i]-1][node.value-1] = node.value
                    lca[node.value-1][right[j]-1] = node.value
                    lca[right[j]-1][node.value-1] = node.value
            # Update this nodes children to include itself plus everything that
            # its children contained
            node.children = [node.value] + nodes[node.left].children + \
                    nodes[node.right].children
        elif node.left is not None:
            node.children = nodes[node.left].children
            left = nodes[node.left].children
            for i in range(len(left)):
                lca[left[i]-1][node.value] = node.value
                lca[node.value][left[i]-1] = node.value
        elif node.right is not None:
            node.children = nodes[node.right].children
            right = nodes[node.right].children
            for j in range(len(right)):
                lca[node.value-1][right[j]-1] = node.value
                lca[right[j]-1][node.value-1] = node.value
        else:
            # We are at a leaf, so add itself to the children list
            node.children = [node.value]

    # Output resulting LCA matrix to file
    output = open("output.txt", 'w')
    for i in lca:
        for j in i:
            s = str(str(j)+' ')
            output.write(s)
        output.write('\n')
    output.close()

if __name__ == '__main__':
    main()
