import warnings

from data_capture.errors import LackOfDataWarning, OutOfRangeError


def args_in_range(a, b):
    def decorator(obj_method):
        def wrapper(self, *args):
            for number in args:
                if number < a or b < number:
                    raise OutOfRangeError("Number out of range")

            return obj_method(self, *args)

        return wrapper

    return decorator


class DataCapture:
    """ """

    def __init__(self) -> None:
        self.numbers_count = [0] * 1001
        self.stats = {}

        self.no_data = True

    @args_in_range(0, 1000)
    def add(self, number: int) -> None:
        """
        Parameters
        ----------
        number: int
        """
        self.no_data = False
        self.numbers_count[number] += 1

    def build_stats(self) -> None:
        """ """
        if self.no_data:
            warnings.warn("There is no data to compute", LackOfDataWarning)

        self.stats = {}

        accumulated = 0
        for index, count in enumerate(self.numbers_count):
            self.stats[index] = accumulated
            accumulated += count

        return self

    @args_in_range(0, 1000)
    def less(self, number: int) -> int:
        return self.stats[number]

    @args_in_range(0, 1000)
    def greater(self, number: int) -> int:
        if number == 1000:
            return 0
        return self.stats[1000] - self.stats[number + 1]

    @args_in_range(0, 1000)
    def between(self, a: int, b: int) -> int:
        if b == 1000:
            return self.greater(a)
        else:
            return self.less(b + 1) - self.less(a)
