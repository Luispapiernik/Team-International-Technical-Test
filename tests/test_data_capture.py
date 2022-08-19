import pytest

from data_capture import (
    DataCapture,
    InvalidTypeError,
    LackOfDataWarning,
    OutOfRangeError,
)


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

    with pytest.warns(LackOfDataWarning) as record:
        data_capture.build_stats()
        assert len(record) == 1
        assert str(record[0].message) == "There is no data to compute"


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

    stats.between(2, 5)

    with pytest.raises(OutOfRangeError):
        data_capture.between(23, 1001)

    with pytest.raises(OutOfRangeError):
        data_capture.between(-1, 1001)


def test_add_method_raises_exception_with_invalid_type():
    data_capture = DataCapture()
    with pytest.raises(InvalidTypeError):
        data_capture.add(3.1)


def test_less_method_raises_exception_with_invalid_type():
    data_capture = DataCapture()

    data_capture.add(3)
    data_capture.add(9)
    data_capture.add(3)
    data_capture.add(4)
    data_capture.add(6)

    with pytest.raises(InvalidTypeError):
        data_capture.less(6.43)


def test_greater_method_raises_exception_with_invalid_type():
    data_capture = DataCapture()

    data_capture.add(3)
    data_capture.add(9)
    data_capture.add(3)
    data_capture.add(4)
    data_capture.add(6)

    with pytest.raises(InvalidTypeError):
        data_capture.greater(1.23)


def test_between_method_raises_exception_with_invalid_type():
    data_capture = DataCapture()

    data_capture.add(3)
    data_capture.add(9)
    data_capture.add(3)
    data_capture.add(4)
    data_capture.add(6)

    with pytest.raises(InvalidTypeError):
        data_capture.between(3.1415926, 2.71828)


def test_less_for_correct_values_1():
    data_capture = DataCapture()
    data_capture.add(3)
    data_capture.add(9)
    data_capture.add(3)
    data_capture.add(4)
    data_capture.add(6)

    stats = data_capture.build_stats()
    assert stats.less(0) == 0
    assert stats.less(1) == 0
    assert stats.less(2) == 0
    assert stats.less(3) == 0
    assert stats.less(4) == 2
    assert stats.less(5) == 3
    assert stats.less(6) == 3
    assert stats.less(7) == 4
    assert stats.less(8) == 4
    assert stats.less(9) == 4
    assert stats.less(10) == 5
    assert stats.less(234) == 5


def test_greater_for_correct_values_1():
    data_capture = DataCapture()
    data_capture.add(3)
    data_capture.add(9)
    data_capture.add(3)
    data_capture.add(4)
    data_capture.add(6)

    stats = data_capture.build_stats()
    assert stats.greater(1000) == 0
    assert stats.greater(200) == 0
    assert stats.greater(10) == 0
    assert stats.greater(9) == 0
    assert stats.greater(8) == 1
    assert stats.greater(7) == 1
    assert stats.greater(6) == 1
    assert stats.greater(5) == 2
    assert stats.greater(4) == 2
    assert stats.greater(3) == 3
    assert stats.greater(2) == 5
    assert stats.greater(1) == 5
    assert stats.greater(0) == 5


def test_between_for_correct_values_1():
    data_capture = DataCapture()
    data_capture.add(3)
    data_capture.add(9)
    data_capture.add(3)
    data_capture.add(4)
    data_capture.add(6)

    stats = data_capture.build_stats()
    assert stats.between(500, 754) == 0
    assert stats.between(10, 50) == 0
    assert stats.between(9, 15) == 1
    assert stats.between(8, 9) == 1
    assert stats.between(8, 10) == 1
    assert stats.between(5, 10) == 2
    assert stats.between(2, 8) == 4
    assert stats.between(0, 9) == 5
    assert stats.between(1, 7) == 4
    assert stats.between(0, 1000) == 5


def test_less_for_correct_values_2():
    data_capture = DataCapture()
    data_capture.add(3)
    data_capture.add(9)
    data_capture.add(3)
    data_capture.add(4)
    data_capture.add(5)
    data_capture.add(4)
    data_capture.add(2)
    data_capture.add(8)
    data_capture.add(8)
    data_capture.add(9)
    data_capture.add(1)
    data_capture.add(0)
    data_capture.add(1000)
    data_capture.add(0)

    stats = data_capture.build_stats()

    assert stats.less(0) == 0
    assert stats.less(1) == 2
    assert stats.less(2) == 3
    assert stats.less(3) == 4
    assert stats.less(4) == 6
    assert stats.less(5) == 8
    assert stats.less(6) == 9
    assert stats.less(7) == 9
    assert stats.less(8) == 9
    assert stats.less(9) == 11
    assert stats.less(10) == 13
    assert stats.less(100) == 13
    assert stats.less(1000) == 13


def test_greater_for_correct_values_2():
    data_capture = DataCapture()
    data_capture.add(3)
    data_capture.add(9)
    data_capture.add(3)
    data_capture.add(4)
    data_capture.add(5)
    data_capture.add(4)
    data_capture.add(2)
    data_capture.add(8)
    data_capture.add(8)
    data_capture.add(9)
    data_capture.add(1)
    data_capture.add(0)
    data_capture.add(1000)
    data_capture.add(0)

    stats = data_capture.build_stats()

    assert stats.greater(0) == 12
    assert stats.greater(1) == 11
    assert stats.greater(2) == 10
    assert stats.greater(3) == 8
    assert stats.greater(4) == 6
    assert stats.greater(5) == 5
    assert stats.greater(6) == 5
    assert stats.greater(7) == 5
    assert stats.greater(8) == 3
    assert stats.greater(9) == 1
    assert stats.greater(10) == 1
    assert stats.greater(100) == 1
    assert stats.greater(1000) == 0


def test_between_for_correct_values_2():
    data_capture = DataCapture()
    data_capture.add(3)
    data_capture.add(9)
    data_capture.add(3)
    data_capture.add(4)
    data_capture.add(5)
    data_capture.add(4)
    data_capture.add(2)
    data_capture.add(8)
    data_capture.add(8)
    data_capture.add(9)
    data_capture.add(1)
    data_capture.add(0)
    data_capture.add(1000)
    data_capture.add(0)

    stats = data_capture.build_stats()
    assert stats.between(0, 1000) == 14
    assert stats.between(1000, 0) == 14

    assert stats.between(0, 0) == 2
    assert stats.between(1000, 1000) == 1
    assert stats.between(3, 3) == 2
    assert stats.between(500, 500) == 0

    assert stats.between(1000, 9) == 3
    assert stats.between(9, 1000) == 3

    assert stats.between(0, 1) == 3
    assert stats.between(1, 0) == 3

    assert stats.between(1000, 0) == 14
    assert stats.between(1000, 0) == 14

    assert stats.between(1, 7) == 7
    assert stats.between(7, 1) == 7

    assert stats.between(0, 9) == 13
    assert stats.between(9, 0) == 13
