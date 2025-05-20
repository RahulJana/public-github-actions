import pytest


#%%
def manual_workflow():
    import numpy as np
    import time
    # Use numpy's Generator for random numbers with a seed
    rng = np.random.default_rng(seed=42)
    a = rng.random((20000, 2000))
    b = rng.random((2000, 20000))
    start = time.time()
    res = np.matmul(a, b)
    elapsed = time.time() - start
    print(f"Matmul took {elapsed:.2f} seconds.")
    return res


manual_workflow()
# %%
