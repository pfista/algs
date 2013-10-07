#!/usr/bin/python2.7

import argparse
from collections import defaultdict
""" Create an LCA Matrix representing node ancestors """

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', metavar='f', help='input file', nargs='+')
    args = parser.parse_args()

    f = open(args.input_file[0], "r")
    
    matrix = []

    nodes = defaultdict(list)

    i = 0

    for line in f:
        info = line.split()
        matrix.append([])
        children = info[1].split(',')
        if len(children) >= 2:
            left = children[0][1:]
            right = children[1][:1]
            nodes[int(info[0])].append(left)
            nodes[int(info[0])].append(right)
        # TODO: what to do with parent nodes?

        i += 1

    print nodes


if __name__ == '__main__':
    main()
