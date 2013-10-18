#!/usr/bin/python2.7
""" Create a minimum spanning tree given an adjacency list """

import argparse
import Queue
from sets import Set

class DisjointSet():
    """ A set of elements partitioned into a number disjoint subsets """

    def __init__(self):
        pass

    def make_set(self, x):
        """ Make a set for a single object """
        x.parent = x
        x.root = 0

    def find(self):
        pass

    def union(self, u, v):
        pass

class Edge():
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

def main():
    """ Parse file input, assemble an ascending edge list, run Kruskal's
    algorithm on the graph from input """
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', metavar='f', help='input file', nargs='+')
    args = parser.parse_args()

    # Open the input file to read
    lines = open(args.input_file[0], "r")

    for line in lines:
        data = line.split()
        # Parse each line
        # Each line has
            # vertex
            # list of edges
            # weights for each edge
    # We now have
        # List of vertices
        # List of edges

    ds = DisjointSet()

    # For each vertex in list_vertices
    ds.make_set(0)

    # A list of edges to represent the minimum spanning tree
    mst = {}
    # For each ordered edge ascending:
        # if find(u) != find(v)
        # Add edge to MST
        # union (u, v)
    # return MST

if __name__ == '__main__':
    main()
