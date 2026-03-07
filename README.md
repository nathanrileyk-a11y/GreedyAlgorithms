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

