import warnings

from data_capture.errors import LackOfDataWarning
from data_capture.utils import args_in_range, args_with_integer_type


class DataCapture:
    """ """

    def __init__(self) -> None:
        self.numbers_count = [0] * 1001
        self.less_equal_numbers = [0] * 1001

        self.no_data = True

    @args_with_integer_type
    @args_in_range(0, 1000)
    def add(self, number: int) -> None:
        """
        Parameters
        ----------
        number: int
        """
        self.no_data = False
        self.numbers_count[number] += 1

    def build_stats(self) -> "DataCapture":
        """ """
        if self.no_data:
            warnings.warn("There is no data to compute", LackOfDataWarning)

        accumulated = 0
        for index, count in enumerate(self.numbers_count):
            accumulated += count

            self.less_equal_numbers[index] = accumulated

        return self

    @args_with_integer_type
    @args_in_range(0, 1000)
    def less(self, number: int) -> int:
        if number == 0:
            return 0
        return self.less_equal_numbers[number - 1]

    @args_with_integer_type
    @args_in_range(0, 1000)
    def greater(self, number: int) -> int:
        return self.less_equal_numbers[1000] - self.less_equal_numbers[number]

    @args_with_integer_type
    @args_in_range(0, 1000)
    def between(self, lower_limit: int, upper_limit: int) -> int:
        if lower_limit > upper_limit:
            lower_limit, upper_limit = upper_limit, lower_limit

        upper_limit = self.less_equal_numbers[upper_limit]
        lower_limit = (
            self.less_equal_numbers[lower_limit] - self.numbers_count[lower_limit]
        )

        return upper_limit - lower_limit
