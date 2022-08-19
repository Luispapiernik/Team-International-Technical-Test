import warnings

from data_capture.errors import LackOfDataWarning
from data_capture.utils import args_in_range, args_with_integer_type


class DataCapture:
    """
    This class contains functionality to compute some basic statistics on a
    collection of small positive integers.
    """

    def __init__(self) -> None:
        self.numbers_count = [0] * 1001
        self.less_equal_numbers = [0] * 1001

        # Sentinel used to give a warning to the user when there is no data
        # added to compute the statistics
        self.no_data = True

    @args_with_integer_type
    @args_in_range(0, 1000)
    def add(self, number: int) -> None:
        """
        This method adds the numbers that will be used to compute the statistics.

        Parameters
        ----------
        number: int
            Number in the interval [0, 1000] (0 and 1000 contained) to be added.
        """
        self.no_data = False
        self.numbers_count[number] += 1

    def build_stats(self) -> "DataCapture":
        """
        This method compute the statistics of all the numbers added in previous
        steps.
        """
        if self.no_data:
            warnings.warn("There is no data to compute", LackOfDataWarning)

        accumulated = 0
        for index, count in enumerate(self.numbers_count):
            accumulated += count

            # Every position in the list contains the count of numbers less or
            # equal than the current index
            self.less_equal_numbers[index] = accumulated

        return self

    @args_with_integer_type
    @args_in_range(0, 1000)
    def less(self, number: int) -> int:
        """
        This method returns the count of numbers less than the given number,
        without counting the given number.

        Parameters
        ----------
        number: int
            Number for which the statistics will be compute.

        Returns
        -------
        out: int
            Statistic associated to the given number.
        """
        if number == 0:
            # There is no valid number less than 0
            return 0
        return self.less_equal_numbers[number - 1]

    @args_with_integer_type
    @args_in_range(0, 1000)
    def greater(self, number: int) -> int:
        """
        This method returns the count of numbers greater than the given number,
        without counting the given number.

        Parameters
        ----------
        number: int
            Number for which the statistics will be compute.

        Returns
        -------
        out: int
            Statistic associated to the given number.
        """
        return self.less_equal_numbers[1000] - self.less_equal_numbers[number]

    @args_with_integer_type
    @args_in_range(0, 1000)
    def between(self, lower_limit: int, upper_limit: int) -> int:
        """
        This method returns the count of numbers between a given range [a, b],
        counting the apparitions of "a" and "b".

        Parameters
        ----------
        lower_limit, upper_limit: int
            Limits for the interval, the order does not matter, that is,
            [lower_limit, upper_limit] is equivalence to [upper_limit, lower_limit]

        Returns
        -------
        out: int
            Statistic associated to the given range.
        """
        if lower_limit > upper_limit:
            lower_limit, upper_limit = upper_limit, lower_limit

        upper_limit = self.less_equal_numbers[upper_limit]
        lower_limit = (
            self.less_equal_numbers[lower_limit] - self.numbers_count[lower_limit]
        )

        return upper_limit - lower_limit
