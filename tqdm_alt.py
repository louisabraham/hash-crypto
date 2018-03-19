try:
    from tqdm import tqdm

except ImportError:
    import sys
    from time import time
    
    print('Missing tqdm module, alternative logging system activated', file=sys.stderr)
    print('You can install tqdm with `python3 -m pip install tqdm`', file=sys.stderr)

    def tqdm(iterable, total=None):
        if total is None:
            total = len(iterable)

        dbt = time()
        for i, line in zip(range(total), iterable):
            yield line
            if (i - 1) * 100 // total < i * 100 // total:
                print('\r%u%%' % (i * 100 // total), end='', file=sys.stderr)
        print('\r100%', file=sys.stderr)

        print('Finished in %u seconds' % (time() - dbt), file=sys.stderr)
