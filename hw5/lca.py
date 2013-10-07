#!/usr/bin/python2.7
""" Create an LCA Matrix representing node ancestors """

import argparse

class Node():
    """ Represents a node in a binary tree, when can have a left and right child
    as well as a parent """
    def __init__(self, left, right, parent):
        self.left = left
        self.right = right
        self.parent = parent

def get_list(lca, nodes, key):
    """ Generate the LCA matrix and store it in lca """
    node = nodes[key]
    lca[key-1][key-1] = key
    if node.left is None and node.right is None:
        return [key]
    elif node.left is None:
        return [key] + get_list(lca, nodes, node.right)
    elif node.right is None:
        return [key] + get_list(lca, nodes, node.left)
    else:
        left_children = get_list(lca, nodes, node.left)
        right_children = get_list(lca, nodes, node.right)
        for i in range(len(left_children)):
            for j in range(len(right_children)):
                lca[left_children[i]-1][right_children[j]-1] = key
                lca[right_children[j]-1][left_children[i]-1] = key
                lca[key-1][left_children[i]-1] = key
                lca[key-1][right_children[j]-1] = key
                lca[left_children[i]-1][key-1] = key
                lca[right_children[j]-1][key-1] = key
        return [key] + left_children + right_children

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
            parent = None

        nodes[key] = Node(left, right, parent)

    # Create a list where each index i represents node i+1 and all contained
    # child nodes
    lists = [[]*len(nodes) for x in xrange(len(nodes))]
    # Store LCA matrix here
    lca = [[0 for j in range(len(nodes))]for x in xrange(len(nodes))]

    for key in nodes:
        lists[key-1] = (get_list(lca, nodes, key))

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
