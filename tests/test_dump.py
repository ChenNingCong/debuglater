from unittest.mock import Mock

from pydump import debug_dump


def test_dump(capsys, monkeypatch):

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

    class Momo(object):

        def __init__(self):
            self.momodata = "Some data"

        def raiser(self):
            x = 1
            raise Exception("BOOM!")

    try:
        foo()
    except:
        import pydump
        filename = __file__ + '.dump'
        print("Exception caught, writing %s" % filename)
        pydump.save_dump(filename)
        print("Run 'python -m pydump %s' to debug" % (filename))

    mock = Mock(side_effect=['print(f"x is {x}")', 'quit'])

    with monkeypatch.context() as m:
        m.setattr('builtins.input', mock)
        debug_dump(filename)

    out, _ = capsys.readouterr()

    assert 'x is 1' in out
