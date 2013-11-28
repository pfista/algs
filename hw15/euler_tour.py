#!/usr/bin/python2.7
""" Find a Eulerian tour given a graph represented by an adjacency list """

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
