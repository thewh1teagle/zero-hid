import tempfile
import os
import uuid
from contextlib import contextmanager


@contextmanager
def temp_path():
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, f"temp_{uuid.uuid4().hex}")
    try:
        yield file_path
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


def read_bytes(path) -> bytes:
    with open(path, "rb") as f:
        return f.read()
