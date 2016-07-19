# Simulation of immediate snapshot from atomic snapshots
# Vikram Saraph

import numpy as np
from random import choice
from copy import copy
from sys import argv

# Number of processes
N = 5
if len(argv) > 1:
	N = int(argv[1])

running = set(range(N))
level = N*[N+1]
snapshots = {q:None for q in xrange(N)}
imm = {}

while running:
	p = choice(tuple(running))
	snapshot = snapshots[p]
	if not snapshot:
		snapshots[p] = copy(level)
	elif len([l for l in snapshot if l <= level[p]]) < level[p]:
		snapshots[p] = None
		level[p] -= 1
	else:
		imm[p] = filter(lambda q: level[p] >= snapshot[q], xrange(N))
		running.remove(p)

print imm
