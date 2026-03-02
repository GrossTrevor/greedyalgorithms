import fifo, lru, optff

def main():
    k, m, r = parse('data/input.in')
    fifo_misses = fifo.fifo(k, r)
    lru_misses = lru.LRU_Test(k, r)
    # optff_misses = optff.optff(k, r)

    with open('data/output.out', 'w') as file:
        file.write(f'FIFO  : {fifo_misses}\n')
        file.write(f'LRU  : {lru_misses}\n')
        # file.write(f'OPTFF  : {optff_misses}\n')

"""
Data will be in the following format:
k m
r1 r2 r3 ... rm
"""
def parse(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        k, m = map(int, first_line.split())
        second_line = file.readline().strip()
        r = list(map(int, second_line.split()))
        return k, m, r

if __name__ == '__main__':
    main()