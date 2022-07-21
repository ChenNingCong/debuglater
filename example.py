import numpy as np

x = np.random.rand(10)

try:
    1 / 0
except:
    import pydump
    pydump.run(__file__)
    raise
