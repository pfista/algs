#!/usr/bin/python2.7

import argparse
from collections import defaultdict
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
    
    nodes = defaultdict(Node)

    i = 0

    for line in lines:
        info = line.split()
        children = info[1].split(',')
        if len(children) >= 2:
            left = children[0][1:]
            right = children[1][:1]
            nodes[int(info[0])].append(left)
            nodes[int(info[0])].append(right)
        # TODO: what to do with parent nodes?
        parent = info[2][1:-1]
        nodes[int(info[0])].append(Node(left, right, parent))

        i += 1

    print nodes


if __name__ == '__main__':
    main()
