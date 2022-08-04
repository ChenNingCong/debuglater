import sys
import pickle

from debuglater import pydump


def test_save_dump_without_dill(tmp_empty, monkeypatch):
    # simulate dill is not installed
    monkeypatch.setattr(pydump, 'dill', None)

    try:
        1 / 0
    except:
        tb = sys.exc_info()[2]

    pydump.save_dump('name.dump', tb=tb)
