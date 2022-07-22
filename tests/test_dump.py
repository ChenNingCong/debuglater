from unittest.mock import Mock

import numpy as np
import pandas as pd
import pytest

from debuglater import pydump


def foo():
    foovar = 7
    bar()


def bar():
    barvar = "hello"
    list_sample = [1, 2, 3, 4]
    dict_sample = {'a': 1, 'b': 2}
    baz()


def baz():
    momo = Momo()
    momo.raiser()


def numpy():
    x = np.array([1, 2, 3])
    1 / 0


def pandas():
    x = pd.DataFrame({'x': [1, 2, 3]})
    1 / 0


class Momo(object):

    def __init__(self):
        self.momodata = "Some data"

    def raiser(self):
        x = 1
        raise Exception("BOOM!")


def test_dump(capsys, monkeypatch):

    try:
        foo()
    except:
        filename = __file__ + '.dump'
        pydump.run(filename)

    mock = Mock(side_effect=['print(f"x is {x}")', 'quit'])

    with monkeypatch.context() as m:
        m.setattr('builtins.input', mock)
        pydump.debug_dump(filename)

    out, _ = capsys.readouterr()

    assert 'x is 1' in out


@pytest.mark.parametrize('function, result', [
    [numpy, "type of x is <class 'numpy.ndarray'>"],
    [pandas, "type of x is <class 'pandas.core.frame.DataFrame'>"],
])
def test_data_structures(capsys, monkeypatch, function, result):

    try:
        function()
    except:
        filename = __file__ + '.dump'
        pydump.run(filename)

    mock = Mock(side_effect=['print(f"type of x is {type(x)}")', 'quit'])

    with monkeypatch.context() as m:
        m.setattr('builtins.input', mock)
        pydump.debug_dump(filename)

    out, _ = capsys.readouterr()

    assert result in out
