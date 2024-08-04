import tempfile
import os


def random_file():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Generate a random file name
    file_name = tempfile.NamedTemporaryFile(dir=temp_dir, delete=False).name
    # Return the path of the random file
    return file_name
