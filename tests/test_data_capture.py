import pytest

from data_capture import DataCapture, LackOfDataWarning, OutOfRangeError


# all numbers must be in the range [0, 1000] otherwise a exception must be raise
def test_add_method_raise_error_on_bad_range():
    data_capture = DataCapture()
    data_capture.add(3)
    data_capture.add(9)

    with pytest.raises(OutOfRangeError):
        data_capture.add(1001)

    data_capture.add(3)
    data_capture.add(4)

    with pytest.raises(OutOfRangeError):
        data_capture.add(-1)

    data_capture.add(6)


# If the user pass no data, a warning is raised but the execution is not
# interrupted by an exception
def test_build_stats_method_when_no_data():
    data_capture = DataCapture()

    with pytest.warns(LackOfDataWarning):
        stats = data_capture.build_stats()


# all numbers must be in the range [0, 1000] otherwise a exception must be raise
def test_less_method_raise_error_on_bad_range():
    data_capture = DataCapture()
    data_capture.add(3)
    data_capture.add(9)

    stats = data_capture.build_stats()

    with pytest.raises(OutOfRangeError):
        data_capture.less(-1)

    stats.less(200)

    with pytest.raises(OutOfRangeError):
        data_capture.less(1001)


# all numbers must be in the range [0, 1000] otherwise a exception must be raise
def test_greater_method_raise_error_on_bad_range():
    data_capture = DataCapture()
    data_capture.add(3)
    data_capture.add(9)

    stats = data_capture.build_stats()

    with pytest.raises(OutOfRangeError):
        data_capture.greater(-1)

    stats.greater(200)

    with pytest.raises(OutOfRangeError):
        data_capture.greater(1001)


# all numbers must be in the range [0, 1000] otherwise a exception must be raise
def test_between_method_raise_error_on_bad_range():
    data_capture = DataCapture()
    data_capture.add(3)
    data_capture.add(9)

    stats = data_capture.build_stats()

    with pytest.raises(OutOfRangeError):
        data_capture.between(-1, 10)

    stats.greater(2, 5)

    with pytest.raises(OutOfRangeError):
        data_capture.greater(23, 1001)

    with pytest.raises(OutOfRangeError):
        data_capture.greater(-1, 1001)
