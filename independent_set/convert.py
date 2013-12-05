#!/usr/bin/python2.7

import argparse

def main():
    """ Converts an adjacency matrix to an adjacency list """
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', metavar='f', help='input file', nargs='+')
    args = parser.parse_args()

    # Open the input file to read
    lines = open(args.input_file[0], "r")
    output = open("output.txt", 'w')

    vertex = 1 # Start default vertex to 1 
    # Parse the data into an edge and vertex list
    for line in lines:
        data = line.split(' ')

        output.write(str(vertex))
        for x in range(0, len(data)):
            if data[x] == '1':
                output.write(' '+str(x+1))
        output.write('\n')
        vertex += 1

    output.close()
            
if __name__ == '__main__':
    main()
