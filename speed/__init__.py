def showSpeed(func, r, *args):
    '''Usage: showSpeed(function, runs)
    You can also pass arguments into <function> like so:
    showSpeed(function, runs, <other>, <args>, <here> ...)

    showSpeed() prints the average execution time of <function> over <runs> runs
    '''
    def formatted(f):
        import re
        s = str(f)
        m = re.fullmatch(r'(-?)(\d)(?:\.(\d+))?e([+-]\d+)', s)
        if not m:
            return s
        sign, intpart, fractpart, exponent = m.groups('')
        exponent = int(exponent) + 1
        digits = intpart + fractpart
        if exponent < 0:
            return sign + '0.' + '0'*(-exponent) + digits
        exponent -= len(digits)
        return sign + digits + '0'*exponent + '.0'
    import os, sys, gc
    class noPrint:
        def __enter__(self):
            self._original_stdout = sys.stdout
            sys.stdout = open(os.devnull, 'w')
        def __exit__(self, exc_type, exc_val, exc_tb):
            sys.stdout.close()
            sys.stdout = self._original_stdout
    from time import perf_counter as pf
    garbage = gc.isenabled()
    gc.disable()
    start = pf()
    with noPrint():
        for _ in range(r):
            func(*args)
    end = pf()
    if garbage:
        gc.enable()
    print(f'{formatted((end-start)/r)}')

def getSpeed(func, r, *args):
    '''Usage: getSpeed(function, runs)
    You can also pass arguments into <function> like so:
    getSpeed(function, runs, <other>, <args>, <here> ...)

    getSpeed() returns the average execution time of <function> over <runs> runs, as a float
    '''
    import os, sys, gc
    class noPrint:
        def __enter__(self):
            self._original_stdout = sys.stdout
            sys.stdout = open(os.devnull, 'w')
        def __exit__(self, exc_type, exc_val, exc_tb):
            sys.stdout.close()
            sys.stdout = self._original_stdout
    from time import perf_counter as pf
    garbage = gc.isenabled()
    gc.disable()
    start = pf()
    with noPrint():
        for _ in range(r):
            func(*args)
    end = pf()
    if garbage:
        gc.enable()
    return (end-start)/r
