# GreedyAlgorithms
Nathan King

Natahja Graddy - 69412034


## Run commands
Run input files with the following command:

**python main.py num.in (replace num with 1,2,3, etc.)**

## Written Solutions

## 1. Cache Eviction Results

1.in (k=4, m=100): FIFO=60, LRU=59, OPTFF=38

2.in (k=4, m=100): FIFO=74, LRU=71, OPTFF=45

3.in (k=8, m=200): FIFO=35, LRU=44, OPTFF=23

In each instance above, OPTFF has the fewest misses.
LRU and FIFO have similar performance results.

## 2. Bad Sequence for LRU or FIFO
Some example sequences that don't favor LRU or FIFO are

1. 1 2 3 4 4 2 5 3 1 2 9 2 3 3 10 2 1 3 5 2 (k=3, r=20)
2. 1 2 3 4 1 4 5 6 4 2 (k=3, r= 10)

The first case returns: 

FIFO  : 15

LRU   : 15

OPTFF : 10


The second case returns: 

FIFO  : 9

LRU   : 8

OPTFF : 6

The reason why OPTFF performs better than LRU and FIFO 
in these examples is due to their implementation. Since FIFO
gets rid of the oldest request in cache, regardless of how frequent 
the request may be, it will incur additional misses where persisting
a frequently used element would be a hit. LRU tries to avoid this by
retaining recently used requests in the cache. The efficiency of 
LRU sometimes suffers when cycle access patterns larger than the
capacity occur, as it loses data that may be recently accessed again
due to a request from a cycle not currently in the cache. OPTFF 
can give a more optimal solution in some sequences by removing elements
that are no longer needed in the future. It will find whichever element 
in the cache will no longer be used or has the farthest distance, and remove
it so cache elements with more frequent uses are maintained.

## Proof of Optimality of OPTFF

Assume That A is some offline algorithm, and assume OPT is the farthest in the future algorithm. At some point t, A and OPT differ. construct B by changing A(t) to OPT(t) and keeping everything else the same for A. Then at time t, B will evict the request furthest in the future, f. And A will evict some other request g. Then A will have f in the cache and B will have g. then B will occur a hit on g and A will occur a miss. Between f and g, A and B use same eviction policy so B will have identical cache to A outside of f. 

Then if f is reached, in one case A has f in the cache and is a hit, but B has a miss because f was evicted. Then since A and B are identical otherwise, A and B have the same number of misses. If A does not have f in cache, both miss and the number of misses in B is less than the number of misses in A. 
If f is never reached and g is reached, then B will have one less miss than A since it evicted f and in that one case, g was a miss for A but not B. 
If g and f are never reached, then the 2 evictions are equivelant so the number of misses will be the same. 
So, in all 4 cases, B has less or equal to the number of misses than A. we can keep applying this argument to all t where A and OPT differ. So for any offline algorithm A, the number of misses of OPT is <= the number of misses of A.