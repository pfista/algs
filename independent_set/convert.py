#!/usr/bin/python2.7

import argparse
import re

def main():
    """ Converts an adjacency matrix to an adjacency list """
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', metavar='f', help='input file', nargs='+')
    args = parser.parse_args()

    # Open the input file to read
    lines = open(args.input_file[0], "r")
    
    edges = []
    vertices = []

    vertex = 1
    # Parse the data into an edge and vertex list
    for line in lines:
        data = line.split(' ')

        for x in range(0, len(data)):
            if data[x] == '1':
                print vertex, x

        vertex += 1
            
if __name__ == '__main__':
    main()
