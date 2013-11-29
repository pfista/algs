#!/usr/bin/python2.7
""" Find a Eulerian tour given a graph represented by an adjacency list """

import argparse
import re

class Edge():
    """ Represents a weighted edge in a graph """
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def __gt__(self, other_edge):
        return self.weight > other_edge.weight

    def __eq__(self, other_edge):
        return self.u == other_edge.u and self.v == other_edge.v \
                or self.u == other_edge.v and self.v == other_edge.u

    def __repr__(self):
        return "["+ str(self.u) + ","+ str(self.v)+ "]"

def fail(reason):
    output = open("output.txt", 'w')
    output.write(reason)
    output.close()

def main():
    """ Parse file input, find a Eulerian tour if it exists """
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', metavar='f', help='input file', nargs='+')
    args = parser.parse_args()

    # Open the input file to read
    lines = open(args.input_file[0], "r")
    
    tour = [] # A list of vertices that represents a Eulerian tour
    edges = []
    vertices = []

    # Parse the data into an edge and vertex list
    for line in lines:
        data = line.split()
        vertices.append(data[0])
        edge_endpoints = data[1][1:-1].split()[0].split(',')

        if (len(edge_endpoints)%2 != 0):
            print "No tour exists, node has odd degree"
            fail("-1")
            return

        for v in edge_endpoints:
            edge = Edge(data[0], v, 1)
            if edge not in edges:
                edges.append(Edge(data[0], v, 1))
        
    # Recursive function to find a eulerian tour given an edgelist and starting
    # vertex
    def find_eulerian_tour(u, edges):
        for edge in edges:
            if u == edge.u:
                # If its the last edge, make it a tour back to the start
                if (len(edges) == 1):
                    tour.insert(0, edge.v)
                edges.remove(edge)
                find_eulerian_tour(edge.v, edges)
                tour.insert(0, edge.u)
            elif u == edge.v:
                if (len(edges) == 1):
                    tour.insert(0, edge.u)
                edges.remove(edge)
                find_eulerian_tour(edge.u, edges)
                tour.insert(0, edge.v)
        
    find_eulerian_tour(edges[0].u, edges)

    if tour[0] != tour[-1]:
        print "No tour found"
        fail("-1")
    else:
        print "Saving tour to output.txt"
        # Output resulting LCA matrix to file
        output = open("output.txt", 'w')
        last = 0
        for i in tour:
            output.write(i)
            if (last != len(tour) -1):
                output.write(' ')
            last += 1
        output.close()

if __name__ == '__main__':
    main()
