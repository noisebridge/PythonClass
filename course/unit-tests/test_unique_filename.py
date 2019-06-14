import pytest

from unique_filename import unique_filename

def test_unique_filename():
    """Test that a filename which is already unique is not modified."""
    filename = 'already-unqiue-filename.csv'

    with mock.patch('os.listdir', return_value=['existing_file.csv']):
        new_filename = unique_filename('.', filename)

    assert filename == new_filename


def test_type_error():
    """unique_filename() raises TypeError when not given strings."""
    with pytest.raises(TypeError):
        unique_filename('.', 7)
