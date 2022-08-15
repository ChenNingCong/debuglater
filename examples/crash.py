import sys
import debuglater

sys.excepthook = debuglater.excepthook_factory(__file__)

x = 1
y = 0

x / y
