import sys
import random


def main():
    capacity = int(sys.argv[1])
    num_requests = int(sys.argv[2])
    file_name = sys.argv[3]


    requests = []
    for i in range((num_requests)):
        requests.append(random.randint(1, 10))
    with open(file_name, 'w') as file:
        file.write(f"{capacity} {num_requests}\n")
        file.write(" ".join(map(str, requests)) + "\n")

main()
