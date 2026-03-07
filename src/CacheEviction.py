from collections import deque, defaultdict
from .LinkedList import DoublyLinkedList
import bisect


class FIFO:
    def __init__(self, capacity, requests, num_requests):
        self.capacity = capacity
        self.misses = 0

        i = 0
        deleteKey = 0
        cacheElements = {}
        q = deque([])

        while i < len(requests):

            #hit
            if(requests[i] in cacheElements.values()):
                i += 1
                continue

            #miss
            else:
                #queue at capacity --> remove least used request and add latest request
                if (len(q) == capacity):

                    #deletion
                    removeElement = q.popleft()

                    for key in cacheElements:
                        if cacheElements[key] == removeElement:
                            deleteKey = key

                    del cacheElements[deleteKey]

                    #add new request
                    q.append(requests[i])
                    cacheElements[i] = requests[i]

                #queue not at capacity --> add new request
                else:
                    q.append(requests[i])
                    cacheElements[i] = requests[i]
                self.misses += 1

            i += 1

        print("Fifo Misses: ", self.misses)

class LRU:
    def __init__(self, capacity, requests, num_requests):
        self.capacity = capacity
        self.requests = requests
        self.num_requests = num_requests
        self.misses = 0
        self.cache = DoublyLinkedList()

    def process(self, request):
        if request in self.cache.hashmap:
            self.cache.delete(request)
            self.cache.insert_end(request)
            return
        else:
            self.misses += 1
        if len(self.cache.hashmap) == self.capacity:
            head = self.cache.head.data
            self.cache.delete(head)
        self.cache.insert_end(request)

    def print_accuracy(self):
        print("LRU Misses: ", self.misses)


#helper functions for OPTFF

#use binary search to find the first occurrence where request's index position is greater than i, if it exists
def getOccurence(cacheIndices, request, i):
    indices = cacheIndices[request]
    indexPos = bisect.bisect_right(indices, i)

    #request either occurs before i or not in list at all
    if indexPos == len(indices):
        return float("inf")

    return indices[indexPos]


#set initial occurrences of each element in request list into dictionary
def setIndices(requests, cacheIndices):
    for i, request in enumerate(requests):
        cacheIndices[request].append(i)

    return  cacheIndices

class OPTFF:

    def __init__(self, capacity, requests, num_requests):
        self.capacity = capacity
        self.misses = 0

        cacheIndices = defaultdict(list)
        setIndices(requests, cacheIndices)
        q = deque([])
        i = 0

        while i < len(requests):

            #hit
            if(requests[i] in q):
                i += 1
                continue

            #miss
            else:
                #queue at capacity --> remove least used request and replace with latest request
                if (len(q) == capacity):

                    #compare each request index and return max value between all requests
                    removeElement = max(q, key=lambda request: getOccurence(cacheIndices, request, i))
                    q.remove(removeElement)

                    # add new request
                    q.append(requests[i])

                #queue not at capacity --> add new request
                else:
                    q.append(requests[i])

                self.misses += 1

            i += 1

        print("OPTFF Misses: ", self.misses)
