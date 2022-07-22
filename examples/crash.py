x = 1
y = 0

try:
    x / y
except:
    import pydump
    pydump.run(__file__ + '.dump')
    raise