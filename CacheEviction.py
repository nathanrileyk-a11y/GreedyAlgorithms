from collections import deque
from LinkedList import DoublyLinkedList


def load_data(file_path):
    with open(file_path, 'r') as file:
        first = file.readline()
        if first == '':
            raise ValueError("First line empty")
        print(first)
        line1 = first.split()
        if len(line1) != 2:
            print("Error: Ensure first line has 2 integers")
            return -1
        try:
            capacity = int(line1[0])
            num_requests = int(line1[1])

        except ValueError: 
            print("Error: Ensure first line contains only integers")

        assert capacity > 1, "Capacity must be greater than 0"
         
        second = file.readline()

        if not second:
            raise ValueError("Request line empty")
        
        requests = list(map(int,second.split()))

        if len(requests) != num_requests:
            raise ValueError("Number of requests in second line does not match number of requests stated in first line")
        return (capacity, requests, num_requests)
        
        

        
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

        print("misses", self.misses)

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
        

class OPTFF:
    def __init__(self, capacity):
        self.capacity = capacity
        self.misses = 0




capacity, requests, num_requests = load_data("data.txt")

print(capacity, requests, num_requests)

testObject = FIFO(capacity, requests, num_requests)