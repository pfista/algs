#!/usr/local/bin/python

from networkx import *
import matplotlib.pyplot as plt

G = nx.read_adjlist("test.txt")

nx.draw(G)
plt.show()
plt.savefig("path.png")
