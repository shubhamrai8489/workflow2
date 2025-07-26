import os
from file_written import write_to_file
def test_write_to_file():
    test_filename = "test_output.txt"
    test_content = "Test Content For CI"
    write_to_file(test_filename, test_content)

    assert os.path.exists(test_filename), "File Is Not Found"

    with open(test_filename, "r") as f:
        content = f.read()
        assert content == test_content, "File content do not match"