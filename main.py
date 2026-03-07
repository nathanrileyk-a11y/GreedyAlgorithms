from src import CacheEviction
from src import LinkedList
import sys

def load_data(file_path):
    with open(file_path, 'r') as file:
        first = file.readline()
        if first == '':
            raise ValueError("First line empty")

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
    if len(sys.argv) != 2:
        raise AssertionError("Must have only input file name as argument in command line")
    file_name = sys.argv[1]

    capacity, requests, num_requests = load_data(f"data/{file_name}")

    testObject = CacheEviction.FIFO(capacity, requests, num_requests)
    test3 = CacheEviction.LRU(capacity, requests, num_requests)
    for r in requests:
        test3.process(r)
    test3.print_accuracy()
    testOb2 = CacheEviction.OPTFF(capacity, requests, num_requests)

    out_name = file_name.rsplit('.', 1)[0] + '.out'
    with open(f"data/{out_name}", 'w') as f:
        f.write(f"FIFO  : {testObject.misses}\n")
        f.write(f"LRU   : {test3.misses}\n")
        f.write(f"OPTFF : {testOb2.misses}\n")

    return
main()



