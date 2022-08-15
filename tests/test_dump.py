from pathlib import Path
import subprocess
from unittest.mock import Mock

import numpy as np
import pandas as pd
import pytest

from debuglater import pydump

# we assume dill is installed for running these tests
try:
    import dill
    dill  # to keep flake8 happy
except ModuleNotFoundError:
    raise Exception('tests require dill')


def foo():
    foovar = 7  # noqa
    bar()


def bar():
    barvar = "hello"  # noqa
    list_sample = [1, 2, 3, 4]  # noqa
    dict_sample = {'a': 1, 'b': 2}  # noqa
    baz()


def baz():
    momo = Momo()
    momo.raiser()


def numpy():
    x = np.array([1, 2, 3])  # noqa
    1 / 0


def pandas():
    x = pd.DataFrame({'x': [1, 2, 3]})  # noqa
    1 / 0


class Momo(object):

    def __init__(self):
        self.momodata = "Some data"

    def raiser(self):
        x = 1  # noqa
        raise Exception("BOOM!")


def test_dump(capsys, monkeypatch):

    try:
        foo()
    except Exception:
        filename = __file__ + '.dump'
        pydump.run(filename)

    mock = Mock(side_effect=['print(f"x is {x}")', 'quit'])

    with monkeypatch.context() as m:
        m.setattr('builtins.input', mock)
        pydump.debug_dump(filename)

    out, _ = capsys.readouterr()

    assert 'x is 1' in out


def test_excepthook(capsys, monkeypatch):
    if Path('examples.crash.dump').is_file():
        Path('examples.crash.dump').unlink()

    subprocess.run(['python', 'examples/crash.py'])

    mock = Mock(side_effect=['print(f"x is {x}")', 'quit'])

    with monkeypatch.context() as m:
        m.setattr('builtins.input', mock)
        pydump.debug_dump('examples/crash.dump')

    out, _ = capsys.readouterr()

    assert 'x is 1' in out


@pytest.mark.parametrize('function, result', [
    [numpy, "type of x is <class 'numpy.ndarray'>"],
    [pandas, "type of x is <class 'pandas.core.frame.DataFrame'>"],
])
def test_data_structures(capsys, monkeypatch, function, result):

    try:
        function()
    except Exception:
        filename = __file__ + '.dump'
        pydump.run(filename)

    mock = Mock(side_effect=['print(f"type of x is {type(x)}")', 'quit'])

    with monkeypatch.context() as m:
        m.setattr('builtins.input', mock)
        pydump.debug_dump(filename)

    out, _ = capsys.readouterr()

    assert result in out
