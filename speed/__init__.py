def checkSpeed(func, r):
    import os, sys
    class noPrint:
        def __enter__(self):
            self._original_stdout = sys.stdout
            sys.stdout = open(os.devnull, 'w')
        def __exit__(self, exc_type, exc_val, exc_tb):
            sys.stdout.close()
            sys.stdout = self._original_stdout
    from time import perf_counter as pf
    start = pf()
    with noPrint():
        for _ in range(r):
            func()
    end = pf()
    print(f'{((end-start)/r):.8f}')
