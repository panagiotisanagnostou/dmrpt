"""Small inspector for the repository's pickle dumps.

Usage: python load_data.py path/to/file1.dump [path/to/file2.dump ...]

This script attempts to load each pickle file, detect common container types (dict, list, numpy arrays)
and prints a compact summary (keys, shapes, dtypes, sample values).
"""
import sys
import pickle
import os
from pprint import pprint

try:
    import numpy as np
except Exception:
    np = None
try:
    import pandas as pd
except Exception:
    pd = None


def summarize(obj, name=None, max_items=5):
    t = type(obj)
    header = f"== {name or 'object'}: {t.__name__} =="
    print(header)
    if isinstance(obj, dict):
        print(f"keys ({len(obj)}):", list(obj.keys())[:max_items])
        for k in list(obj.keys())[:max_items]:
            summarize(obj[k], name=f"{k}")
    elif isinstance(obj, (list, tuple)):
        print(f"length: {len(obj)}")
        for i, v in enumerate(obj[:max_items]):
            summarize(v, name=f"[{i}]")
    elif pd is not None and isinstance(obj, pd.DataFrame):
        print(f"pandas.DataFrame shape={obj.shape}")
        print("dtypes:")
        print(obj.dtypes.to_dict())
        print("head:")
        print(obj.head(3).to_string(index=False))
    elif np is not None and isinstance(obj, np.ndarray):
        print(f"numpy.ndarray shape={obj.shape} dtype={obj.dtype}")
        print("sample:")
        print(obj.flatten()[:min(obj.size, 10)])
    else:
        # fallback: print summary repr
        r = repr(obj)
        if len(r) > 200:
            r = r[:200] + '...'
        print(r)


def load_and_summarize(path):
    print(f"Loading: {path}")
    if not os.path.exists(path):
        print("  -> file not found")
        return 2
    try:
        with open(path, 'rb') as f:
            data = pickle.load(f)
    except Exception as e:
        print(f"  -> ERROR loading pickle: {e}")
        return 3
    summarize(data, name=os.path.basename(path))
    return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    exit_code = 0
    for p in sys.argv[1:]:
        code = load_and_summarize(p)
        if code != 0:
            exit_code = code
        print("\n")
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
