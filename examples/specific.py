x = 1
y = 0

try:
    x / y
except Exception:
    import debuglater

    debuglater.run(__file__)
    raise
