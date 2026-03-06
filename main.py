from src import CacheEviction
from src import LinkedList

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
        
def main():
    capacity, requests, num_requests = load_data("data/data.txt")
    testObject = CacheEviction.FIFO(capacity, requests, num_requests)
    testOb2 = CacheEviction.OPTFF(capacity, requests, num_requests)
    test3 = CacheEviction.LRU(capacity, requests, num_requests)

    return




