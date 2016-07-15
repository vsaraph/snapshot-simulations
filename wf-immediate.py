# Simulation of immediate snapshot from atomic snapshots
# Vikram Saraph

import numpy as np
from random import choice
from copy import copy

# Number of processes
N = 4

running = set(range(N))
level = N*[N+1]
snapshots = {q:None for q in xrange(N)}
imm = {}

while running:
	p = choice(tuple(running))
	print "%d's turn" % p
	snapshot = snapshots[p]
	if not snapshot:
		snapshots[p] = copy(level)
	elif len([l for l in snapshot if l < N+1]) < N - t:
		snapshots[p] = None 
		continue
	elif len([l for l in snapshot if l <= level[p]]) < level[p]:
		print "%d dropping..." % p
		snapshots[p] = None
		level[p] -= 1
	else:
#		if len(filter(lambda q: level[p] >= snapshot[q], xrange(N))) < N - t:
#			continue
		imm[p] = filter(lambda q: level[p] >= snapshot[q], xrange(N))
		running.remove(p)
	print level

print imm
