#!/usr/bin/python2.7
""" Create a minimum spanning tree given an adjacency list """

import argparse
import re
import Queue
from sets import Set

class DisjointSet():
    """ A set of elements partitioned into a number disjoint subsets """

    def __init__(self):
        self.parents = {}
        self.rank = {}
        pass

    def make_set(self, x):
        """ Make a set for a single object """
        self.parents[x] = x
        self.rank[x] = 0

    def find(self, vertex):
        if self.parents[vertex] != vertex:
            self.parents[vertex] = self.find(self.parents[vertex])
        return self.parents[vertex]

    def union(self, u, v):
        if self.rank[u] < self.rank[v]:
            self.parents[u] = self.parents[v] # Add u to v's set
        elif self.rank[u] > self.rank[v]:
            self.parents[v] = self.parents[u] # Add v to u's set
        else:
            self.parents[v] = self.parents[u]
            self.rank[u] += 1 # Increase u's rank

    def __repr__(self):
        return str(self.parents)

class Edge():
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def __gt__(self, other_edge):
        return self.weight > other_edge.weight

    def __eq__(self, other_edge):
        return self.weight == other_edge.weight

    def __repr__(self):
        return str(self.weight)+"["+ str(self.u) + ","+ str(self.v)+ "]"

def main():
    """ Parse file input, assemble an ascending edge list, run Kruskal's
    algorithm on the graph from input """
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', metavar='f', help='input file', nargs='+')
    args = parser.parse_args()

    # Open the input file to read
    lines = open(args.input_file[0], "r")

    mst = [] # A list of edges to represent the minimum spanning tree
    edges = []
    vertices = []

    # Parse the data into an edge and vertex list
    for line in lines:
        data = map(int, re.findall('\d+', line))
        vertices.append(data[0])
        for i in range(1, len(data)-1, 2):
            edges.append(Edge(data[0], data[i], data[i+1]))

    # Disjoint set used to assemble the MST
    ds = DisjointSet()

    # Sort the list in ascending order
    edges = sorted(edges)

    # Execute Kruskal's Algorithm
    # For each vertex in list_vertices, init the DisjointSet
    for i in range (0, len(vertices)):
        ds.make_set(vertices[i])

    for i in range(0, len(edges)):
        if ds.find(edges[i].u) != ds.find(edges[i].v):
            mst.append(edges[i])
            ds.union(edges[i].u, edges[i].v)

    # Create the required formatted output for the MST
    out = [[]for x in xrange(len(vertices))]

    for edge in edges:
        out[edge.u-1].append(edge.v)
        out[edge.u-1] = sorted(out[edge.u-1])

    # Output resulting LCA matrix to file
    output = open("output.txt", 'w')
    for i in range(len(out)):
        output.write(str(i+1)+" (")
        last = 0
        for j in out[i]:
            s = str(j)
            if last != len(out[i])-1:
                s += ','
            last += 1
            output.write(s)
        output.write(')\n')
    output.close()

if __name__ == '__main__':
    main()
