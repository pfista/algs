#!/usr/bin/python2.7

import argparse
""" Create an LCA Matrix representing node ancestors """

class Node():
    def __init__(self, left, right, parent):
        self.left = left
        self.right = right
        self.parent = parent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', metavar='f', help='input file', nargs='+')
    args = parser.parse_args()

    lines = open(args.input_file[0], "r")
    
    nodes = dict()

    for line in lines:
        info = line.split()
        children = info[1].split(',')
        if len(children) >= 2:
            if children[0][1:]:
                left = children[0][1:]
            if children[1][:1]:
                right = children[1][:1]
        try:
            parent = int(info[2][1:-1])
        except ValueError:
            parent = None

        nodes[int(info[0])] = Node(left, right, parent)

    for key in nodes:
        print key, nodes[key].left
        print key, nodes[key].right
        print key, nodes[key].parent


if __name__ == '__main__':
    main()
