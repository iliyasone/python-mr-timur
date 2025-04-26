import time

def read_input(filename):
    with open(filename) as f:
        n, m, k = map(int, f.readline().split())
        occupied = set(tuple(map(int, line.split())) for line in f)
    return n, m, k, occupied

def is_pair_valid(row, i, occupied):
    if (row, i) in occupied or (row, i + 1) in occupied:
        return False
    for r in range(1, row):
        if (r, i) in occupied or (r, i + 1) in occupied:
            return False
    return True

def find_pair_slow(n, m, k, occupied):
    start_time = time.time()

    for row in range(m, 0, -1):
        # Progress print every 1000 rows
        if row % 10 == 0:
            elapsed = time.time() - start_time
            print(f"Checked up to row {m - row + 1}/{m}... elapsed: {int(elapsed)}s")

        for i in range(k - 1, 0, -1):
            if is_pair_valid(row, i, occupied):
                elapsed = time.time() - start_time
                print(f"\nFound! Total time: {elapsed:.2f} seconds")
                return row, i + 1

    print("No pair found.")
    return None

if __name__ == "__main__":
    n, m, k, occupied = read_input("files/26/26_17537.txt")
    result = find_pair_slow(n, m, k, occupied)
    if result:
        print(result[0], result[1])
