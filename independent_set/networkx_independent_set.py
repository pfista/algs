#!/usr/local/bin/python

from networkx import *
import matplotlib.pyplot as plt
from networkx.algorithms.approximation import maximum_independent_set
import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', metavar='f', help='input file', nargs='+')
    parser.add_argument('num_loops', metavar='f', type=int, help='number of times to execute the algorithm', nargs='+')
    args = parser.parse_args()

    G = nx.read_adjlist(args.input_file[0])
    loops = args.num_loops[0]

    #nx.draw(G)

    plt.show()
    plt.savefig("path.png")

    startTime = datetime.now()
    for num in range(0,loops):
        S = maximal_independent_set(G)
        print len(S)
    endTime = datetime.now()
    #print endTime-startTime
        
if __name__ == '__main__':
    main()
