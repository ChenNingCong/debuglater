import sys
import pickle

from debuglater.pydump import FakeTraceback


def test_serialize_fake_traceback():
    try:
        1 / 0
    except:
        tb = sys.exc_info()[2]

    assert pickle.dumps(FakeTraceback(tb))