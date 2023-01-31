import sys

if __name__ == "__main__":
    # sys.exit(0)

    from concurrent.futures import ThreadPoolExecutor
    _d = {'f': 4, 'l':11}
    _l = ['a,', 'b','c']

    def logall(l):
        print(f"{l}\n{_d}\n\n")


    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(logall, _l)

