#!/usr/local/bin/python

from networkx import *
import matplotlib.pyplot as plt
from networkx.algorithms.approximation import maximum_independent_set
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', metavar='f', help='input file', nargs='+')
    args = parser.parse_args()

    G = nx.read_adjlist(args.input_file[0])

    nx.draw(G)

    plt.show()
    plt.savefig("path.png")

    S = maximum_independent_set(G)

    print S


if __name__ == '__main__':
    main()
