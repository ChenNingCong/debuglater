import sys

import pytest

from debuglater import pydump


@pytest.mark.parametrize(
    "path",
    [
        "name.dump",
        "path/to/file.dump",
    ],
)
def test_save_dump_without_dill(tmp_empty, monkeypatch, path):
    # simulate dill is not installed
    monkeypatch.setattr(pydump, "dill", None)

    try:
        1 / 0
    except Exception:
        tb = sys.exc_info()[2]

    pydump.save_dump(path, tb=tb)
