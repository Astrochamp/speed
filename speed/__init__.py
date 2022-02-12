def checkSpeed(func, r):
    from time import perf_counter as pf
    start = pf()
    with noPrint():
        for _ in range(r):
            func()
    end = pf()
    return f'{((end-start)/r):.8f}'
